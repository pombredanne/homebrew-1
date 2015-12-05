# -*- coding: utf-8 -*-
from __future__ import absolute_import

import subprocess

from .logger import log


class HomeBrew(object):

    def __init__(self):
        self.installed = self.get_installed()
        self.uses = self.get_uses()

    def get_installed(self):
        result = subprocess.check_output(['brew', 'list'])
        installed = result.split()
        return installed

    def get_uses(self):
        uses = {}
        for package in self.installed:
            uses[package] = subprocess.check_output(
                ['brew', 'uses', '--installed', package]
            ).split()
        return uses

    @property
    def packages_not_needed_by_other(self):
        return dict(
            (key, value) for key, value in self.uses.items() if not value
        )

    @property
    def packages_needed_by_other(self):
        return dict(
            (key, value) for key, value in self.uses.items() if value
        )

    @property
    def package_dependencies(self):
        dependencies = {}
        for package, needed_by in self.packages_needed_by_other.items():
            for needed in needed_by:
                if not dependencies.get(needed):
                    dependencies[needed] = [package]
                else:
                    dependencies[needed].append(package)
        return dependencies

    def log_info(self):
        log(self.installed, self.packages_not_needed_by_other,
            self.packages_needed_by_other, self.package_dependencies)
