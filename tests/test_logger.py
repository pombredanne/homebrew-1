from homebrew import logger


def test_log_title(caplog):
    logger.log_title("Installed packages:")
    caplog_lines = [record.msg for record in caplog.records]
    assert len(caplog_lines[0]) == len(caplog_lines[1])


def test_log_blank_line(caplog):
    logger.log_blank_line()
    caplog_lines = [record.msg for record in caplog.records]
    assert caplog_lines[0] == ""


def test_log(caplog, expected_log_output):
    logger.log(
        installed=["foo", "bar"],
        packages_not_needed_by_other=["bar"],
        packages_needed_by_other={"foo": ["bar"]},
        package_dependencies={"bar": ["foo"]},
    )
    caplog_lines = [record.msg for record in caplog.records]
    assert caplog_lines == expected_log_output
