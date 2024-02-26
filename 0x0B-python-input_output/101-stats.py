#!/usr/bin/python3
"""
Log Parsing
"""
import sys

def compute_metrics(lines):
    """
    Compute metrics such as total file size and counts of different status codes.

    Args:
        lines (list): A list of strings representing lines of input data.

    Returns:
        tuple: A tuple containing the total file size (int) and a dictionary
               with counts of different status codes.
    """
    total_file_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    status_count = {}

    for line in lines:
        parts = line.split()
        if len(parts) >= 5:
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_file_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
                status_count.keys = status_code
                status_count.values = status_counts[status_code]

    return total_file_size, status_count

def print_statistics(total_file_size, status_counts):
    """
    Print statistics such as total file size and counts of different status codes.

    Args:
        total_file_size (int): The total size of all files processed.
        status_counts (dict): A dictionary containing counts of different status codes.

    Returns:
        None
    """
    print("Total file size:", total_file_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    """
    Main function to read input, compute metrics, and print statistics.

    Reads input line by line from standard input, computes metrics such as
    total file size and counts of different status codes, and prints statistics
    every 10 lines or when interrupted by CTRL + C.

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
                total_file_size, status_counts = compute_metrics(lines)
                print_statistics(total_file_size, status_counts)
                lines = []
    except KeyboardInterrupt:
        total_file_size, status_counts = compute_metrics(lines)
        print_statistics(total_file_size, status_counts)

if __name__ == "__main__":
    main()
