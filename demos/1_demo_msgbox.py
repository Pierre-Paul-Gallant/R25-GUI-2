# https://docs.python.org/3/library/tkinter.messagebox.html
# https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/


import tkinter
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog


#messagebox.askquestion(title="En-tête", message="Texte ici !")

messagebox.showinfo("1","infos")
messagebox.showwarning("2","avertissement")
messagebox.showerror("3","erreur")

messagebox.askquestion("4","question")

messagebox.askokcancel("5","cancel?")
messagebox.askyesno("6","oui / non ?")
messagebox.askretrycancel("7", "ré-essayer ?")

messagebox.askyesnocancel("8","true/false/None")



messagebox.Message(title="9",message="ret",type='abortretryignore').show()