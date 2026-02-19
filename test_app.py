def test_high_value(capsys):
    # This test will crash before it even runs because app.py has syntax errors
    check_status(15)
    captured = capsys.readouterr()
    assert "High value" in captured.out

def test_low_value(capsys):
    check_status(5)
    captured = capsys.readouterr()
    assert "Low value" in captured.out
