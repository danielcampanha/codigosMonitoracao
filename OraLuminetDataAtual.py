#!/bin/python
# export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/drives/c/oracle/instantclient_11_2/

import cx_Oracle
import time
from datetime import datetime
import sys
import os
os.environ["ORACLE_HOME"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1"
os.environ["LD_LIBRARY_PATH"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1/lib"


	
database = "ppacte0a"
user = "snmp_bndes"
password = "SnMp230soid"
# host = "vrt0980"

# Conexao do cx_Oracle. Necessario preencher as variaveis acima para conexao efetiva.
# connection = cx_Oracle.connect(user, password, "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host="+host+")(Port=1521))(CONNECT_DATA=(SID="+database+")))")
connection = cx_Oracle.connect(user, password, database)

cursor = connection.cursor()
cursor.execute("SELECT MAX(PARTDATE) FROM UR_LUMINET_BACKLOG.ITX_RECORDINGS")
tuple = cursor.fetchone()

date = tuple[0]
# print date.year, date.month, date.day


now = datetime.now()
# print now.year, now.month, now.day


def compareData(date, now):
	if date.year == now.year and date.month == now.month and date.day == now.day:
		# print "Dia igual"
		print 0
	else:
		print 1

compareData(date, now)