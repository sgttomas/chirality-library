//! Bounded external-package probe; no registration, supply, execution or adoption.
//! Consumer: chirality-app 366e7a6656d807142e7bdeda0ccf99c37d7227b1.
//! Input: Root 1357d706ea77497903976bf159f3880bea4d1360 coordinated-knowledge-work.
//! In a complete disposable App export, copy this file into app/src-tauri/src/
//! and append `#[cfg(test)] mod app_workflow_reader;` to src/lib.rs.
//! Set CHIRALITY_READER_PACKAGE to the unmodified exported package directory,
//! CHIRALITY_READER_SCRATCH to an owned temporary directory. Run offline/locked:
//! cargo test --lib app_workflow_reader::root_package_capture -- --exact --nocapture --test-threads=1
//! Use an isolated Cargo home and target; follow any local build-resource policy.

use crate::util::sha256_hex;
use crate::workflow_declaration::Reading;
use crate::workflow_workspace::{Snapshot, SNAPSHOT_METHOD};
use std::{env, fs, path::PathBuf};

#[test]
fn root_package_capture() {
    let package =
        PathBuf::from(env::var_os("CHIRALITY_READER_PACKAGE").expect("package input required"));
    let scratch =
        PathBuf::from(env::var_os("CHIRALITY_READER_SCRATCH").expect("owned scratch required"));
    let captured = Snapshot::capture(&package).expect("actual App capture");
    let declaration = captured
        .declaration()
        .expect("actual App declaration reader");
    println!(
        "{}",
        serde_json::json!({
            "method": SNAPSHOT_METHOD, "revision": captured.revision(),
            "files": captured.manifest(), "declaration": declaration,
            "hygiene_findings": captured.hygiene_findings()
        })
    );
    assert_eq!(SNAPSHOT_METHOD, "chirality.app.workflow-package.sha256/v1");
    let expected = [
        (
            "REVIEW-NOTES.md",
            "0ae8867dc3010f99feb0251756f0008fb67dd57ff96a1af70125f688c91d055d",
        ),
        (
            "WORKFLOW.md",
            "0488a744eb163fc633e1ae356de1955a58e9ca1f6396ef6b028c2e8ffad75355",
        ),
    ];
    assert_eq!(
        captured.files().len(),
        expected.len(),
        "complete selected package"
    );
    for (name, digest) in expected {
        let bytes = &captured.files()[name];
        assert_eq!(bytes, &fs::read(package.join(name)).unwrap());
        assert_eq!(sha256_hex(bytes), digest, "Root source bytes: {name}");
    }
    assert_eq!(declaration.reading, Reading::Undeclared);
    assert!(declaration.raw.is_none());
    assert_eq!(declaration.categories.len(), 5);
    assert!(declaration
        .categories
        .values()
        .all(|r| *r == Reading::Undeclared));
    assert!(declaration.findings.is_empty());
    assert!(captured.hygiene_findings().is_empty());

    // WD RV-1/RV-3 and CC-CONTENT-IDENTITY: location is not content;
    // companion bytes are content even when WORKFLOW.md is unchanged.
    let relocated = scratch.join(format!("relocated-{}", std::process::id()));
    fs::create_dir(&relocated).expect("fresh relocation directory");
    for (name, bytes) in captured.files() {
        fs::write(relocated.join(name), bytes).unwrap();
    }
    let same = Snapshot::capture(&relocated).unwrap();
    assert_eq!(same.files(), captured.files());
    assert_eq!(same.revision(), captured.revision());
    let mut adapted = captured.files()["REVIEW-NOTES.md"].clone();
    adapted.extend_from_slice(b"\nFixture-only controlled byte change.\n");
    fs::write(relocated.join("REVIEW-NOTES.md"), &adapted).unwrap();
    let changed = Snapshot::capture(&relocated).unwrap();
    assert_eq!(
        changed.files()["WORKFLOW.md"],
        captured.files()["WORKFLOW.md"]
    );
    assert_eq!(changed.files()["REVIEW-NOTES.md"], adapted);
    assert_ne!(changed.revision(), captured.revision());
    assert_eq!(
        Snapshot::capture(&package).unwrap().files(),
        captured.files()
    );
    println!(
        "{}",
        serde_json::json!({
            "relocation_preserves_identity": true,
            "resource_byte_change_revision": changed.revision(),
            "original_input_unchanged": true
        })
    );
    fs::remove_dir_all(relocated).unwrap();
}
