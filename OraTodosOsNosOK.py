#!/bin/python
#!/usr/bin/python
# export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/drives/c/oracle/instantclient_11_2/

import cx_Oracle
import sys
import os
os.environ["ORACLE_HOME"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1"
os.environ["LD_LIBRARY_PATH"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1/lib"

# if len(sys.argv) != 2:
    # print "Uso: "+sys.argv[0]+" <database>"
    # print "Ex.: "+sys.argv[0]+" dbndes0a"
    # exit(1)

user = ' '
password = ' '
host = [' ', ' ', ' ', ' ' ] 
database = [' ', ' ', ' ', ' ']
query = "select * from gv$session"
conexao_sucesso = False
todas_as_conexoes = []

def testarconexao (user, password, host, database, query):
		try:
			connection = cx_Oracle.connect(user, password, "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host="+host+")(Port=1521))(CONNECT_DATA=(SID="+database+")))")
			cursor = connection.cursor()
			cursor.execute(query)
			conectou = True
		except:
			#print "Deu erro na Query"
			conectou = False

		return conectou

for i in range(len(database)):
	todas_as_conexoes.append(testarconexao (user, password, host[i], database[i], query))


for i in range (len(todas_as_conexoes)):
	if todas_as_conexoes[i] == True:
		conexao_sucesso = True
		break;
	else:
		conexao_sucesso = False


if conexao_sucesso == True:
	print '0 - OK'
else:
	print '1 - ERRO'
	
print todas_as_conexoes	
	
