import json
import os
from functools import wraps

CACHE_DIR = os.path.join(
    os.path.expanduser("~/Library/Caches"), __loader__.name.split(".")[0]
)


class UsesCache:
    _installed_path = os.path.join(CACHE_DIR, "installed.json")
    _uses_path = os.path.join(CACHE_DIR, "uses.json")

    def read_installed(self):
        try:
            with open(self._installed_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def write_installed(self, installed):
        with open(self._installed_path, "w") as file:
            json.dump(installed, file)

    def read_uses(self):
        with open(self._uses_path, "r") as file:
            return json.load(file)

    def write_uses(self, uses):
        with open(self._uses_path, "w") as file:
            json.dump(uses, file)


uc = UsesCache()


def uses_cache(method):
    @wraps(method)
    def _wrapper(self):
        if sorted(self._installed) == sorted(uc.read_installed()):
            return uc.read_uses()

        uc.write_installed(self._installed)
        uses = method(self)
        uc.write_uses(uses)

        return uses

    return _wrapper
