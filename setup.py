#!/usr/bin/env python

import sys
from distutils.core import setup, Extension
sources = """cache.c cursor.c module.c row.c  util.c
connection.c microprotocols.c prepare_protocol.c shell.c statement.c sqlite3.c""".split()

if sys.platform == "win32":
    define_macros = [("MODULE_NAME", '\\"sqlite3\\"')]
else:
    define_macros = [("MODULE_NAME", '"sqlite3"')]

setup(name="_sqlite3",
      version="2.6.0-schmir1",
      description="make stdout unbuffered",
      ext_modules=[Extension("_sqlite3", sources, define_macros=define_macros)])
