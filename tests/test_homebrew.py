#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_homebrew
----------------------------------

Tests for `homebrew` module.
"""

from homebrew import brew


def test_homebrew(monkeypatch):
    def mockreturn(brew):
        brew.installed = []
        brew.uses = {}

    monkeypatch.setattr(brew, '__init__', mockreturn)
    hb = brew()
    assert hb.packages_not_needed_by_other == {}
    assert hb.packages_needed_by_other == {}
    assert hb.package_dependencies == {}
