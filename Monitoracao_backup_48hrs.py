#!/bin/python
#!/usr/bin/python
# export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/drives/c/oracle/instantclient_11_2/

import cx_Oracle
import sys
import os
import time
from datetime import datetime
os.environ["ORACLE_HOME"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1"
os.environ["LD_LIBRARY_PATH"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1/lib"

if len(sys.argv) != 4:
    print "Variaveis: "+sys.argv[0]+" <database> <user> <password>"
    print "Ex. de uso: "+sys.argv[0]+" ora_database1 admin admin123"
    exit(1)
	
database = sys.argv[1]
database = database.split('_')[1]
user = sys.argv[2]
password = sys.argv[3]
# Conexao do cx_Oracle. Necessario preencher as variaveis acima para conexao efetiva.
#connection = cx_Oracle.connect(user, password, "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host="+host+")(Port=1521))(CONNECT_DATA=(SID="+database+")))")
connection = cx_Oracle.connect(user, password, database)

cursor = connection.cursor()

cursor.execute("""
select to_char(completion_time,'dd-mm-yyyy hh24:mi:ss') from V$BACKUP_SET_DETAILS
where backup_type like 'I' and incremental_level = '1'
order by completion_time desc
fetch first 1 row only """)

ultimaVez = cursor.fetchone()
ultimaVez = str(ultimaVez)
ultimaVez = ultimaVez.split("'")[1]
ultimaVez = ultimaVez.split("'")[0]
ultimaVez = time.strptime(ultimaVez, "%d-%m-%Y %H:%M:%S")

s_now = str(datetime.now().strftime('%Y.%m.%d.%H.%M.%S.%f'))
d_now = time.strptime(s_now, "%Y.%m.%d.%H.%M.%S.%f") 
backupAlert = time.mktime(d_now) - time.mktime(ultimaVez)

if (backupAlert/3600 > 48):
	print '1 - passou do tempo'
else:
	print '0 - ok'


