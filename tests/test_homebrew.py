from homebrew import HomeBrew


def test_homebrew_init(monkeypatch):
    monkeypatch.setattr("subprocess.check_output", lambda popenargs: b"foo\nbar")

    hb = HomeBrew()

    assert len(hb.installed_packages) == 2
    assert hb.installed_packages[0] == "foo"
    assert hb.installed_packages[1] == "bar"
