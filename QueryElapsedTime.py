#!/bin/python
#!/usr/bin/python
# export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/drives/c/oracle/instantclient_11_2/

import cx_Oracle
import sys
import os
os.environ["ORACLE_HOME"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1"
os.environ["LD_LIBRARY_PATH"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1/lib"

if len(sys.argv) != 3:
    print "Uso: "+sys.argv[0]+" database <sql_id>"
    print "Ex.: "+sys.argv[0]+" ora_database 7umy6juhz0000"
    exit(1)
	
database = sys.argv[1]
database = database.split('_')[1]
sql_id = sys.argv[2]
user = ' '
password = ' '
# host = 'vrt0980'
# Conexao do cx_Oracle. Necessario preencher as variaveis acima para conexao efetiva.
# connection = cx_Oracle.connect(user, password, "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host="+host+")(Port=1521))(CONNECT_DATA=(SID="+database+")))")
connection = cx_Oracle.connect(user, password, database)

cursor = connection.cursor()

cursor.execute("select AVG(round(elapsed_time_total/1000000, 2)) as MediaElapsed from DBA_HIST_SQLSTAT where sql_id = '"+ sql_id +"' and snap_id = (select max(snap_id) from DBA_HIST_SQLSTAT where sql_id = '"+ sql_id +"')")

mediaElapsed = cursor.fetchone()
mediaStr = str(mediaElapsed)
mediaStr = mediaStr.split('(')[1]
mediaStr = mediaStr.split(',')[0]
mediaFloat = float(mediaStr)

print round(mediaFloat, 4)
