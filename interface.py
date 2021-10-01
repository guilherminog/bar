""" Essa inserção de dados será feita pela UI para sqlite
    não esquecer de estudar as bibliotecas de dados para
    guardar e acessar, tudo isso pelo 'tkinter'.
    Data de inicio 30/09/2021"""



from tkinter import *
import tkinter as tk
from insert_data import inf_init, inf_contato

nome, idade = inf_init()
tel, email, endereco = inf_contato()


def _inf_contato():
    print ("Nome:%s" % nome.get(inf_init(nome)))
    print ("Idade:%s" % idade.get(inf_init(idade)))
    print ("Email:%s" % email.get(inf_init(email)))
    print ("Telefone:%s" % tel.get(inf_init(tel)))
    print ("Edereço:%s" % endereco.get(inf_init(endereco)))



app = tk.Tk()
app.title("PROGRAMAS BAR")
app.geometry('500x400')
app.resizable(1, 1)

backFrame = tk.Frame(master=app, width=200, height=200, bg = 'yellow').pack()


button1 = tk.Button(master=backFrame, text='', bg='blue', fg='red', ).pack()
button1.place(x=100, y=80)
button2 = tk.Button(master=backFrame, text='teste', bg='blue', fg='green').pack()
button2.place(x=100, y=60)
#button3 = tk.Label(master=backFrame, text='Button 3', bg='red',fg='blue').pack()


app.mainloop()


"""
    Estudar formas de criar uma caixa de diálogo.
    para inserção de dados
# backFrame.pack()
# backFrame.propagate(0)


# from tkinter import ttk

# root_window = ttk() """