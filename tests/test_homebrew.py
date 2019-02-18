from homebrew import HomeBrew


def test_homebrew(monkeypatch):
    def _fake_get_uses(self):
        return {"foo": ["bar"], "bar": []}

    monkeypatch.setattr(HomeBrew, "_get_uses", _fake_get_uses)
    monkeypatch.setattr("subprocess.check_output", lambda popenargs: b"foo\nbar")

    hb = HomeBrew()

    assert len(hb.installed_packages) == 2
    assert hb.installed_packages[0] == "foo"
    assert hb.installed_packages[1] == "bar"

    assert len(hb._uses) == 2
    assert hb._uses["foo"] == ["bar"]
    assert hb._uses["bar"] == []

    assert hb.packages_not_needed_by_other == {"bar": []}
    assert hb.packages_needed_by_other == {"foo": ["bar"]}
    assert hb.package_dependencies == {'bar': ['foo']}
    assert hb.info is None
