import argparse
import sys
from reader import read_csv
from table import print_table
from reports_registry import REPORTS


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    data = read_csv(args.files)

    if args.report not in REPORTS:
        print("Unknown report:", args.report)
        sys.exit(1)

    report_func = REPORTS[args.report]
    headers, rows = report_func(data)
    print_table(headers=headers, rows=rows)


if __name__ == "__main__":
    main()
