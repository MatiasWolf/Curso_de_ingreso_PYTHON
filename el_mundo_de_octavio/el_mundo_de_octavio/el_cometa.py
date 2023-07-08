import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

'''
La juguetería El MUNDO DE OCTAVIO nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

COMETA: 

AB = Diámetro mayor (se debe calcular)
DC = diámetro menor (se ingresa por prompt)
BD y BC = lados menores (se ingresa por prompt)
AD y AC = lados mayores (se ingresa por prompt)

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia.
La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="El Cometa 🪁", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.label_diametro_menor = customtkinter.CTkLabel(master=self, text="Diametro Menor DC")
        self.label_diametro_menor.grid(row=1, column=0, padx=20, pady=10)

        self.txt_diametro_menor= customtkinter.CTkEntry(master=self)
        self.txt_diametro_menor.grid(row=1, column=1)
        
        self.label_lados_menores = customtkinter.CTkLabel(master=self, text="Lados Menores BD y BC")
        self.label_lados_menores.grid(row=2, column=0, padx=20, pady=10)

        self.txt_lados_menores = customtkinter.CTkEntry(master=self)
        self.txt_lados_menores.grid(row=2, column=1)

        self.label_lados_mayores = customtkinter.CTkLabel(master=self, text="Lados Mayores AD y AC")
        self.label_lados_mayores.grid(row=3, column=0, padx=20, pady=10)

        self.txt_lados_mayores = customtkinter.CTkEntry(master=self)
        self.txt_lados_mayores.grid(row=3, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        diametro_menor_texto = prompt("Diametro Menor", "Ingrese el diametro menor")
        lado_menor = prompt("Longitud del lado menor", "Ingrese la medida del lado menor")
        lado_mayor = prompt("Longitud del lado mayor", "Ingrese la medida del lado mayor")
        
        #parseo
        diametro_menor = int(diametro_menor_texto)
        lado_menor_numero = int(lado_menor)
        lado_mayor_numero = int(lado_mayor)
        
        #calculos
        calculo_diametro_mayor_1 =  lado_mayor_numero ** 2 - (diametro_menor / 2)**2 
        calculo_diametro_mayor_2 = calculo_diametro_mayor_1 ** 0.5
        
        calculo_diametro_mayor_3 = lado_menor_numero ** 2 - (diametro_menor / 2)**2 
        calculo_diametro_mayor_4 = calculo_diametro_mayor_3 ** 0.5
        
        diametro_mayor = calculo_diametro_mayor_2 + calculo_diametro_mayor_4
        
        area_cometa = (diametro_mayor * diametro_menor) / 2
        perimetro_cometa = (lado_menor_numero * 2) + (lado_mayor_numero * 2) 
        mts_varillas = (perimetro_cometa + diametro_mayor + diametro_menor) / 100
        
        #area total del cometa
        cola_cometa = (area_cometa * 10) / 100
        area_total_cometa = area_cometa + cola_cometa
        mts_papel = area_total_cometa / 100
        
        #materiales para 10 cometas
        
        mts_papel_para_10_cometas = mts_papel * 10
        mts_varillas_para_10_cometas = (mts_varillas * 10)
        
        mensaje = "Los materiales necesarios para producir 10 cometas son:"
        mensaje_final = "{0} \n Varillas: {1:.2f} mts \n Papel: {2:.2f} mts cuadrados".format(mensaje, mts_varillas_para_10_cometas, mts_papel_para_10_cometas)
        
        self.txt_diametro_menor.delete(0, 'end')
        self.txt_diametro_menor.insert(0, diametro_menor)

        self.txt_lados_menores.delete(0, 'end')
        self.txt_lados_menores.insert(0, lado_menor_numero)

        self.txt_lados_mayores.delete(0, 'end')
        self.txt_lados_mayores.insert(0, lado_mayor_numero)
        
        alert("Cometas", mensaje_final)
            
        
        
        
        
        
        
        
        
        
        
        

    
if __name__ == "__main__":
    app = App()
    app.mainloop()