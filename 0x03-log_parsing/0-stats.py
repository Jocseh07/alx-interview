#!/usr/bin/python3
"""
Log parsing
"""


import sys


def print_stats(total_size, status_codes):
    """
    This function prints the total file size and the count of each status code.

    Args:
    - total_size: The total file size.
    - status_codes: A dictionary containing the count of each status code.

    Returns:
    - None
    """
    print("File size:", total_size)
    for code in status_codes.keys():
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """
    This function parses a log entry line and extracts the
    IP address, status code, and file size.

    Args:
    - line: A string representing a log entry.

    Returns:
    - ip_address: The IP address extracted from the log entry.
    - status_code: The status code extracted from the log entry.
    - file_size: The file size extracted from the log entry.
    """
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = parts[-2]
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (IndexError, ValueError, TypeError):
        return None, None, None


def main():
    """
    This script parses log files and calculates statistics
    based on the log entries.

    Functions:
    - main(): The main function that reads log entries from
    standard input, parses them, and calculates statistics.
    """

    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0,
                    401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line)
            if ip_address is None:
                continue

            total_size += file_size
            status_codes[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    finally:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
