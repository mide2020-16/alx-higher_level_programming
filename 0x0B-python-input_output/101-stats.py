import sys

def compute_metrics(lines):
    total_file_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    for line in lines:
        parts = line.split()
        if len(parts) >= 5:
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_file_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

    return total_file_size, status_counts

def print_statistics(total_file_size, status_counts):
    print("Total file size:", total_file_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
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
