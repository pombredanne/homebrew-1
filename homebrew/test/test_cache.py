from homebrew.caching import uc


def test_uses_cache():
    assert uc.read_installed() == []
    assert uc.read_uses() == []
    assert uc.write_installed(None) is None
    assert uc.write_uses(None) is None
