#!/bin/python
#!/usr/bin/python
# export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/drives/c/oracle/instantclient_11_2/

import os
import sys
os.environ["ORACLE_HOME"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1"
os.environ["LD_LIBRARY_PATH"] = "/opt/oracle/app/oracle/product/12.1.0/dbhome_1/lib"

if len(sys.argv) != 2:
    print "Uso: "+sys.argv[0]+" <database>"
    print "Ex.: "+sys.argv[0]+" ora_dbndes0a"
    exit(1)

database = sys.argv[1]
database = database.split('_')[1]
# print database

array_sql_id = [['PRDinfra', '407kdbc5x0000', 'Tempo da Query do Cadastro Funcionario', 'Tempo de CPU da Query do Cadastro Funcionario', 'Tempo de IO da Query do Cadastro Funcionario',
				'OraQueryElapsedTime', 'OraQueryCPUTime', 'OraQueryIOWait', 'Tempo da Query do Cadastro Funcionario acima do esperado',
				'Tempo do CPU da Query do Cadastro Funcionario acima do esperado', 'Tempo do IO da Query do Cadastro Funcionario acima do esperado', "10", "11", "12"],
				
				['DSVinfra', 'gzzdbdrg20000', 'Tempo da Query do Insert', 'Tempo de CPU da Query do Insert', 'Tempo de IO da Query do Insert', 'OraQueryCPUTime', 'OraQueryElapsedTime',"OraQueryIOWait", "Tempo da Query do Insert acima do esperado", "Tempo do CPU da Query do Insert acima do esperado", "Tempo do IO da Query do Insert acima do esperado", "15", "16", "17"],
				
				["PRDinfra", "407kdbc5x0000", "Tempo da Query do Portal Externo", "Tempo de CPU da Query do Portal Externo", "Tempo de IO da Query do Portal Externo", "OraQueryElapsedTime", "OraQueryCPUTime", "OraQueryIOWait", "Tempo da Query do Portal Externo acima do esperado", "Tempo do CPU da Query do Portal Externo acima do esperado", "Tempo do IO da Query do Portal Externo acima do esperado", "20", "21", "22"]]
# array_sql_id = []
				
print """{
	data:["""
for i in range(len(array_sql_id)):
	if array_sql_id[i][0] != database:
		continue
	else:		
		
		# for i in range(len(array_sql_id)-1):
		print 	" 	{" 	
		print	" 	{#DATABASE}: "  + '"' + array_sql_id[i][0] + '",' '\n' , 
		print	" 	{#SQL_ID}: " + '"' +array_sql_id[i][1]+ '",' '\n' , 
		print	" 	{#ELAPSED_ITEM_NAME}: " + '"' +array_sql_id[i][2]+ '",' '\n',
		print	" 	{#CPU_ITEM_NAME}: " + '"' +array_sql_id[i][3]+ '",' '\n', 
		print	" 	{#IO_ITEM_NAME}: " + '"' +array_sql_id[i][4]+ '",' '\n',
		print	" 	{#ELAPSED_ITEM_KEY} : "  + '"' +array_sql_id[i][5]+ '",''\n', 
		print	" 	{#CPU_ITEM_KEY}: " + '"' +array_sql_id[i][6]+ '",' '\n', 
		print	" 	{#IO_ITEM_KEY}: "  + '"' +array_sql_id[i][7]+ '",' '\n', 
		print	" 	{#ELAPSED_TRIGGER_NAME}: " + '"' +array_sql_id[i][8]+ '",' '\n',
		print	" 	{#CPU_TRIGGER_NAME}: " + '"' +array_sql_id[i][9]+ '",' '\n',
		print	" 	{#IO_TRIGGER_NAME}: " + '"' +array_sql_id[i][10]+ '",' '\n',
		print	" 	{#ELAPSED_TRIGGER_THRESHOLD}: " + '"' +array_sql_id[i][11]+ '",' '\n',
		print	" 	{#CPU_TRIGGER_THRESHOLD}: " + '"' +array_sql_id[i][12]+ '",' '\n',
		print	" 	{#IO_TRIGGER_THRESHOLD}: " + '"' +array_sql_id[i][13]+ '"},''\n'
	
print """ 	    ]	
}"""
	
	
	
	
