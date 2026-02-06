"""Main script to compute statistics from a file."""

import sys
import time
import os

from src.stats import count, mean, median, mode, variance, standard_deviation

RESULTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'results', 'p1')


def read_data(filepath):
    """Read numbers from a file (one number per line)."""
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
                data.append(float(line))
            except ValueError:
                skipped_lines.append((line_num, line))

    if skipped_lines:
        for line_num, line in skipped_lines:
            print(f"Warning: Skipped invalid data at line {line_num} in {filepath}: '{line}'")

    if not data:
        raise ValueError(f"File is empty or contains no valid data: {filepath}")

    return data


def compute_statistics(filepath):
    """Compute statistics for a single file and return results."""
    start_time = time.time()
    data = read_data(filepath)

    results = {
        'Count': count(data),
        'Mean': mean(data),
        'Median': median(data),
        'Mode': mode(data),
        'Var': variance(data),
        'Std': standard_deviation(data),
    }

    elapsed_time = time.time() - start_time
    results['Time'] = f"{elapsed_time:.6f}"

    return results


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python -m compute_statistics <filepath1> [filepath2] ...")
        sys.exit(1)

    filepaths = sys.argv[1:]

    # Compute statistics for all files
    all_results = []
    valid_filenames = []
    skipped_files = []

    for filepath in filepaths:
        try:
            all_results.append(compute_statistics(filepath))
            valid_filenames.append(os.path.basename(filepath))
        except (FileNotFoundError, ValueError) as e:
            print(f"Warning: Skipping file - {e}")
            skipped_files.append(filepath)

    if not all_results:
        print("Error: No valid files to process")
        sys.exit(1)

    # Build header and rows
    headers = [''] + valid_filenames
    metrics = ['Count', 'Mean', 'Median', 'Mode', 'Var', 'Std', 'Time']

    # Print and collect output
    output_lines = []
    header_line = '\t'.join(headers)
    output_lines.append(header_line)
    print(header_line)

    for metric in metrics:
        row = [metric] + [str(results[metric]) for results in all_results]
        row_line = '\t'.join(row)
        output_lines.append(row_line)
        print(row_line)

    # Write results to file
    output_filename = "StatisticsResults.txt"
    output_path = os.path.join(RESULTS_DIR, output_filename)

    try:
        os.makedirs(RESULTS_DIR, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(output_lines))
        print(f"\nResults saved to: {output_path}")
    except PermissionError:
        print(f"\nError: Permission denied writing to {output_path}")
        sys.exit(1)

    if skipped_files:
        print(f"\nSkipped {len(skipped_files)} file(s): {', '.join(skipped_files)}")


if __name__ == '__main__':
    main()
