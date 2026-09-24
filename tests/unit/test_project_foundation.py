from pathlib import Path

from retailiq.config.settings import (
    PROJECT_ROOT,
    SOURCE_PATH,
    RAW_PATH,
    STAGING_PATH,
    INTERMEDIATE_PATH,
    WAREHOUSE_PATH,
    MARTS_PATH,
)


def test_project_root_exists():
    assert PROJECT_ROOT.exists()
    assert (PROJECT_ROOT / "docs").exists()


def test_olist_source_exists():
    assert SOURCE_PATH.exists()
    assert len(list(SOURCE_PATH.glob("*.csv"))) == 9


def test_implementation_layers_exist():
    for path in (
        RAW_PATH,
        STAGING_PATH,
        INTERMEDIATE_PATH,
        WAREHOUSE_PATH,
        MARTS_PATH,
    ):
        assert path.exists()
