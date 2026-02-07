"""Script to convert numbers from decimal to binary and hexadecimal."""

import sys
import time
import os

from src.converters import decimal_to_binary, decimal_to_hexadecimal

RESULTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'results', 'p2')


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
                data.append(int(float(line)))
            except ValueError:
                skipped_lines.append((line_num, line))

    if skipped_lines:
        for line_num, line in skipped_lines:
            print(f"Warning: Skipped invalid data at line {line_num} in {filepath}: '{line}'")

    if not data:
        raise ValueError(f"File is empty or contains no valid data: {filepath}")

    return data


def convert_numbers(filepath):
    """Convert all numbers in a file to binary and hexadecimal."""
    start_time = time.time()
    data = read_data(filepath)

    results = []
    for number in data:
        results.append({
            'Decimal': number,
            'Binary': decimal_to_binary(number),
            'Hexadecimal': decimal_to_hexadecimal(number),
        })

    elapsed_time = time.time() - start_time

    return results, elapsed_time


def process_files(filepaths):
    """Process multiple files and return results."""
    all_results = []
    skipped_files = []

    for filepath in filepaths:
        try:
            results, elapsed_time = convert_numbers(filepath)
            all_results.append({
                'filename': os.path.basename(filepath),
                'results': results,
                'time': elapsed_time,
            })
        except (FileNotFoundError, ValueError) as e:
            print(f"Warning: Skipping file - {e}")
            skipped_files.append(filepath)

    return all_results, skipped_files


def format_results(all_results):
    """Format results as tab-separated lines."""
    output_lines = []
    output_lines.append("Decimal\tBinary\tHexadecimal")

    for file_data in all_results:
        output_lines.append(f"\n# {file_data['filename']}")
        for row in file_data['results']:
            output_lines.append(f"{row['Decimal']}\t{row['Binary']}\t{row['Hexadecimal']}")
        output_lines.append(f"# Time: {file_data['time']:.6f} seconds")

    return output_lines


def save_results(output_lines):
    """Save results to file."""
    output_path = os.path.join(RESULTS_DIR, "ConversionResults.txt")

    try:
        os.makedirs(RESULTS_DIR, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(output_lines))
        print(f"\nResults saved to: {output_path}")
    except PermissionError:
        print(f"\nError: Permission denied writing to {output_path}")
        sys.exit(1)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python -m src.convert_numbers <filepath1> [filepath2] ...")
        sys.exit(1)

    filepaths = sys.argv[1:]
    all_results, skipped_files = process_files(filepaths)

    if not all_results:
        print("Error: No valid files to process")
        sys.exit(1)

    output_lines = format_results(all_results)

    for line in output_lines:
        print(line)

    save_results(output_lines)

    if skipped_files:
        print(f"\nSkipped {len(skipped_files)} file(s): {', '.join(skipped_files)}")


if __name__ == '__main__':
    main()
