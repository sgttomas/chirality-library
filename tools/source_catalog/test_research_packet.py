import tools.source_catalog.research_packet as rp


def test_packet_slug_lowercases_and_underscores():
    assert rp.packet_slug("Demo Topic!") == "demo_topic"
    assert rp.packet_slug("Runtime  Stabilization") == "runtime_stabilization"
    assert rp.packet_slug("---") == "untitled"


def test_evidence_map_appends_new_columns_at_end():
    # The three new columns must be appended (never inserted) so positional readers don't break.
    assert rp.EVIDENCE_MAP_COLUMNS[-3:] == ["VerificationSource", "AssertionMode", "LoadBearing"]
    assert rp.EVIDENCE_MAP_COLUMNS[:18][-1] == "Limitations"


def test_query_log_columns_are_canonical():
    assert rp.QUERY_LOG_COLUMNS == [
        "QueryID", "UTC", "DomainRoot", "Snapshot", "Mode",
        "Query", "Filters", "K", "ResultCount", "Notes",
    ]


def test_amendment_candidate_columns_present():
    assert rp.AMENDMENT_CANDIDATE_COLUMNS[0] == "AmendmentID"
    assert "RecommendedRoute" in rp.AMENDMENT_CANDIDATE_COLUMNS
    assert "LoadBearing" in rp.AMENDMENT_CANDIDATE_COLUMNS


def test_packet_csv_files_cover_the_five_csvs():
    assert set(rp.PACKET_CSV_FILES) == {
        "Query_Log.csv", "Evidence_Map.csv", "Conflicts.csv",
        "Amendment_Candidates.csv", "Open_Questions.csv",
    }
