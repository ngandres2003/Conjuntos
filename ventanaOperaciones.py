import string
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox


'''Controla todas las operaciones y eventos de la primera ventana'''
class Operaciones:
    def __init__(self, ventana, ventana_principal,Conjuntos):
        self.ventana = ventana
        self.Conjuntos = Conjuntos
        self.ventana_principal = ventana_principal
        self.ventana.title("Operaciones de Conjuntos")
        self.ventana.geometry("400x450")
        self.ventana.configure(background='grey')
        self.colocar_titulo()
        self.colocar_botones()
       
    




    def colocar_titulo(self):
        self.titulo = Label(self.ventana, text="Operaciones de Conjuntos", font=("Tahoma 20 bold"),bg='grey',fg="white")
        self.titulo.pack(pady=10)

    def colocar_botones(self):      
        self.boton_interseccion = Button(self.ventana, text="Intersección",font="Tahoma 10 bold ", command=self.menu_interseccion,width=20, height=2)
        self.boton_union = Button(self.ventana, text="Unión",font="Tahoma 10 bold ", command=self.menu_union,width=20, height=2)
        self.boton_diferencia =Button(self.ventana, text="Diferencia", font="Tahoma 10 bold ",command=self.menu_diferencia,width=20, height=2)
        self.boton_complemento =Button(self.ventana, text="Complemento",font="Tahoma 10 bold ", command=self.menu_complemento,width=20, height=2)
        self.boton_automatico =Button(self.ventana, text="Automatico",font="Tahoma 10 bold ",width=20, height=2, command= self.operaciones_automaticas)
        self.boton_volver = Button(self.ventana, text="Volver a la Principal",font="Tahoma 10 bold ", command=self.volver,width=20, height=2)
        
        self.boton_interseccion.pack(pady=10)
        self.boton_union.pack(pady=10)
        self.boton_diferencia.pack(pady=10)
        self.boton_complemento.pack(pady=10)
        self.boton_automatico.pack(pady=10)
        self.boton_volver.pack(pady=10)
        
        
    
    def menu(self, titulo, conjuntos):
        mensaje = titulo +"\n\n"
        for i, conjunto in enumerate(conjuntos, start=1):
            mensaje += f"{i}: {conjunto}\n"
        entrada = simpledialog.askstring(titulo, mensaje)
        if entrada:
            indices = entrada.split(",")
            indices = [int(index.strip()) for index in indices if index.strip().isdigit()]

            if len(indices) == 2 and all(1 <= index <= len(conjuntos) for index in indices):
                seleccion = [conjuntos[index - 1] for index in indices]
                return seleccion
            else:
                messagebox.showwarning("Advertencia", "Debe seleccionar exactamente 2 conjuntos válidos.")
                return None
        else:
            return None
        
    def menu_2(self, titulo, conjuntos):
        mensaje = titulo + "\n\n"
        for i, conjunto in enumerate(conjuntos, start=1):
            mensaje += f"{i}: {conjunto}\n"

        entrada = simpledialog.askstring(titulo, mensaje)
        if entrada:
            index = int(entrada.strip())
            if 1 <= index <= len(conjuntos):
                seleccion = conjuntos[index - 1]
                return seleccion
            else:
                messagebox.showwarning("Advertencia", "Debe seleccionar un conjunto válido.")
                return None
        else:
            return None
        
    def menu_interseccion(self):
        if len(self.Conjuntos.subConjuntos) >=2:
            seleccion = self.menu("Seleccionar 2 conjuntos separados por coma: ", self.Conjuntos.subConjuntos)
            seleccion = self.interseccion(seleccion[0],seleccion[1])
            messagebox.showinfo("Operacion","Interseccion: " + str(seleccion))
        else:
            messagebox.showwarning("Alert","Debes tener como minimo 2 subconjuntos")
    
    def menu_union(self):
        if len(self.Conjuntos.subConjuntos) >=2:
            seleccion = self.menu("Seleccionar 2 conjuntos separados por coma: ", self.Conjuntos.subConjuntos)
            seleccion = self.union(seleccion[0],seleccion[1])
            messagebox.showinfo("Operacion","Union: " + str(seleccion))
        else:
            messagebox.showwarning("Alert","Debes tener como minimo 2 subconjuntos")
    
    def menu_diferencia(self):
        if len(self.Conjuntos.subConjuntos) >=2:
            seleccion = self.menu("Seleccionar 2 conjuntos separados por coma: ", self.Conjuntos.subConjuntos)
            seleccion = self.diferencia(seleccion[0],seleccion[1])
            messagebox.showinfo("Operacion","Diferencia: " + str(seleccion))
        else:
            messagebox.showwarning("Alert","Debes tener como minimo 2 subconjuntos")
    
    def menu_complemento(self):
        seleccion = self.menu_2("Seleccionar 1 conjunto: ", self.Conjuntos.subConjuntos)
        seleccion = self.complemento(self.Conjuntos.universo,seleccion)
        messagebox.showinfo("Operacion","Complemento: " + str(seleccion))
    

    def operaciones_automaticas(self):
        respuesta = ""
        if len(self.Conjuntos.subConjuntos) >= 2:

            for x in self.Conjuntos.subConjuntos:
                for y in self.Conjuntos.subConjuntos:
                    if x!=y:
                        respuesta+="\n"+str(x)+"∩"+str(y)+": " + str(self.interseccion(x,y))+"\n"+str(x)+"U"+str(y)+": " + str(self.union(x,y))+"\n"+str(x)+"-"+str(y)+": " + str(self.diferencia(x,y))+"\n"+str(x)+"': " + str(self.complemento(self.Conjuntos.universo,x))
                        


            messagebox.showinfo("Operacion","Automatico: \n" + respuesta)
        else:
            messagebox.showerror("Alert","Debes tener como minimo 2 subconjuntos")
            
       



    def complemento(self,universo,sub):
        return universo.difference(sub)  
    def diferencia(self,sub1,sub2):
        return sub1.difference(sub2)
    def union(self,sub1,sub2):
        return sub1.union(sub2)  
    def interseccion(self,sub1,sub2):
        return sub1.intersection(sub2)

    
    def volver(self):
        self.ventana.withdraw()
        self.ventana_principal.deiconify()
    
