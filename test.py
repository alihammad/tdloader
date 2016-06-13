import teradata

class DB():
	def __init__(self):
		udaExec = teradata.UdaExec (appName="test", version="1.0",logConsole=False)
		session = udaExec.connect(method="odbc", system="tddemo",username="dbc", password="dbc")
		self.session = session

	def fun1(self):
		# session.execute("create table financial.dummytable1(a varchar(10))")
		cur = self.session.cursor()
		cur.arraysize = 5000
		# rows = cur.execute("SHOW TABLE financial.dummytable1")
		# for row in rows:
		# 	print(row)

		# cur.close()

		# for row in self.session.execute("SHOW TABLE financial.dummytable1"):
		# 	print(row)

		cur.execute("show table financial.dummytable1")
		# count = cur.fetchall()[0][0]
		# print("Count: {0} ".format(count))

		stmt = cur.fetchall()
		print(len(stmt))
			
		cur.close()

db = DB()
db.fun1()

print("---The End---")