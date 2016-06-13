#!/usr/bin/env python

"""This is the example module.

Tokenizer:
TODO: Input
         - [Config file path] [ [[Directory path] [File extensions as filter]] | [File/s path] ]
Usage
tokenizer.py [t|d] [Config file path] [f|d] [ [[Directory path] [File extensions as filter]] | [File/s path] ]


This module does stuff.
"""

__author__ = "Ali Hammad Baig"
__copyright__ = "Copyright 2016, Me Myself"
__credits__ = ["Ali Hammad Baig"]
__license__ = ""
__version__ = "1.0.1"
__maintainer__ = "Ali Hammad Baig"
__email__ = "ali.hammadbaig@gmail.com"
__status__ = "Development"
__prog__ = "tdloader"

import logging
import os
import teradata
import copy
from datetime import datetime

class DB():
	def __init__(self):
		# logging.basicConfig(filename='tdloader.log',
		# 				filemode='a',
		# 				format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
		# 				datefmt='%H:%M:%S',
		# 				level=logging.DEBUG)

		# os.system('config.py')
		# from config import username, password, tdip
		# username = str(username)
		# password = str(password)
		# tdip = str(tdip)
		# print("TDIP: {0}, Username: {1}, Passwrod: {2}".format(tdip, username, password))

		#udaExec = teradata.UdaExec (appName="HelloWorld", version="1.0", logConsole=False)
		#session = udaExec.connect(method="odbc", system=tdip,username=username, password=password)

		udaExec = teradata.UdaExec (appConfigFile="tdloader.ini")
		logger = logging.getLogger(__name__)
		session = udaExec.connect("${dataSourceName}")
		self.session = session
		self.log = logger

	def lookup_value(self):
		query = "SELECT * FROM dbc.ChildrenV WHERE parent='gcfr_main'"
		# self.cur.execute(query, (user_name,))
		# self.result = self.cur.fetchone()
		# self.result = self.session.execute(query)
		# print("Result: " + str(self.result.fetchone))
		#self.result = self.cur.fetchone

		for row in self.session.execute(query):
			print(row)

	def get_db_hierarchy(self, parent_db):
		"""blah blah
		blah blah
		"""
		rows = self.session.execute(file="${hierarchyQuery}")
		return rows

	def create_dirs(self, rows):
		for row in rows:
			os.makedirs(row.route, exist_ok=True)
		

	def get_db_obj_show_stmts(self, db):
		shw_stmt= self.session.execute(file="${shwstmtQuery}", params=(db, )).fetchone()[0]
		return shw_stmt

	def save_obj_ddl_in_file(self, db, filesystem_path, rs):
		for row in rs:
			file_path = filesystem_path+'/'+rs['filename']
			show_stmt = rs['showstmt']

			self.log.info("file_path: {0},  show_stmt: {1}".format(file_path, show_stmt))
			# ddl = self.session.execute(show_stmt)
			# file = open(file_path, 'w+')
			# file.write(ddl)
			# file.close()



# constructor
db = DB()
rs_db_hierarchy = tuple(db.get_db_hierarchy('gcfr_main'))
db.create_dirs(rs_db_hierarchy)
# rs_db_hierarchy gives databasename and route
# rs_db_obj_show_stmt gives filename and show statement
for row in rs_db_hierarchy:
	db_name = row.databasename
	filesystem_path = row.route
	print("dbname: {0}, file path: {1}".format(db_name, filesystem_path))
	rs_db_obj_show_stmt = db.get_db_obj_show_stmts(db_name)
	print(rs_db_obj_show_stmt)
	# db.save_obj_ddl_in_file(db_name, filesystem_path, rs_db_obj_show_stmt)