import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry




class ExcluirProjeto:
  def __init__(self, janela_mestre, idt):
      # Cria uma nova janela (pop-up)
      self.popup = tk.Toplevel(janela_mestre)
      self.popup.grab_set()




      # Constantes
      PADX = 10
      PADY = 10




      # Variáveis
      linha = 0




      # Buscar dados que já estão na base
      cmd = "SELECT * FROM tb_projeto WHERE idt_projeto = %s"
      funcao = janela_mestre.sql.get_object(cmd, [idt])




      # Primeira linha - Título
      titulo = tk.Label(self.popup, text="Excluir Projeto", font='Helvetica 16 bold', fg='blue')
      titulo.grid(row=linha, column=0, columnspan=3, padx=PADX, pady=PADY)
      linha += 1




      # Segunda linha - Identificador da função
      lb_idt= tk.Label(self.popup, text="Identificador", font='Helvetica 12 bold', fg='blue')
      lb_idt.grid(row=linha, column=0, padx=PADX, pady=PADY)




      self.idt_var = tk.StringVar()
      self.idt_var.set(funcao['idt_projeto'])
      self.lb_dado_idt = tk.Label(self.popup, textvariable=self.idt_var, font='Helvetica 16 bold',
                               foreground='green')
      self.lb_dado_idt.grid(row=linha, column=1, columnspan=2, padx=PADX, pady=PADY, sticky="W")
      linha += 1




      # Terceira linha - Receber o Nome da Função
      lb_nome = tk.Label(self.popup, text="Nome da Projeto", font='Helvetica 12 bold', fg='blue')
      lb_nome.grid(row=linha, column=0, padx=PADX, pady=PADY)




      self.nome_var = tk.StringVar()
      self.nome_var.set(funcao['nme_projeto'])
      self.lb_dado_nome = tk.Label(self.popup, textvariable=self.nome_var, font='Helvetica 16 bold', foreground='green')
      self.lb_dado_nome.grid(row=linha, column=1, columnspan=2, padx=PADX, pady=PADY)
      linha += 1


      lb_datainicial = tk.Label(self.popup, text="Data inicial do projeto", font='Helvetica 12 bold', fg='blue')
      lb_datainicial.grid(row=3, column=0, padx=PADX, pady=PADY)




      self.valor_var = tk.StringVar()
      self.valor_var.set(funcao['dta_ini_projeto'])
      self.lb_dado_valor = tk.Label(self.popup, textvariable=self.valor_var, font='Helvetica 16 bold',
                                    foreground='green')
      self.lb_dado_valor.grid(row=linha, column=1, columnspan=2, padx=PADX, pady=PADY, sticky="W")
      linha += 1


      lb_datafinal = tk.Label(self.popup, text="Data final do projeto", font='Helvetica 12 bold', fg='blue')
      lb_datafinal.grid(row=4, column=0, padx=PADX, pady=PADY)




      self.valor_var = tk.StringVar()
      self.valor_var.set(funcao['dta_fim_projeto'])
      self.lb_dado_valor = tk.Label(self.popup, textvariable=self.valor_var, font='Helvetica 16 bold', foreground='green')
      self.lb_dado_valor.grid(row=linha, column=1, columnspan=2, padx=PADX, pady=PADY, sticky="W")
      linha += 1




      # Quinta Linha - Operação de Excluir
      self.bt_excluir = tk.Button(self.popup, text="Excluir o Projeto", command=lambda: self.excluir(janela_mestre),
                                 font='Helvetica 12 bold',
                                 fg='white',
                                 bg='blue')
      self.bt_excluir.grid(row=linha, column=0, columnspan=3, padx=PADX, pady=PADY)
      self.bt_excluir.focus()




  # Botão para confirmar a exclusão
  def excluir(self, janela_mestre):
      resposta = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir este projeto?")
      if resposta:
          idt = int(self.idt_var.get())
          # Excluir os dados no banco de dados
          cmd = "DELETE FROM tb_projeto WHERE idt_projeto = %s"
          num_reg = janela_mestre.sql.upd_del(cmd, [idt])
          # Fechar a janela pop-up
          self.popup.destroy()
