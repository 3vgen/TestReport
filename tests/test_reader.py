import pytest
from reader import read_csv
import os


def test_read_files(tmp_path):
    file1 = tmp_path / "file1.csv"
    file1.write_text("position,performance\nDev,80\nQA,90")

    file2 = tmp_path / "file2.csv"
    file2.write_text("position,performance\nDev,85\nQA,95")

    rows = read_csv([file1, file2])

    assert len(rows) == 4
    assert rows[0]["position"] == "Dev"
    assert rows[3]["performance"] == "95"
