from homebrew import HomeBrew


def fake_get_uses(self):
    for package in self._installed:
        self._uses[package] = ["baz"]


def test_homebrew_init(monkeypatch):
    monkeypatch.setattr(HomeBrew, "_get_uses", fake_get_uses)
    monkeypatch.setattr("subprocess.check_output", lambda popenargs: b"foo\nbar")

    hb = HomeBrew()

    assert len(hb.installed_packages) == 2
    assert hb.installed_packages[0] == "foo"
    assert hb.installed_packages[1] == "bar"

    assert len(hb._uses) == 2
    assert hb._uses["foo"] == ["baz"]
    assert hb._uses["bar"] == ["baz"]
