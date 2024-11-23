import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import util.validate as val


class IncluirProjeto:
    def __init__(self, janela_mestre, dateEntry=None):
        # Cria uma nova janela (pop-up)
        self.popup = tk.Toplevel(janela_mestre)
        self.popup.grab_set()

        # Constantes
        PADX = 10
        PADY = 10
        self.obrigatorios = []

        # Primeira linha - Título
        titulo = tk.Label(self.popup, text="Incluir Projeto", font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=0, column=0, columnspan=3, padx=PADX, pady=PADY)

        # Segunda linha - Receber o Nome do Projeto
        lb_nome = tk.Label(self.popup, text="Nome do Projeto", font='Helvetica 12 bold', fg='blue')
        lb_nome.grid(row=1, column=0, padx=PADX, pady=PADY)

        self.nome_var = tk.StringVar()
        self.et_nome = ttk.Entry(self.popup, textvariable=self.nome_var, font='Helvetica 16 bold',
                                 foreground='green', width=30)
        val.limitar_tamanho(self.et_nome, 50)
        self.obrigatorios.append([self.et_nome, lb_nome.cget('text')])
        self.et_nome.grid(row=1, column=1, columnspan=2, padx=PADX, pady=PADY)

        lb_datainicial = tk.Label(self.popup, text="Data inicial do projeto", font='Helvetica 12 bold', fg='blue')
        lb_datainicial.grid(row=2, column=0, padx=PADX, pady=PADY)

        self.entry_data_inicio = DateEntry(self.popup, font='Helvetica 12', width=12)
        self.entry_data_inicio.grid(row=2, column=1, padx=PADX, pady=PADY)

        lb_datafinal = tk.Label(self.popup, text="Data final do projeto", font='Helvetica 12 bold', fg='blue')
        lb_datafinal.grid(row=3, column=0, padx=PADX, pady=PADY)

        self.entry_data_fim = DateEntry(self.popup, font='Helvetica 12', width=12)
        self.entry_data_fim.grid(row=3, column=1, padx=PADX, pady=PADY)

        # Quarta linha - Botão para incluir uma nova função
        self.bt_salvar = tk.Button(self.popup, text="Incluir Novo Projeto", command=lambda: self.salvar(janela_mestre),
                                   font='Helvetica 12 bold',
                                   fg='white',
                                   bg='blue')
        self.bt_salvar.grid(row=4, column=0, columnspan=3, padx=PADX, pady=PADY)
        self.et_nome.focus()

    # Botão para confirmar a inclusão
    def salvar(self, janela_mestre):
        retorno = val.todos_campos_preenchidos(self.obrigatorios)
        if retorno[0]:
            nome = self.nome_var.get()
            data_inicial = self.entry_data_inicio.get_date()  # Obtém a data inicial
            data_final = self.entry_data_fim.get_date()  # Obtém a data final
            # Inserir os dados no banco de dados
            cmd = "INSERT INTO tb_projeto (nme_projeto, dta_ini_projeto, dta_fim_projeto) VALUES (%s, %s, %s)"
            id = janela_mestre.sql.insert(cmd, (nome, data_inicial, data_final))
            # Fechar a janela pop-up
            self.popup.destroy()
        else:
            messagebox.showerror("Erro: Campo(s) obrigatório(s)",
                                 "O(s) seguinte(s) campo(s) é/são obrigatório(s):\n" + retorno[1])