from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = PROJECT_ROOT / "config" / "environment.yml"
SOURCE_PATH = PROJECT_ROOT / "data" / "source" / "olist"
RAW_PATH = PROJECT_ROOT / "data" / "raw"
STAGING_PATH = PROJECT_ROOT / "data" / "staging"
INTERMEDIATE_PATH = PROJECT_ROOT / "data" / "intermediate"
WAREHOUSE_PATH = PROJECT_ROOT / "data" / "warehouse"
MARTS_PATH = PROJECT_ROOT / "data" / "marts"
LOG_PATH = PROJECT_ROOT / "logs"
