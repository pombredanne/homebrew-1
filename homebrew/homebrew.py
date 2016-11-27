# -*- coding: utf-8 -*-
import asyncio
import subprocess

from .logger import log


class HomeBrew(object):

    def __init__(self):
        self.installed = self.get_installed()
        self.get_uses()

    def get_installed(self):
        result = subprocess.check_output(['brew', 'list'])
        installed = result.split()
        return [r.decode('utf-8') for r in installed]

    def get_uses(self):
        self.uses = {}
        loop = asyncio.get_event_loop()
        tasks = [asyncio.ensure_future(self.get_uses_for_package(package))
                 for package in self.installed]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()

    async def get_uses_for_package(self, package):
        uses = await asyncio.create_subprocess_exec(
            *['brew', 'uses', '--installed', package],
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT
        )
        stdout, _ = await uses.communicate()
        self.uses[package] = stdout.decode('utf-8').split()

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
