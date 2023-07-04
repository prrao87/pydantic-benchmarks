from pathlib import Path
from typing import Any

import srsly
from codetiming import Timer

from schemas import Wine

# Custom types
JsonBlob = dict[str, Any]


class FileNotFoundError(Exception):
    pass


def get_json_data(data_dir: Path, filename: str) -> list[JsonBlob]:
    """Get all line-delimited files from a directory with a given prefix"""
    file_path = data_dir / filename
    if not file_path.is_file():
        # File may not have been uncompressed yet so try to do that first
        data = srsly.read_gzip_jsonl(file_path)
        # This time if it isn't there it really doesn't exist
        if not file_path.is_file():
            raise FileNotFoundError(f"No valid .jsonl file found in `{data_dir}`")
    else:
        data = srsly.read_gzip_jsonl(file_path)
    return data


def validate(
    data: list[JsonBlob],
) -> list[JsonBlob]:
    """Validate a list of JSON blobs against the Wine schema"""
    validated_data = [Wine(**item).model_dump(exclude_none=True) for item in data]
    return validated_data


def run():
    """Wrapper function to time the validator over many runs"""
    with Timer(name="Single case", text="{name}: {seconds:.3f} sec"):
        validated_data = validate(data)
        print(f"Validated {len(validated_data)} records in cycle {i + 1} of {num}")


if __name__ == "__main__":
    DATA_DIR = Path("../data")
    FILENAME = "winemag-data-130k-v2.jsonl.gz"
    data = list(get_json_data(DATA_DIR, FILENAME))

    num = 10
    with Timer(name="All cases", text="{name}: {seconds:.3f} sec"):
        for i in range(num):
            run()
