
from util.db import SQL


cpf = input('Digite o CPF: ')
senha = input('Digite o Senha: ')


cmd = '''
SELECT nme_colaborador, sts_colaborador FROM tb_colaborador WHERE cpf_colaborador = %s AND pwd_colaborador = SHA(%s)
'''


sql = SQL(esquema='bd_planejamento')


colaborador = sql.get_object(cmd, [cpf, senha])


if colaborador is None:
   print('Falha no Login')
else:
   print('Bem vindo ao sistema')
   print(colaborador['nme_colaborador'])
   print('Função:', ('Administrador' if colaborador['sts_colaborador'] == 'A' else 'Usuário Comum'))

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


   def insert(self, comando, params=()):
       cs = self.cnx.cursor()
       cs.execute(comando, params)
       self.cnx.commit()
       idt = cs.lastrowid
       cs.close()
       return idt


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




def inserir_projetos(sql):
   projetos = [
       ['Controle de Acesso de Visitantes', '2024-10-05'],
       ['Controle de Atendimento de Monitoria', '2024-10-06'],
       ['Gestão de Cursos', '2024-10-07']
   ]


   cmd_insert_projeto = '''
   INSERT INTO tb_projeto(nme_projeto, dta_ini_projeto)
   VALUES (%s, %s)
   '''


   for projeto in projetos:
       idt = sql.insert(cmd_insert_projeto, projeto)
       print(f'Criado projeto: {idt} - {projeto[0]}')




def listar_projetos(sql):
   cmd_select_projetos = '''
   SELECT idt_projeto, nme_projeto, dta_ini_projeto, dta_fim_projeto
   FROM tb_projeto
   '''


   projetos_cadastrados = sql.get_list(cmd_select_projetos)


   pt = PrettyTable(['ID Projeto', 'Nome do Projeto', 'Data Início', 'Data Fim'])


   for projeto in projetos_cadastrados:
       pt.add_row([
           projeto['idt_projeto'],
           projeto['nme_projeto'],
           projeto['dta_ini_projeto'],
           projeto['dta_fim_projeto'] if projeto['dta_fim_projeto'] else 'Em andamento'
       ])


   print(pt)
