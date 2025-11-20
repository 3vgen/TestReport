from reports.performance import generate_performance_report


def test_build_performance_report():
    data = [
        {"position": "Dev", "performance": "80"},
        {"position": "QA", "performance": "90"},
        {"position": "Dev", "performance": "100"}
    ]
    headers, rows = generate_performance_report(data)

    assert headers == ["position", "avg_performance"]
    # QA: 90, Dev: (80+100)/2 = 90, все строки performance должны быть 90
    positions = [row[0] for row in rows]
    assert "Dev" in positions and "QA" in positions
    for row in rows:
        assert row[1] == 90
