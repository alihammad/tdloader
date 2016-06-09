#!/usr/bin/env python

import logging
import os
from datetime import datetime

import teradata

#####
## Tokenizer:
## TODO: Input
##          - [Config file path] [ [[Directory path] [File extensions as filter]] | [File/s path] ]
## Usage
## tokenizer.py [t|d] [Config file path] [f|d] [ [[Directory path] [File extensions as filter]] | [File/s path] ]
#####

__author__ = "Ali Hammad Baig"
__copyright__ = "Copyright 2016, Me Myself"
__credits__ = ["Ali Hammad Baig"]
__license__ = ""
__version__ = "1.0.1"
__maintainer__ = "Ali Hammad Baig"
__email__ = "ali.hammadbaig@gmail.com"
__status__ = "Development"
__prog__ = "tdloader"

class DB():
	def __init__(self):
		logging.basicConfig(filename='tdloader.log',
						filemode='a',
						format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
						datefmt='%H:%M:%S',
						level=logging.DEBUG)
		
		os.system('config.py')
		from config import username, password, tdip
		username = str(username)
		password = str(password)
		tdip = str(tdip)
		print("TDIP: {0}, Username: {1}, Passwrod: {2}".format(tdip, username, password))

		udaExec = teradata.UdaExec (appName="HelloWorld", version="1.0", logConsole=False)
		session = udaExec.connect(method="odbc", system=tdip,username=username, password=password)
		self.session = session

	def lookup_value(self):
		query = "SELECT * FROM dbc.ChildrenV WHERE parent='gcfr_main'"
		# self.cur.execute(query, (user_name,))
		# self.result = self.cur.fetchone()
		# self.result = self.session.execute(query)
		# print("Result: " + str(self.result.fetchone))
		#self.result = self.cur.fetchone

		for row in self.session.execute(query):
			print(row)

		
db = DB()
db.lookup_value()
# print(value.result)