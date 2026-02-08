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
        relative_path = os.path.relpath(output_path)
        print(f"\nResults saved to: {relative_path}")
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


def get_output_path(output_path, filepaths):
    """
    Get the output path, appending input filename if single file.

    Args:
        output_path: Base output path
        filepaths: List of input filepaths

    Returns:
        Modified output path
    """
    if len(filepaths) == 1:
        input_name = os.path.splitext(os.path.basename(filepaths[0]))[0]
        base, ext = os.path.splitext(output_path)
        return f"{base}_{input_name}{ext}"
    return output_path


def run_main(usage, process_fn, format_fn, output_path):
    """
    Common main function logic for file processing scripts.

    Args:
        usage: Usage string to display if no arguments provided
        process_fn: Function to process filepaths, returns (results, skipped_files)
        format_fn: Function to format results into output lines
        output_path: Path to save results
    """
    if len(sys.argv) < 2:
        print(usage)
        sys.exit(1)

    filepaths = sys.argv[1:]
    all_results, skipped_files = process_fn(filepaths)

    if not all_results:
        print("Error: No valid files to process")
        sys.exit(1)

    output_lines = format_fn(all_results)

    final_output_path = get_output_path(output_path, filepaths)

    print_results(output_lines)
    save_results(output_lines, final_output_path)
    print_skipped_files(skipped_files)
