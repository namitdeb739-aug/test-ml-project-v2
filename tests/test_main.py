import pytest

from test_ml_v2.main import main


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert "Hello from test-ml-v2!" in captured.out
