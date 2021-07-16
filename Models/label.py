import tkinter as tk

class Label(tk.Label):
    def __init__(self, master, text, command):
        super().__init__(master=master,text=text, font=("Courier", 25),fg='blue')