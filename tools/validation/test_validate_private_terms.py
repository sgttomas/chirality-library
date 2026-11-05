import gzip
import io
import os
import subprocess
import sys
import zipfile
from pathlib import Path

import pytest

SCRIPT = Path(__file__).with_name('validate_private_terms.py')
# Synthetic machine names, assembled at runtime. They are invented, so the
# validator's own split-form matching of the fragments below is harmless.
TERM = 'Fixture' + 'Laptop' + '-Pro'
OTHER = 'old' + 'box.lan' + '.home'
RUN = 'projects/x/execution/_Coordination/AgentRuns/RUN-1/'
HOST_ATTR = 'host' + 'name'


@pytest.fixture
def repo(tmp_path):
    def git(*args, env=None):
        return subprocess.run(['git', *args], cwd=tmp_path, check=True, capture_output=True, text=True, env=env)
    git('init', '-q')
    git('config', 'user.name', 'Fixture')
    git('config', 'user.email', 'fixture@example.invalid')
    old = tmp_path / RUN / 'old.md'
    old.parent.mkdir(parents=True)
    old.write_text(f'line one\npre-existing history on {TERM}\n')  # history is not re-scanned
    git('add', '.')
    git('commit', '-qm', 'base')
    return tmp_path, git, git('rev-parse', 'HEAD').stdout.strip()


def write(root, files):
    for name, content in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content if isinstance(content, bytes) else content.encode())


def clean_env(**extra):
    env = {k: v for k, v in os.environ.items() if k not in ('PRIVATE_TERMS', 'GIT_EXTERNAL_DIFF')}
    env.update(extra)
    return env


def run(repo, files, terms=(TERM, OTHER), extra=(), commit=True, env_extra=None, commit_env=None, cwd=None):
    root, git, base = repo
    write(root, files)
    git('add', '.')
    env = clean_env(**(env_extra or {}))
    if terms:
        env['PRIVATE_TERMS'] = '\n'.join(terms)
    if commit:
        git('commit', '-qm', 'change', env=clean_env(**(commit_env or {})))
        span = ['--base', base, '--head', 'HEAD']
    else:
        span = ['--staged']
    return subprocess.run([sys.executable, str(SCRIPT), *span, *extra], cwd=cwd or root, env=env,
                          capture_output=True, text=True)


def no_term_in(result):
    text = (result.stdout + result.stderr).lower()
    return all(t.lower() not in text for t in (TERM, OTHER))


@pytest.mark.parametrize('form', [
    TERM,
    TERM.upper(),
    'Fixture' + '""' + 'Laptop' + '-Pro',                       # split by quotes
    'Fix' + '[t]' + 'ure' + '[-]' + 'Lap' + 'top' + '\\-Pro',   # character classes and escapes
    'fixture laptop pro',                                         # spaces
    'Fixture' + '\\u002d' + 'Laptop' + '\\u2019' + 'Pro',        # JSON escapes
    'Fixture' + '%20' + 'Laptop' + '%E2%80%99' + 'Pro',          # percent-encoding
    'Fixture' + '&#8217;' + 'Laptop' + '&#45;' + 'Pro',          # HTML entities
])
def test_term_in_any_form_blocks_without_printing_it(repo, form):
    result = run(repo, {'docs/notes.md': f'built on {form} today\n'})
    assert result.returncode == 1, result.stdout
    assert 'docs/notes.md:1: private term 1 (any form)' in result.stdout
    assert no_term_in(result)


def test_seven_separators_do_not_join(repo):
    result = run(repo, {'docs/notes.md': 'Fixture' + '-' * 7 + 'Laptop-Pro\n'})
    assert result.returncode == 0, result.stdout


def test_earlier_dotted_name_blocks(repo):
    result = run(repo, {RUN + 'screen.sh': 'PAT="old[.]box' + '[.]lan[.]home"\n'})
    assert result.returncode == 1
    assert 'private term 2' in result.stdout and no_term_in(result)


def test_terms_are_numbered_by_list_position(repo):
    result = run(repo, {'docs/notes.md': f'x\n{TERM}\n'}, terms=('mac', TERM))
    assert 'docs/notes.md:2: private term 2 (any form)' in result.stdout


def test_gzipped_evidence_is_decompressed(repo):
    result = run(repo, {RUN + 'suite.xml.gz': gzip.compress(f'<x>{TERM}</x>\n'.encode())})
    assert result.returncode == 1
    assert 'suite.xml.gz (decompressed):1: private term 1' in result.stdout


def test_undecompressible_gz_is_screened_raw(repo):
    result = run(repo, {RUN + 'fake.gz': f'not gzip at all {TERM}\n'})
    assert result.returncode == 1
    assert 'not decompressible' in result.stdout and 'fake.gz:1: private term 1' in result.stdout


def test_zip_members_are_screened(repo):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('inner.txt', ('padding ' * 50 + TERM + '\n'))
    result = run(repo, {RUN + 'bundle.zip': buffer.getvalue()})
    assert result.returncode == 1
    assert 'bundle.zip (zip member 1):1: private term 1' in result.stdout


@pytest.mark.parametrize('name, content', [
    ('docs/image.png', b'\x89PNG\x00\x00' + TERM.encode()),
    ('docs/notes-utf16.txt', ('hello ' + TERM).encode('utf-16-le')),
    (RUN + 'state.bin', b'\x00\x01\x02' + TERM.encode() + b'\x00'),
])
def test_binary_and_utf16_bytes_are_screened(repo, name, content):
    result = run(repo, {name: content})
    assert result.returncode == 1, result.stdout


def test_modified_file_scans_added_lines_only(repo):
    result = run(repo, {RUN + 'old.md': f'line one\npre-existing history on {TERM}\nnew clean line\n'})
    assert result.returncode == 0, result.stdout
    result = run(repo, {RUN + 'old.md': f'line one\npre-existing history on {TERM}\nnew clean line\nnow {TERM}\n'})
    assert result.returncode == 1
    assert 'old.md:4: private term 1' in result.stdout


def test_added_lines_starting_with_plus_plus_and_carriage_returns(repo):
    body = f'line one\npre-existing history on {TERM}\n'
    result = run(repo, {RUN + 'old.md': body + f'++{TERM}\nprogress 50%\r{TERM}\n'})
    assert result.returncode == 1
    assert 'old.md:3: private term 1' in result.stdout and 'old.md:4: private term 1' in result.stdout


def test_diff_settings_cannot_hide_added_lines(repo):
    root, git, base = repo
    write(root, {'.gitattributes': 'projects/x/** -diff\n'})
    git('add', '.')
    git('commit', '-qm', 'attributes')
    body = f'line one\npre-existing history on {TERM}\n'
    result = run(repo, {RUN + 'old.md': body + f'new {TERM}\n'},
                 env_extra={'GIT_EXTERNAL_DIFF': 'true'}, cwd=root / 'projects')
    assert result.returncode == 1, result.stdout
    assert 'old.md:3: private term 1' in result.stdout


def test_paths_are_screened_and_masked(repo):
    result = run(repo, {f'logs/{TERM}.log': 'clean content\n'})
    assert result.returncode == 1
    assert 'path logs/<host>.log: private term 1' in result.stdout and no_term_in(result)


def test_commit_identity_and_message_are_screened(repo):
    email = 'me@' + TERM + '.local'
    result = run(repo, {'docs/notes.md': 'clean\n'},
                 commit_env={'GIT_AUTHOR_EMAIL': email, 'GIT_COMMITTER_EMAIL': email})
    assert result.returncode == 1
    assert 'author email: private term 1' in result.stdout
    assert 'committer email: private term 1' in result.stdout and no_term_in(result)


def test_staged_mode_screens_the_next_commit_identity(repo):
    result = run(repo, {'docs/notes.md': 'clean\n'}, commit=False,
                 env_extra={'GIT_AUTHOR_EMAIL': 'me@' + TERM + '.local'})
    assert result.returncode == 1
    assert "the next commit's author identity: private term 1" in result.stdout


@pytest.mark.parametrize('path', [RUN + 'py.xml', 'tools/fixtures/py.xml'])
@pytest.mark.parametrize('attr', [
    f'{HOST_ATTR}="build-17.example"',
    f"{HOST_ATTR}='build-17.example'",
    f'{HOST_ATTR} = "build-17.example"',
    f'{HOST_ATTR}=\\"build-17.example\\"',
])
def test_junit_host_attribute_blocks_anywhere_without_terms(repo, path, attr):
    result = run(repo, {path: f'<testsuites {attr}><testsuite name="pytest">x</testsuite></testsuites>\n'}, terms=())
    assert result.returncode == 1, result.stdout
    assert 'junit hostname attribute' in result.stdout
    assert 'NOTE: no private terms configured' in result.stdout


@pytest.mark.parametrize('value', ['', '<host>', '&lt;host&gt;'])
def test_junit_placeholder_or_empty_host_passes(repo, value):
    suite = f'<testsuite name="pytest" {HOST_ATTR}="{value}">x</testsuite>\n'
    result = run(repo, {RUN + 'py.xml.gz': gzip.compress(suite.encode())}, terms=())
    assert result.returncode == 0, result.stdout


def test_no_terms_passes_with_a_note(repo):
    result = run(repo, {'docs/notes.md': f'{TERM}\n'}, terms=())
    assert result.returncode == 0
    assert 'NOTE: no private terms configured' in result.stdout


def test_required_terms_missing_is_an_error(repo):
    result = run(repo, {'docs/notes.md': 'clean\n'}, terms=(), extra=['--require-terms'])
    assert result.returncode == 2
    assert 'required' in result.stderr


def test_unreadable_terms_file_is_an_error(repo, tmp_path_factory):
    missing = tmp_path_factory.mktemp('private') / 'absent.txt'
    result = run(repo, {'docs/notes.md': f'{TERM}\n'}, terms=(), extra=['--terms-file', str(missing)])
    assert result.returncode == 2 and no_term_in(result)


def test_terms_file_and_staged_mode(repo, tmp_path_factory):
    terms = tmp_path_factory.mktemp('private') / 'terms.txt'
    terms.write_text(f'# names\n\n{TERM}\n')
    result = run(repo, {'docs/notes.md': f'{TERM}\n'}, terms=(), extra=['--terms-file', str(terms)], commit=False)
    assert result.returncode == 1
    assert 'docs/notes.md:1: private term 1' in result.stdout and no_term_in(result)


def test_short_terms_are_not_screened(repo):
    result = run(repo, {'docs/notes.md': 'a mac and a pc\n'}, terms=('mac', 'pc'))
    assert result.returncode == 0
    assert '2 term(s) shorter than 6' in result.stdout


def test_truncated_gz_is_screened_as_far_as_it_decompresses(repo):
    whole = gzip.compress((f'{TERM}\n' + 'filler line\n' * 2000).encode())
    result = run(repo, {RUN + 'cut.xml.gz': whole[: len(whole) // 2]})
    assert result.returncode == 1
    assert 'not decompressible' in result.stdout and '(partly decompressed):1: private term 1' in result.stdout


def test_zip_with_an_undecodable_member_name_does_not_crash(repo):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as archive:
        archive.writestr('member.txt', 'clean\n')
    data = buffer.getvalue().replace(b'member.txt', b'membe\xff.txt')
    # mark the names as UTF-8 (general-purpose flag bit 11) in both headers
    data = data.replace(b'PK\x03\x04\x14\x00\x00\x00', b'PK\x03\x04\x14\x00\x00\x08')
    data = data.replace(b'PK\x01\x02\x14\x03\x14\x00\x00\x00', b'PK\x01\x02\x14\x03\x14\x00\x00\x08')
    result = run(repo, {RUN + 'odd.zip': data + TERM.encode()})
    assert 'Traceback' not in result.stderr
    assert result.returncode == 1 and 'odd.zip' in result.stdout


def test_commit_message_after_a_record_separator_is_screened(repo):
    root, git, base = repo
    write(root, {'docs/notes.md': 'clean\n'})
    git('add', '.')
    git('commit', '-qm', 'subject\n\nbody \x1e then ' + TERM)
    env = clean_env(PRIVATE_TERMS=TERM)
    result = subprocess.run([sys.executable, str(SCRIPT), '--base', base, '--head', 'HEAD'], cwd=root, env=env,
                            capture_output=True, text=True)
    assert result.returncode == 1
    assert 'message: private term 1' in result.stdout and no_term_in(result)
