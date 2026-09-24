import os
from pathlib import Path

import psycopg2


def load_env(path: Path) -> dict[str, str]:
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            values[key] = value
    return values


env = load_env(Path(".env"))

connection = psycopg2.connect(
    host=env["POSTGRES_HOST"],
    port=int(env["POSTGRES_PORT"]),
    dbname=env["POSTGRES_DB"],
    user=env["POSTGRES_USER"],
    password=env["POSTGRES_PASSWORD"],
)

schemas = (
    "raw",
    "staging",
    "intermediate",
    "warehouse",
    "marts",
    "semantic",
)

try:
    with connection:
        with connection.cursor() as cursor:
            for schema in schemas:
                cursor.execute(f'CREATE SCHEMA IF NOT EXISTS "{schema}"')

            cursor.execute(
                """
                SELECT schema_name
                FROM information_schema.schemata
                WHERE schema_name = ANY(%s)
                ORDER BY schema_name
                """,
                (list(schemas),),
            )

            found = [row[0] for row in cursor.fetchall()]

    if found != sorted(schemas):
        raise RuntimeError(
            f"Schema validation failed. Expected={sorted(schemas)}, Found={found}"
        )

    print("DATABASE_SCHEMA_COUNT=", len(found))
    for schema in found:
        print("SCHEMA=", schema)
    print("DATABASE_SCHEMA_STATUS=PASS")

finally:
    connection.close()
