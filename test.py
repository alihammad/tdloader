import teradata

class DB():
	def __init__(self):
		udaExec = teradata.UdaExec (appName="test", version="1.0",logConsole=False)
		session = udaExec.connect(method="odbc", system="tddemo",username="dbc", password="dbc")
		self.session = session

	def fun1(self):
		# session.execute("create table financial.dummytable1(a varchar(10))")
		rows = self.session.execute("SHOW TABLE financial.dummytable1").fetchone()[0]
		for row in rows:
			print(row)
db = DB()
db.fun1()

print("---The End---")