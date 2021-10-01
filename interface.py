import tkinter as tk

app = tk.Tk()
app.geometry('500x400')
app.resizable(0, 0)

backFrame = tk.Frame(master=app, width=500, height=400, bg = 'yellow').pack()
button1 = tk.Button(master=backFrame, text='Button 1', bg='blue', fg='red').pack()

button2 = tk.Button(master=backFrame, text='Button 2', bg='blue', fg='green').pack()
button3 = tk.Label(master=backFrame, text='Button 3', bg='red',fg='blue').pack()


app.mainloop()





# from tkinter import ttk

# root_window = ttk()