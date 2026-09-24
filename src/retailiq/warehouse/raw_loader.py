from __future__ import annotations

import csv
from pathlib import Path

import psycopg2
from psycopg2 import sql


CUSTOMER_COLUMNS = (
    "customer_id",
    "customer_unique_id",
    "customer_zip_code_prefix",
    "customer_city",
    "customer_state",
)


def load_env(path: Path) -> dict[str, str]:
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            values[key] = value
    return values


def connect():
    env = load_env(Path(".env"))
    return psycopg2.connect(
        host=env["POSTGRES_HOST"],
        port=int(env["POSTGRES_PORT"]),
        dbname=env["POSTGRES_DB"],
        user=env["POSTGRES_USER"],
        password=env["POSTGRES_PASSWORD"],
    )


def load_customers(source: Path, connection) -> int:
    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)

        if tuple(reader.fieldnames or ()) != CUSTOMER_COLUMNS:
            raise ValueError(
                f"Unexpected customer columns: {reader.fieldnames}"
            )

        rows = []
        for row in reader:
            rows.append(
                (
                    row["customer_id"],
                    row["customer_unique_id"],
                    int(row["customer_zip_code_prefix"])
                    if row["customer_zip_code_prefix"]
                    else None,
                    row["customer_city"],
                    row["customer_state"],
                )
            )

    if not rows:
        raise ValueError("Customer source contains no records")

    with connection:
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE raw.olist_customers")
            cursor.executemany(
                """
                INSERT INTO raw.olist_customers
                (
                    customer_id,
                    customer_unique_id,
                    customer_zip_code_prefix,
                    customer_city,
                    customer_state
                )
                VALUES (%s, %s, %s, %s, %s)
                """,
                rows,
            )

            cursor.execute("SELECT COUNT(*) FROM raw.olist_customers")
            database_count = cursor.fetchone()[0]

    if database_count != len(rows):
        raise RuntimeError(
            f"Customer reconciliation failed: source={len(rows)}, database={database_count}"
        )

    return database_count


if __name__ == "__main__":
    source_path = Path("data/raw/olist_customers_dataset.csv")
    connection = connect()
    try:
        count = load_customers(source_path, connection)
        print("GENERIC_RAW_LOADER_CUSTOMERS=PASS")
        print("SOURCE_ROW_COUNT=", count)
        print("DATABASE_ROW_COUNT=", count)
    finally:
        connection.close()
