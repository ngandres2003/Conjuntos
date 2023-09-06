from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from ventana import Conjuntos

ventana_principal = Tk()
ventana_principal.resizable(False,False) 
c = Conjuntos(ventana_principal)
ventana_principal.mainloop()