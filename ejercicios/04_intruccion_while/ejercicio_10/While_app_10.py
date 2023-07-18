import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Wolf
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        acumulador_positivos = 0
        acumulador_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_cero = 0
        continuar = True
        while continuar == True:
            numero = prompt("UTN", "Ingrese un numero")
            numero = int(numero)
            
            if numero >= 0:
                acumulador_positivos += numero
                contador_positivos += 1
            if numero < 0:
                acumulador_negativos += numero
                contador_negativos += 1
            if numero == 0:
                contador_cero += 1
            
            continuar = question("UTN", "¿Desea seguir ingresando numeros?")
            if continuar == False:
                break
        
        diferencia_numeros = acumulador_positivos + acumulador_negativos
        
        alert("UTN", f"La suma acumulada de numeros positivos es: {acumulador_positivos}\n\
        La suma acumulada de numeros negativos es: {acumulador_negativos}\n\
        La cantidad de numeros positivos ingresados es: {contador_positivos}\n\
        La cantidad de numeros negativos ingresados es: {contador_negativos}\n\
        La cantidad de ceros ingresados es: {contador_cero}\n\
        La diferencia entre los numeros positivos y negativos es: {diferencia_numeros}")
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
