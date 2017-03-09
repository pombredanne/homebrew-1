#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from homebrew import homebrew


@pytest.mark.skip
def test_homebrew(monkeypatch):
    """TODO: Write tests"""
    homebrew.HomeBrew()


@pytest.mark.parametrize("dct, empty_values, expected", [
    ({'a': None}, True, {'a': None}),
    ({'a': None}, False, {}),
    ({'a': 'Foo'}, True, {}),
    ({'a': 'Foo'}, False, {'a': 'Foo'}),
    ({'a': None, 'b': 'Foo', 'c': 'Bar'}, True, {'a': None}),
    ({'a': None, 'b': 'Foo', 'c': 'Bar'}, False, {'b': 'Foo', 'c': 'Bar'}),
])
def test_get_empty_values_from_dict(dct, empty_values, expected):
    assert dict(homebrew.get_empty_values_from_dict(
        dct, empty_values)) == expected
