========
Usage
========

To use homebrew in a project::

    >>> from homebrew import brew
    >>> b = brew()
    >>> b.packages_not_needed_by_other
    {'node': [], 'python': [], 'tree': [], 'gettext': [], 'emacs': [], 'gnupg': [], 'git-flow': [], 'python3': []}
    >>> b.packages_needed_by_other
    {'sqlite': ['python', 'python3'], 'openssl': ['node', 'python', 'python3'], 'xz': ['emacs', 'gettext', 'python3'], 'readline': ['python', 'python3', 'sqlite'], 'gdbm': ['python', 'python3'], 'pkg-config': ['emacs', 'node', 'python', 'python3']}
    >>> b.package_dependencies
    {'node': ['openssl', 'pkg-config'], 'sqlite': ['readline'], 'python': ['sqlite', 'openssl', 'readline', 'gdbm', 'pkg-config'], 'gettext': ['xz'], 'emacs': ['xz', 'pkg-config'], 'python3': ['sqlite', 'openssl', 'xz', 'readline', 'gdbm', 'pkg-config']}
    >>> b.log_info()
    Installed packages:
    -------------------
    emacs, gdbm, gettext, git-flow, gnupg, node, openssl, pkg-config, python, python3, readline, sqlite, tree, xz

    No package depends on these packages:
    -------------------------------------
    emacs, gettext, git-flow, gnupg, node, python, python3, tree

    These packages are needed by other packages:
    --------------------------------------------
    Package gdbm is needed by: python, python3
    Package openssl is needed by: node, python, python3
    Package pkg-config is needed by: emacs, node, python, python3
    Package readline is needed by: python, python3, sqlite
    Package sqlite is needed by: python, python3
    Package xz is needed by: emacs, gettext, python3

    These packages depend on other packages:
    ----------------------------------------
    Package emacs depends on: xz, pkg-config
    Package gettext depends on: xz
    Package node depends on: openssl, pkg-config
    Package python depends on: sqlite, openssl, readline, gdbm, pkg-config
    Package python3 depends on: sqlite, openssl, xz, readline, gdbm, pkg-config
    Package sqlite depends on: readline
