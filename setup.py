#!/usr/bin/env python

from distutils.core import setup, Extension
sources = """cache.c cursor.c module.c row.c  util.c
connection.c microprotocols.c prepare_protocol.c shell.c statement.c sqlite3.c""".split()

define_macros = [("MODULE_NAME", '\\"sqlite3\\"')]
setup(name = "_sqlite3",
      description = "make stdout unbuffered",
      ext_modules = [Extension("_sqlite3", sources, define_macros=define_macros)])
