from homebrew import cache


def test_read(monkeypatch):
    assert cache.read(None) is None


def test_write(monkeypatch):
    assert cache.write(None, None) is None
