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
    with open(filepath, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            try:
                data.append(float(line))
            except ValueError as exc:
                raise ValueError(
                    f"Invalid data at line {line_num} in {filepath}: '{line}'"
                ) from exc

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
    filenames = [os.path.basename(fp) for fp in filepaths]

    # Compute statistics for all files
    all_results = []
    for filepath in filepaths:
        try:
            all_results.append(compute_statistics(filepath))
        except FileNotFoundError as e:
            print(f"Error: {e}")
            sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

    # Build header and rows
    headers = [''] + filenames
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


if __name__ == '__main__':
    main()
