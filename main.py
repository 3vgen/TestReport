import argparse
from reader import read_csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()


if __name__ == "__main__":
    main()
