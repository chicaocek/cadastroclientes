import tkinter as tk
import sqlite3
import pandas as pd
from tkinter import messagebox

# #Criando o Banco de Dados:
#
# conexao = sqlite3.connect('clientes.db')
#
# # Criando o cursor:
# c = conexao.cursor()
#
# # Criando a tabela:
#
# # c.execute("""CREATE TABLE  clientes (
# #     nome text,
# #     sobrenome text,
# #     email text,
# #     telefone text
# #     )""")
#
# #Commit as mudanças:
# conexao.commit()
#
# #Fechar o banco de dados:
# conexao.close()


#Criando Janela:

janela = tk.Tk()

janela.title('Cadastro de Clientes')
janela. geometry("330x350+0+0")
janela.configure(background='#8af2f2')
janela.iconbitmap(default="cadastro.ico")
janela.resizable(0, 0)
# Função cadastrar

def cadastrar_cliente():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO clientes VALUES (:nome,:sobrenome,:email,:telefone)",
              {
                  'nome': entry_nome.get(),
                  'sobrenome': entry_sobrenome.get(),
                  'email': entry_email.get(),
                  'telefone': entry_telefone.get()
              })

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_nome.delete(0, "end")
    entry_sobrenome.delete(0, "end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")

    # Mensagens de confirmação

    messagebox.showinfo('Nota', 'Cadastrado no banco de dados')

# Função exportar

def exporta_clientes():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    # print(clientes_cadastrados)
    clientes_cadastrados=pd.DataFrame(clientes_cadastrados, columns=['nome', 'sobrenome','email', 'telefone', 'Id_banco'])
    clientes_cadastrados.to_excel('clientes.xlsx')

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # Mensagens de confirmação
    messagebox.showinfo('Nota', 'Exportado para o Excel')

#Rótulos Entradas:
label_nome = tk.Label(janela, text='Nome', bg='#ffffb3', font="Times 10 bold")
label_nome.grid(row=0,column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome', bg='#ffffb3', font="Times 10 bold")
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail', bg='#ffffb3', font="Times 10 bold")
label_email.grid(row=2, column=0 , padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone', bg='#ffffb3', font="Times 10 bold")
label_telefone.grid(row=3, column=0, padx=10, pady=10)

#Caixas Entradas:
entry_nome = tk.Entry(janela , width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width =35)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width =35)
entry_email.grid(row=2, column=1 , padx=10, pady=10)

entry_telefone = tk.Entry(janela, width =35)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Cliente', bg='yellow', font="Times 12 bold", command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0, columnspan=2,  padx=10, pady=10, ipadx=87)

# Botão de Exportar

botao_exportar = tk.Button(text='Exportar para Excel', bg='yellow', font="Times 12 bold", command=exporta_clientes)
botao_exportar.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

# Botão Sair

botao_sair = tk.Button(text='Sair', bg='yellow', fg='red', font="Times 17 bold", command=janela.destroy)
botao_sair.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=30)

janela.mainloop()


