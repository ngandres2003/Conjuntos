from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from ventanaOperaciones import Operaciones

class Conjuntos:
    universo = {}
    subConjuntos = []
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Conjuntos")
        self.ventana.geometry("400x400")
        self.ventana.configure(background='grey')
        self.colocarTitulo()
        self.colocarBotones()
        
        
        

    def colocarTitulo(self):
                
        self.titulo = Label(self.ventana, text="Conjuntos", font=("Tahoma 20 bold"),bg='grey',fg="white")
        self.titulo.pack(pady=10)


    
    def crearUniverso(self):
        resultado = simpledialog.askstring("Universo", "Ingrese datos separado por coma ")
        resultado = resultado.replace(" ","")
        Conjuntos.universo =set(resultado.split(","))
        self.boton1.config(state=DISABLED)
        messagebox.showinfo("Operación", "Universo Creado: " + str(Conjuntos.universo))
    
    def crearSubConjunto(self):
        if len(Conjuntos.universo) > 0:

            valido = True
            subconjunto = simpledialog.askstring("SubConjunto", "Ingrese datos separado por coma ")
            subconjunto = subconjunto.replace(" ","")     
            subconjunto = set(subconjunto.split(","))
            for element in subconjunto:
                if element not in Conjuntos.universo:
                    valido = False
            
            if valido == True:
                Conjuntos.subConjuntos.append(subconjunto)
                messagebox.showinfo("Operación", "Subconjunto creado")
            else:
                messagebox.showwarning("Operación", "Cada elemento del subconjunto debe pertenecer al universo")


            
        else:
             messagebox.showwarning("Operación", "Debes crear primer el universal")

        
    
    def crearAutomatico(self):
        Conjuntos.universo = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        Conjuntos.subConjuntos = [
            {1,3,5,7,9},
            {2,4,6,8,10},
            {3,6,9,12},
            {4,8,12,16,20},
            {5,10,15,20},
            {2,5,8,1,3,19,20}
        ]
        
        messagebox.showinfo("Alert","Conjuntos creado automaticamente. \nUniverso: 1-20")
        self.boton1.config(state=DISABLED)
        self.boton2.config(state=DISABLED)
        self.boton3.config(state=DISABLED)
    
    def operaciones(self):
        if len(Conjuntos.universo) > 0 and len(Conjuntos.subConjuntos) > 0:
            self.ventana.withdraw()
            ventana_operaciones = Toplevel(self.ventana)
            ventana_operaciones.resizable(False,False)
            app_ventana_operaciones = Operaciones(ventana_operaciones, self.ventana,Conjuntos)
        else:
            messagebox.showwarning("Alert","Debes crear el universal y subconjuntos")


    


    def limpiar(self):
        Conjuntos.universo.clear()
        Conjuntos.subConjuntos.clear()
        self.boton1.config(state=ACTIVE)
        self.boton2.config(state=ACTIVE)
        self.boton3.config(state=ACTIVE)
        messagebox.showinfo("Alert","Se ha eliminado todos los conjuntos")
    



    def colocarBotones(self):
        #Definimos Botones
        self.boton1 = Button(self.ventana, text="Crear Universal",font="Tahoma 10 bold ",width=20,height=2, command=self.crearUniverso)
        self.boton2 = Button(self.ventana, text="Crear Subconjunto",font="Tahoma 10 bold ",width=20,height=2, command=self.crearSubConjunto)
        self.boton3 = Button(self.ventana, text="Crear Automaticamente",font="Tahoma 10 bold ",width=20,height=2, command=self.crearAutomatico)
        self.boton4 = Button(self.ventana, text="Operaciones",font="Tahoma 10 bold ",width=20,height=2, command=self.operaciones)
        self.boton5 = Button(self.ventana, text="Limpiar",font="Tahoma 10 bold ",width=20,height=2,command=self.limpiar)
            
        #Colocamos espacio entre botonnes y los colocamos
        self.boton1.pack(pady=10)
        self.boton2.pack(pady=10)
        self.boton3.pack(pady=10)
        self.boton4.pack(pady=10)
        self.boton5.pack(pady=10)
    




