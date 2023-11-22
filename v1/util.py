from pathlib import Path
from typing import Any

import srsly

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
