from Models.Beast import Beast
from Models.Chat import Chat
from Models.Chien import Chien
from Models.Oiseau import Oiseau
from datetime import date
import tkinter as tk


# chat1:Chat= Chat("Kebab",6.0,53.2,"M",date(1985,12,10),date(2020,12,10),"Bonne composition",True,"court")
# chat2:Chat= Chat("Machin",12.0,75,"F",date(1992,12,10),date(2020,2,10),"Bonne composition",True,"long")

# chat1.crier()
# print(chat1)
# print(chat2)
# print(chat2)


# fond=tk.PhotoImage(file='pic/fond.png')

app = tk.Tk()
app.title("Annimalerie")
# app.iconbitmap('pic/images.ico')
app.iconphoto(False, tk.PhotoImage(file='pic/logo.png'))
app.geometry('800x400')
label = tk.Label(app, text="Enregistrer un annimal !",bg='#49A', font=("Courier", 25, "bold")).grid(row=1, columnspan=6)
label = tk.Label(app, text="",bg='#49A', font=("Courier", 10, "bold")).grid(row=2, columnspan=3)

app['bg'] = '#49A'

catbutton= tk.Button(app,text="Chat", font=("Courier", 12)).grid(row=3, column=1)
dogbutton= tk.Button(app,text="Chien", font=("Courier", 12)).grid(row=3, column=2)
birdbutton= tk.Button(app,text="Oiseau", font=("Courier", 12)).grid(row=3, column=3)

app.mainloop()
