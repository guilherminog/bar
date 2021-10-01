import tkinter as tk

app = tk.Tk()
app.title("Place() method")
app.geometry('200x200')
app.resizable(1, 1)

backFrame = tk.Frame(master=app, width=200, height=200, bg = 'yellow').pack()


button1 = tk.Button(master=backFrame, text='Login', bg='blue', fg='red', ).pack()
button2 = tk.Button(master=backFrame, text='teste', bg='blue', fg='green').pack()
#button3 = tk.Label(master=backFrame, text='Button 3', bg='red',fg='blue').pack()


app.mainloop()


"""
    Estudar formas de criar uma caixa de diálogo.
    para inserção de dados
# backFrame.pack()
# backFrame.propagate(0)


# from tkinter import ttk

# root_window = ttk() """