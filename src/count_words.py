"""Script to count words in files."""

import time
import os

from src.word_counter import get_word_frequencies
from src.utils import run_main

RESULTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'results', 'p3')


def read_text(filepath):
    """Read all text from a file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()

    return text


def count_file_words(filepath):
    """Count word frequencies in a file and return results."""
    start_time = time.time()
    text = read_text(filepath)

    frequencies = get_word_frequencies(text)

    elapsed_time = time.time() - start_time

    return frequencies, elapsed_time


def process_files(filepaths):
    """Process multiple files and return results."""
    all_results = []
    skipped_files = []

    for filepath in filepaths:
        try:
            frequencies, elapsed_time = count_file_words(filepath)
            all_results.append({
                'filename': os.path.basename(filepath),
                'frequencies': frequencies,
                'time': elapsed_time,
            })
        except FileNotFoundError as e:
            print(f"Warning: Skipping file - {e}")
            skipped_files.append(filepath)

    return all_results, skipped_files


def format_results(all_results):
    """Format results as tab-separated lines."""
    output_lines = []

    for file_data in all_results:
        output_lines.append(f"# {file_data['filename']}")
        output_lines.append("Word\tCount")

        frequencies = file_data['frequencies']
        total = 0

        for word, count in frequencies.items():
            output_lines.append(f"{word}\t{count}")
            total += count

        output_lines.append(f"Total\t{total}")
        output_lines.append(f"Time\t{file_data['time']:.6f}")
        output_lines.append("")

    return output_lines


def main():
    """Main entry point."""
    output_path = os.path.join(RESULTS_DIR, "WordCountResults.txt")
    run_main(
        usage="Usage: python -m src.count_words <filepath1> [filepath2] ...",
        process_fn=process_files,
        format_fn=format_results,
        output_path=output_path,
    )


if __name__ == '__main__':
    main()
