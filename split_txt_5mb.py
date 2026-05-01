#!/usr/bin/env python3
"""Split a text file into chunks of a fixed size (default: 5 MB)."""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_CHUNK_MB = 4


def split_text_file(input_file: Path, chunk_size_mb: int = DEFAULT_CHUNK_MB) -> list[Path]:
    """Split input_file into chunk_size_mb files and return created file paths."""
    if not input_file.exists() or not input_file.is_file():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    chunk_size_bytes = chunk_size_mb * 1024 * 1024
    output_dir = input_file.parent / f"{input_file.stem}_parts"
    output_dir.mkdir(parents=True, exist_ok=True)

    created_files: list[Path] = []
    part_index = 1
    current_size = 0
    writer = None

    def new_output_file(index: int):
        filename = output_dir / f"{input_file.stem}_part_{index:03d}{input_file.suffix}"
        file_handle = open(filename, "wb")
        return filename, file_handle

    try:
        out_path, writer = new_output_file(part_index)
        created_files.append(out_path)

        with open(input_file, "rb") as reader:
            for line in reader:
                line_len = len(line)

                # Start a new part when adding this line would exceed the limit.
                if current_size > 0 and current_size + line_len > chunk_size_bytes:
                    writer.close()
                    part_index += 1
                    out_path, writer = new_output_file(part_index)
                    created_files.append(out_path)
                    current_size = 0

                writer.write(line)
                current_size += line_len

    finally:
        if writer is not None and not writer.closed:
            writer.close()

    return created_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Split a .txt file into multiple files of fixed size (default 5 MB)."
    )
    parser.add_argument("input_file", type=Path, help="Path to the input .txt file")
    parser.add_argument(
        "--size-mb",
        type=int,
        default=DEFAULT_CHUNK_MB,
        help=f"Chunk size in MB (default: {DEFAULT_CHUNK_MB})",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.size_mb <= 0:
        raise ValueError("--size-mb must be greater than 0")

    files = split_text_file(args.input_file, args.size_mb)

    print(f"Created {len(files)} file(s):")
    for file_path in files:
        size_mb = file_path.stat().st_size / (1024 * 1024)
        print(f"- {file_path} ({size_mb:.2f} MB)")


if __name__ == "__main__":
    main()
