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

####################################	
user = ['JCR', 'RELEASE', 'COMMUNITY', 'CUSTOMIZATION', 'FEEDBACK', 'LIKEMINDS']
password = ['vAse5t', 'vAse5t', 'vAse5t', 'vAse5t', 'vAse5t', 'vAse5t']	
host = ' '
database = 'PRDInfra'
queries = ['select distinct(1) from WCM_LIBRARIES', 'select distinct(1) from PAGE_INST', 'select distinct(1) from PAGE_INST', 'select distinct(1) from PAGE_INST', 'select distinct(1) from ENTITIES', 'select distinct(1) from lps_user_data']
results = []
# Conexao do cx_Oracle. Necessario preencher as variaveis acima para conexao efetiva.
###################################

########### -- Funcao conexao com diferentes schemas e queries -- #################
def testarQuery(user, password, database, queries):
	connection = cx_Oracle.connect(user, password, database)
	cursor = connection.cursor()
	cursor.execute(queries)
	result = cursor.fetchone()
	result = str(result)
	result = result.split('(')[1]
	result = result.split(',')[0]
	result = int(result)
	return result
##################################################################################	
	

for i in range(len(user)):
	testarQuery(user[i], password[i], database, queries[i])
	results.append(testarQuery(user[i], password[i], database, queries[i]))

ultimo_array = results	
# print ultimo_array	
############### -- Checar se todos schemas estao funcionando -- ############		
schemas_corretos = True

for i in range(len(ultimo_array)):
	# print user[i]
	# print password[i]
	# print queries[i]
	if ultimo_array[i] != 1:
		schemas_corretos = False
		break
# print schemas_corretos		
if schemas_corretos == False:
	print user[i] 		
else:
	print '0'	
###########################################################################	
results = [] 

