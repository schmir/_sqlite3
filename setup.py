#!/usr/bin/env python

import sys, os, imp, time

if "setuptools" in sys.modules:
    from setuptools import setup, Extension
    from setuptools.command.install import install as _install
else:
    from distutils.core import setup, Extension
    from distutils.command.install import install as _install

sources = """cache.c cursor.c module.c row.c  util.c
connection.c microprotocols.c prepare_protocol.c shell.c statement.c sqlite3.c""".split()

if sys.platform == "win32":
    define_macros = [("MODULE_NAME", '\\"sqlite3\\"')]
else:
    define_macros = [("MODULE_NAME", '"sqlite3"')]

from distutils.sysconfig import get_python_lib


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
        try:
            os.rename(path, disabled)
        except Exception, err:
            header = "------------ %s ------------" % err

            print """
%s
Could not rename %s to %s
Please rename the file manually!
%s
""" % (header, path, disabled, "-"*len(header))
            time.sleep(8)


setup(name="_sqlite3",
      version="2.6.0-schmir2",
      url="https://github.com/schmir/_sqlite3",
      ext_modules=[Extension("_sqlite3", sources, define_macros=define_macros)],
      cmdclass=dict(install=install))
