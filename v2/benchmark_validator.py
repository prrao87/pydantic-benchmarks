from pathlib import Path
from typing import Any

import pytest
import util
from schemas import Wine
from schemas_optimized import WinesTypeAdapter

# Custom types
JsonBlob = dict[str, Any]


@pytest.fixture
def data():
    """Load the data once per session"""
    DATA_DIR = Path("../data")
    FILENAME = "winemag-data-130k-v2.jsonl.gz"
    data = list(util.get_json_data(DATA_DIR, FILENAME))
    return data


def validate(data: list[JsonBlob]) -> list[JsonBlob]:
    """Validate a list of JSON blobs against the Wine schema"""
    validated_data = [Wine(**item).model_dump(exclude_none=True, by_alias=True) for item in data]
    return validated_data


def test_validate(benchmark, data):
    """Validate the data"""
    result = benchmark(validate, data)
    assert len(result) == len(data)


def test_validate_optimized(benchmark, data):
    """Validate a list of JSON blobs against the Wine schema"""
    result = benchmark(WinesTypeAdapter.validate_python, data)
    assert len(result) == len(data)
