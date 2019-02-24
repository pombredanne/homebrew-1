import pytest

from homebrew import HomeBrew


class MockTask:
    def __init__(self, package, uses):
        self.package = package
        self.uses = uses

    def result(self):
        return self.package, self.uses


def _fake_asyncio_run(coro):
    return {MockTask("foo", ["bar"]), MockTask("bar", [])}, None


@pytest.fixture(autouse=True)
def mock_async(monkeypatch):
    monkeypatch.setattr(HomeBrew, "_get_uses_for_package", lambda self_, package: [])
    monkeypatch.setattr("asyncio.wait", lambda tasks: None)
    monkeypatch.setattr("asyncio.run", _fake_asyncio_run)


@pytest.fixture(autouse=True)
def mock_check_output(monkeypatch):
    monkeypatch.setattr("subprocess.check_output", lambda popenargs: b"foo\nbar")


@pytest.fixture
def expected_log_output():
    return [
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
