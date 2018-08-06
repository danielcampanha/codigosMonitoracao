#!/bin/python
#!/usr/bin/python
# export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/drives/c/oracle/instantclient_11_2/

import cx_Oracle
import sys
import os
os.environ["ORACLE_HOME"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1"
os.environ["LD_LIBRARY_PATH"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1/lib"

####################################	
user = ''
password = ''
sql_id = '7b9q2g1pyvj2j'
#host = ''
database = 'PINFRA0A'

# Conexao do cx_Oracle. Necessario preencher as variaveis acima para conexao efetiva.
########### -- Funcao conexao com diferentes schemas e queries -- #################

#connection = cx_Oracle.connect(user, password, "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=vrt0980)(Port=1521))(CONNECT_DATA=(SID="+database+")))")
connection = cx_Oracle.connect(user, password, database)
cursor = connection.cursor()
cursor.execute("select AVG(round(elapsed_time_total/1000000, 2)) as MediaElapsed from DBA_HIST_SQLSTAT where sql_id = '"+sql_id+"' and snap_id = (select max(snap_id) from DBA_HIST_SQLSTAT where sql_id = '"+sql_id+"')")
result = cursor.fetchone()
result = str(result)
result = result.split('(')[1]
result = result.split(',')[0]
result = float(result)
print result
##################################################################################	
	


