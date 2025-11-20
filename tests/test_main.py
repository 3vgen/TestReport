import sys
import pytest


# мок для метода чтения файлов
def fake_read_files(file_list):
    return [
        {"position": "Dev", "performance": "80"},
        {"position": "QA", "performance": "90"},
        {"position": "Dev", "performance": "100"}
    ]


def test_main_performance(monkeypatch, capsys):
    # Подмена аргументов
    monkeypatch.setattr(sys, 'argv', ['main.py', '--files', 'fake.csv', '--report', 'performance'])

    # Подмена метода на мок
    import main
    monkeypatch.setattr(main, "read_csv", fake_read_files)

    main.main()

    captured = capsys.readouterr()
    assert "Dev" in captured.out
    assert "QA" in captured.out
    assert "avg_performance" in captured.out


def test_main_unknown_report(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['main.py', '--files', 'fake.csv', '--report', 'unknown'])

    import main
    monkeypatch.setattr(main, "read_csv", fake_read_files)

    with pytest.raises(SystemExit) as exc_info:
        main.main()

    assert exc_info.value.code == 1

    captured = capsys.readouterr()
    assert "Unknown report" in captured.out
