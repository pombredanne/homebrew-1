import asyncio
import subprocess
from collections import defaultdict

from .logger import log


def get_empty_values_from_dict(dct, empty_values=True):
    for key, value in dct.items():
        if empty_values and not value:
            yield (key, value)
        elif not empty_values and value:
            yield (key, value)


class HomeBrew:
    _uses = {}

    def __init__(self):
        self.installed = self.get_installed()

    def run(self):
        self.get_uses()
        self.log_info()

    def get_installed(self):
        result = subprocess.check_output(["brew", "list"])
        installed = result.split()
        return [r.decode("utf-8") for r in installed]

    def get_uses(self):
        tasks = [self._get_uses_for_package(package) for package in self.installed]
        asyncio.run(asyncio.wait(tasks))

    async def _get_uses_for_package(self, package):
        uses = await asyncio.create_subprocess_exec(
            *["brew", "uses", "--installed", package],
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT
        )
        stdout, _ = await uses.communicate()
        self._uses[package] = stdout.decode("utf-8").split()

    def log_info(self):
        log(
            self.installed,
            self.packages_not_needed_by_other,
            self.packages_needed_by_other,
            self.package_dependencies,
        )

    @property
    def packages_not_needed_by_other(self):
        return dict(get_empty_values_from_dict(self._uses))

    @property
    def packages_needed_by_other(self):
        return dict(get_empty_values_from_dict(self._uses, empty_values=False))

    @property
    def package_dependencies(self):
        dependencies = defaultdict(list)
        for package, needed_by in self.packages_needed_by_other.items():
            for needed in needed_by:
                dependencies[needed].append(package)
        return {needed: sorted(packages) for needed, packages in dependencies.items()}
