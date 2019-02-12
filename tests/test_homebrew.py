from homebrew import HomeBrew


def test_homebrew_init(monkeypatch):
    monkeypatch.setattr("subprocess.check_output", lambda popenargs: b"foo\nbar")

    hb = HomeBrew()

    assert len(hb.installed) == 2
    assert hb.installed[0] == "foo"
    assert hb.installed[1] == "bar"
