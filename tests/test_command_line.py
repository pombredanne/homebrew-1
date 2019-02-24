import pytest

from homebrew import __version__
from homebrew.command_line import parse_args


def test_parse_args(capsys):
    with pytest.raises(SystemExit):
        parse_args(["--version"])

    captured = capsys.readouterr()
    assert captured.out.strip() == __version__

    with pytest.raises(SystemExit):
        parse_args(["--help"])

    captured = capsys.readouterr()
    assert "Get homebrew info" in captured.out
