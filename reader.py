import csv


def read_csv(file_list):
    rows = []
    for file_name in file_list:

        with open(file_name, newline="", encoding="utf-8") as csvfile:
            rows.extend(csv.DictReader(csvfile))

    return rows


