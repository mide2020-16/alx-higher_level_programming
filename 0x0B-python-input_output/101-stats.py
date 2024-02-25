#!/usr/bin/python3
"""
File Information
"""
import sys
from collections import defaultdict


def compute_metrics(lines):
    """
    Compute metrics such as total file size and counts

    Args:
        lines (list): A list of strings representing lines of input data.

    Returns:
        tuple: A tuple containing the total file size (int) and a dictionary
               with counts of different status codes (defaultdict).
    """
    total_file_size = 0
    status_counts = defaultdict(int)

    for line in lines:
        parts = line.split()
        if len(parts) >= 9:
            status_code = parts[8]
            file_size = int(parts[-1])
            total_file_size += file_size
            status_counts[status_code] += 1

    return total_file_size, status_counts


def print_stats(total_file_size, status_count):
    """
    Print statistics such as total file size and counts

    Args:
        total_file_size (int): The total size of all files processed.
        status_count (defaultdict): A dictionary containing counts of different
                                    status codes.

    Returns:
        None
    """
    print(f"Total file size: {total_file_size}")

    for status_code in sorted(status_count.keys()):
        print(f"{status_code}: {status_count[status_code]}")


def main():
    """
    Main function to read input, compute metrics, and print statistics.

    Reads input line by line from standard input, computes metrics
    file size and counts of different status codes, and prints statistics every
    10 lines or when interrupted by CTRL + C.

    Args:
        None

    Returns:
        None
    """
    lines = []

    try:
        for line in sys.stdin:
            lines.append(line.strip())
            if len(lines) == 10:
                total_file_size, status_count = compute_metrics(lines)
                print_stats(total_file_size, status_count)
                lines = []
    except KeyboardInterrupt:
        total_file_size, status_count = compute_metrics(lines)
        print_stats(total_file_size, status_count)


if __name__ == "__main__":
    main()
