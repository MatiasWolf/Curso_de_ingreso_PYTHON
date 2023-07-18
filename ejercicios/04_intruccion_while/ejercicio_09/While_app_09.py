import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Wolf
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        
        contador = 0
        maximo = None
        minimo = None
        continuar = True
        while continuar == True:
            numero = prompt("UTN", "Ingrese un numero")
            contador += 1
            numero = int(numero)
            if maximo == None or maximo < numero:
                maximo = numero
            if minimo == None or minimo > numero:
                minimo = numero
            
            continuar = question("UTN", "¿Desea continuar ingresando numeros?")
            if continuar == False:
                break
        
        self.txt_maximo.delete(0, "end")
        self.txt_maximo.insert(0, maximo)
        self.txt_minimo.delete(0, "end")
        self.txt_minimo.insert(0, minimo)
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
