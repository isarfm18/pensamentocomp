import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import util.validate as val
from tkcalendar import DateEntry






class AlterarProjeto:
  def __init__(self, janela_mestre, idt):
      # Cria uma nova janela (pop-up)
      self.popup = tk.Toplevel(janela_mestre)
      self.popup.grab_set()




      # Constantes
      PADX = 10
      PADY = 10




      # Variáveis
      self.obrigatorios = []
      linha = 0




      # Buscar dados que já estão na base
      cmd = "SELECT * FROM tb_projeto WHERE idt_projeto = %s"
      funcao = janela_mestre.sql.get_object(cmd, [idt])




      # Primeira linha - Título
      titulo = tk.Label(self.popup, text="Alterar Projeto", font='Helvetica 16 bold', fg='blue')
      titulo.grid(row=linha, column=0, columnspan=3, padx=PADX, pady=PADY)
      linha += 1




      # Segunda linha - Mostrar o identificador da função (readonly)
      lb_idt= tk.Label(self.popup, text="Identificador", font='Helvetica 12 bold', fg='blue')
      lb_idt.grid(row=linha, column=0, padx=PADX, pady=PADY)




      self.idt_var = tk.StringVar()
      self.idt_var.set(funcao['idt_projeto'])
      self.et_idt = ttk.Entry(self.popup, textvariable=self.idt_var, font='Helvetica 16 bold',
                               foreground='green', width=5, state="readonly")
      self.et_idt.grid(row=linha, column=1, columnspan=2, padx=PADX, pady=PADY, sticky="W")
      linha += 1




      # Terceira linha - Receber o Nome da Função
      lb_nome = tk.Label(self.popup, text="Nome do Projeto", font='Helvetica 12 bold', fg='blue')
      lb_nome.grid(row=linha, column=0, padx=PADX, pady=PADY)




      self.nome_var = tk.StringVar()
      self.nome_var.set(funcao['nme_projeto'])
      self.et_nome = ttk.Entry(self.popup, textvariable=self.nome_var, font='Helvetica 16 bold',
                               foreground='green', width=30)
      val.limitar_tamanho(self.et_nome, 50)
      self.obrigatorios.append([self.et_nome, lb_nome.cget('text')])
      self.et_nome.grid(row=linha, column=1, columnspan=2, padx=PADX, pady=PADY)
      linha += 1


      lb_datainicial = tk.Label(self.popup, text="Data inicial do projeto", font='Helvetica 12 bold', fg='blue')
      lb_datainicial.grid(row=4, column=0, padx=PADX, pady=PADY)


      self.entry_data_inicio = DateEntry(self.popup, font='Helvetica 12', width=12)
      self.entry_data_inicio.grid(row=4, column=1, padx=PADX, pady=PADY)


      lb_datafinal = tk.Label(self.popup, text="Data final do projeto", font='Helvetica 12 bold', fg='blue')
      lb_datafinal.grid(row=5, column=0, padx=PADX, pady=PADY)


      self.entry_data_fim = DateEntry(self.popup, font='Helvetica 12', width=12)
      self.entry_data_fim.grid(row=5, column=1, padx=PADX, pady=PADY)




      vcmd = (self.popup.register(val.validate_float), '%P')  # %P representa o novo valor
      self.valor_var = tk.StringVar()
      self.valor_var.set(funcao['dta_ini_projeto'])
      self.et_valor = ttk.Entry(self.popup, textvariable=self.valor_var, font='Helvetica 16 bold', foreground='green',
                                width=10, validate='key', validatecommand=vcmd)
      self.obrigatorios.append([self.et_valor, lb_valor.cget('text')])
      self.et_valor.grid(row=linha, column=1, columnspan=2, padx=PADX, pady=PADY, sticky="W")
      linha += 1




      # Quinta linha - Botação para salvar alterações
      self.bt_alterar = tk.Button(self.popup, text="Alterar o Projeto", command=lambda: self.alterar(janela_mestre),
                                 font='Helvetica 12 bold',
                                 fg='white',
                                 bg='blue')
      self.bt_alterar.grid(row=linha, column=0, columnspan=3, padx=PADX, pady=PADY)
      self.et_nome.focus()




  # Botão para confirmar a alteração
  def alterar(self, janela_mestre):
      retorno = val.todos_campos_preenchidos(self.obrigatorios)
      if retorno[0]:
          idt = int(self.idt_var.get())
          nome = self.nome_var.get()
          valor = float(self.valor_var.get())
          # Alterar os dados no banco de dados
          cmd = "UPDATE tb_projeto SET nme_projeto = %s, dta_ini_projeto  = %s, dta_fim_projeto = % WHERE idt_projeto = %s"
          num_reg = janela_mestre.sql.upd_del(cmd, (nome, dta_ini_projeto, dta_fim_projeto, idt))
          # Fechar a janela pop-up
          self.popup.destroy()
      else:
          messagebox.showerror("Erro:A Campo(s) obrigatório(s)", "O(s) seguinte(s) campo(s) é/são obrigatório(s):\n" + retorno[1])
