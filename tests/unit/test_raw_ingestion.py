import json

from retailiq.config.settings import SOURCE_PATH, RAW_PATH
from retailiq.ingestion.raw_ingestion import EXPECTED_SOURCE_FILES, ingest_source


def test_raw_ingestion_preserves_all_expected_sources(tmp_path):
    raw_dir = tmp_path / "raw"
    manifest_path = tmp_path / "manifest.json"

    manifest = ingest_source(
        SOURCE_PATH,
        raw_dir,
        manifest_path,
    )

    assert manifest["source_file_count"] == 9
    assert manifest_path.exists()

    for filename in EXPECTED_SOURCE_FILES:
        assert (raw_dir / filename).exists()

    saved = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert saved["source_file_count"] == 9

    for record in saved["records"]:
        assert record["source_sha256"] == record["raw_sha256"]
        assert record["source_size_bytes"] == record["raw_size_bytes"]
        assert record["row_count"] > 0
