from homebrew import HomeBrew


def test_homebrew(caplog):
    hb = HomeBrew()

    assert len(hb.installed_packages) == 2
    assert hb.installed_packages[0] == "foo"
    assert hb.installed_packages[1] == "bar"

    assert len(hb._uses) == 2
    assert hb._uses["foo"] == ["bar"]
    assert hb._uses["bar"] == []

    assert hb.packages_not_needed_by_other == {"bar": []}
    assert hb.packages_needed_by_other == {"foo": ["bar"]}
    assert hb.package_dependencies == {"bar": ["foo"]}

    hb.info
    caplog_lines = [record.msg for record in caplog.records]
    assert caplog_lines == [
        "Installed packages:",
        "-------------------",
        "bar, foo",
        "",
        "No package depends on these packages:",
        "-------------------------------------",
        "bar",
        "",
        "These packages are needed by other packages:",
        "--------------------------------------------",
        "Package foo is needed by: bar",
        "",
        "These packages depend on other packages:",
        "----------------------------------------",
        "Package bar depends on: foo",
        "",
    ]
