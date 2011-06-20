#!/usr/bin/env python

import sys, os, imp
from distutils.core import setup, Extension
sources = """cache.c cursor.c module.c row.c  util.c
connection.c microprotocols.c prepare_protocol.c shell.c statement.c sqlite3.c""".split()

if sys.platform == "win32":
    define_macros = [("MODULE_NAME", '\\"sqlite3\\"')]
else:
    define_macros = [("MODULE_NAME", '"sqlite3"')]

from distutils.sysconfig import get_python_lib
from distutils.command.install import install as _install


class install(_install):
    def run(self):
        try:
            path = imp.find_module("_sqlite3")[1]
        except ImportError:
            path = None

        _install.run(self)

        if path is None:
            return

        if path.startswith(get_python_lib()):
            return

        dirname, fn = os.path.split(path)
        disabled = os.path.join(dirname, "disabled-" + fn)
        print "mv %s %s" % (path, disabled)
        os.rename(path, disabled)


setup(name="_sqlite3",
      version="2.6.0-schmir1",
      description="make stdout unbuffered",
      ext_modules=[Extension("_sqlite3", sources, define_macros=define_macros)],
      cmdclass=dict(install=install))
