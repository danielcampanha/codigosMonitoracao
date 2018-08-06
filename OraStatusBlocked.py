#!/bin/python
#!/usr/bin/python
# export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/drives/c/oracle/instantclient_11_2/

import cx_Oracle
import sys
import os
os.environ["ORACLE_HOME"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1"
os.environ["LD_LIBRARY_PATH"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1/lib"

if len(sys.argv) != 2:
    print "Uso: "+sys.argv[0]+" <database>"
    print "Ex.: "+sys.argv[0]+" ora_database"
    exit(1)
	
database = sys.argv[1]
database = database.split('_')[1]
user = ' '
password = ' '
# host = ''
# Conexao do cx_Oracle. Necessario preencher as variaveis acima para conexao efetiva.
# connection = cx_Oracle.connect(user, password, "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host="+host+")(Port=1521))(CONNECT_DATA=(SID="+instancia+")))")
connection = cx_Oracle.connect(user, password, database)

cursor = connection.cursor()

cursor.execute("select count(*) from gv$session where  BLOCKING_SESSION_STATUS = 'VALID' and username like '%'")

blocked = cursor.fetchone()
blockedStr = str(blocked)
blockedStr = blockedStr.split('(')[1]
blockedStr = blockedStr.split(',')[0]
blockedInt = int(blockedStr)

print blockedInt

