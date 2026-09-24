from pathlib import Path

from retailiq.config.settings import SOURCE_PATH, RAW_PATH
from retailiq.ingestion.raw_ingestion import ingest_source

manifest_path = RAW_PATH / "ingestion_manifest.json"
manifest = ingest_source(SOURCE_PATH, RAW_PATH, manifest_path)

print(f"RAW_FILES={manifest['source_file_count']}")
print(f"MANIFEST={manifest_path}")
for record in manifest["records"]:
    print(
        f"{record['source_filename']} | "
        f"rows={record['row_count']} | "
        f"sha256={record['source_sha256']}"
    )
