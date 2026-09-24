import csv
from pathlib import Path

import psycopg2
from psycopg2 import sql


def load_env(path: Path) -> dict[str, str]:
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            values[key] = value
    return values


env = load_env(Path(".env"))
source = Path("data/raw/olist_customers_dataset.csv")

if not source.exists():
    raise FileNotFoundError(source)

connection = psycopg2.connect(
    host=env["POSTGRES_HOST"],
    port=int(env["POSTGRES_PORT"]),
    dbname=env["POSTGRES_DB"],
    user=env["POSTGRES_USER"],
    password=env["POSTGRES_PASSWORD"],
)

table = sql.Identifier("raw", "olist_customers")

try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                sql.SQL(
                    """
                    CREATE TABLE IF NOT EXISTS {} (
                        customer_id TEXT NOT NULL,
                        customer_unique_id TEXT NOT NULL,
                        customer_zip_code_prefix INTEGER,
                        customer_city TEXT,
                        customer_state TEXT
                    )
                    """
                ).format(table)
            )

            cursor.execute(sql.SQL("TRUNCATE TABLE {}").format(table))

            with source.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)

                required = {
                    "customer_id",
                    "customer_unique_id",
                    "customer_zip_code_prefix",
                    "customer_city",
                    "customer_state",
                }

                if set(reader.fieldnames or []) != required:
                    raise ValueError(
                        f"Unexpected source columns: {reader.fieldnames}"
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

    print("SOURCE_ROW_COUNT=", len(rows))
    print("DATABASE_ROW_COUNT=", database_count)
    print("TABLE=raw.olist_customers")

    if database_count != len(rows):
        raise RuntimeError(
            f"Row-count mismatch: source={len(rows)}, database={database_count}"
        )

    print("CUSTOMER_RAW_LOAD_STATUS=PASS")

finally:
    connection.close()
