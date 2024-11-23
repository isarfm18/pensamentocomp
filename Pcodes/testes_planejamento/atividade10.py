import mysql.connector
from prettytable import PrettyTable


class SQL:
   def __init__(self, servidor='localhost', usr='root', pwd='ceub123456', esquema='bd_planejamento'):
       self.cnx = mysql.connector.connect(
           host=servidor,
           user=usr,
           password=pwd,
           database=esquema
       )


   def __del__(self):
       self.cnx.close()


   def get_list(self, comando, params=()):
       cs = self.cnx.cursor()
       cs.execute(comando, params)
       md = cs.description
       catalog = []
       for reg in cs:
           dic = {col[0]: valor for col, valor in zip(md, reg)}
           catalog.append(dic)
       cs.close()
       return catalog


sql = SQL()


cmd_select_projetos = '''
SELECT nme_projeto, dta_ini_projeto
FROM tb_projeto
'''


projetos_cadastrados = sql.get_list(cmd_select_projetos)


tabela_projetos = PrettyTable()
tabela_projetos.field_names = ['Nome do Projeto', 'Data de Início']


for projeto in projetos_cadastrados:
   tabela_projetos.add_row([projeto['nme_projeto'], projeto['dta_ini_projeto']])


print(tabela_projetos)
