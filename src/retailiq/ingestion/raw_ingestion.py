from __future__ import annotations

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


EXPECTED_SOURCE_FILES = (
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def count_csv_rows(path: Path) -> int:
    import csv

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        next(reader, None)
        return sum(1 for _ in reader)


def ingest_source(source_dir: Path, raw_dir: Path, manifest_path: Path) -> dict:
    source_dir = source_dir.resolve()
    raw_dir = raw_dir.resolve()
    manifest_path = manifest_path.resolve()

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    raw_dir.mkdir(parents=True, exist_ok=True)

    records = []

    for filename in EXPECTED_SOURCE_FILES:
        source_file = source_dir / filename

        if not source_file.is_file():
            raise FileNotFoundError(f"Expected source file not found: {source_file}")

        raw_file = raw_dir / filename
        shutil.copy2(source_file, raw_file)

        source_hash = sha256_file(source_file)
        raw_hash = sha256_file(raw_file)

        if source_hash != raw_hash:
            raise ValueError(f"Checksum mismatch after raw copy: {filename}")

        records.append(
            {
                "source_filename": filename,
                "raw_filename": filename,
                "source_size_bytes": source_file.stat().st_size,
                "raw_size_bytes": raw_file.stat().st_size,
                "source_sha256": source_hash,
                "raw_sha256": raw_hash,
                "row_count": count_csv_rows(source_file),
            }
        )

    manifest = {
        "project": "RetailIQ",
        "layer": "raw",
        "ingestion_type": "source-preserving-copy",
        "ingested_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_file_count": len(records),
        "records": records,
    }

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, indent=2),
        encoding="utf-8",
    )

    return manifest

