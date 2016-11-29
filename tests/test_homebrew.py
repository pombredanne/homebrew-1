#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_homebrew
----------------------------------

Tests for `homebrew` module.
"""
import pytest

from homebrew import homebrew


@pytest.mark.skip
def test_homebrew(monkeypatch, caplog):
    """TODO: Write tests"""
    homebrew.HomeBrew()
