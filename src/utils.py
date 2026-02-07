"""Shared utility functions for file processing."""

import sys
import os


def read_data(filepath, converter=float):
    """
    Read numbers from a file (one number per line).

    Args:
        filepath: Path to the file to read
        converter: Function to convert each line (default: float)

    Returns:
        List of converted values
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    data = []
    skipped_lines = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            try:
                data.append(converter(line))
            except ValueError:
                skipped_lines.append((line_num, line))

    if skipped_lines:
        for line_num, line in skipped_lines:
            print(f"Warning: Skipped invalid data at line {line_num} in {filepath}: '{line}'")

    if not data:
        raise ValueError(f"File is empty or contains no valid data: {filepath}")

    return data


def save_results(output_lines, output_path):
    """
    Save results to a file.

    Args:
        output_lines: List of lines to write
        output_path: Full path to the output file
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(output_lines))
        print(f"\nResults saved to: {output_path}")
    except PermissionError:
        print(f"\nError: Permission denied writing to {output_path}")
        sys.exit(1)


def print_results(output_lines):
    """Print results to console."""
    for line in output_lines:
        print(line)


def print_skipped_files(skipped_files):
    """Print summary of skipped files."""
    if skipped_files:
        print(f"\nSkipped {len(skipped_files)} file(s): {', '.join(skipped_files)}")
