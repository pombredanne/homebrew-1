#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_homebrew
----------------------------------

Tests for `homebrew` module.
"""

import subprocess

from homebrew import brew


def test_homebrew(monkeypatch, caplog):
    def mockreturn(brew):
        if 'uses' in brew:
            return 'emacs'
        if 'list' in brew:
            return 'boe blub'
        return None

    monkeypatch.setattr(subprocess, 'check_output', mockreturn)
    hb = brew()
    assert hb.packages_not_needed_by_other == {}
    assert hb.packages_needed_by_other == {
        u'blub': [u'emacs'],
        u'boe': [u'emacs']
    }
    assert 'boe' and 'blub' in hb.package_dependencies.get('emacs')
    hb.log_info()
    log_text = caplog.text()
    assert 'blub, boe' in log_text
    assert 'Package blub is needed by: emacs' in log_text
