"""Main script to compute statistics from a file."""

import sys
import time
import os

from src.stats import count, mean, median, mode, variance, standard_deviation
from src.utils import read_data, save_results, print_results, print_skipped_files

RESULTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'results', 'p1')
METRICS = ['Count', 'Mean', 'Median', 'Mode', 'Var', 'Std', 'Time']


def compute_statistics(filepath):
    """Compute statistics for a single file and return results."""
    start_time = time.time()
    data = read_data(filepath, converter=float)

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


def process_files(filepaths):
    """Process multiple files and return results with valid filenames."""
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

    return all_results, valid_filenames, skipped_files


def format_results(all_results, valid_filenames):
    """Format results as tab-separated lines."""
    output_lines = []
    header_line = '\t'.join([''] + valid_filenames)
    output_lines.append(header_line)

    for metric in METRICS:
        row = [metric] + [str(results[metric]) for results in all_results]
        output_lines.append('\t'.join(row))

    return output_lines


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python -m compute_statistics <filepath1> [filepath2] ...")
        sys.exit(1)

    filepaths = sys.argv[1:]
    all_results, valid_filenames, skipped_files = process_files(filepaths)

    if not all_results:
        print("Error: No valid files to process")
        sys.exit(1)

    output_lines = format_results(all_results, valid_filenames)

    print_results(output_lines)

    output_path = os.path.join(RESULTS_DIR, "StatisticsResults.txt")
    save_results(output_lines, output_path)

    print_skipped_files(skipped_files)


if __name__ == '__main__':
    main()
