import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

"""
Nombre: Matias
Apellido: Wolf
Enunciado: Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular:


1 -nombre , edad y género de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y su género es xxx"

2 -pedir la altura de la persona e informar si es bajo: menor a 140 cm,  
medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.

3- Validar todos los datos.

4- En las vacaciones se pueden seleccionar distintas excursiones para realizar. Se pueden hacer desde 0 excursiones a 11 excursiones.

5- Una vez ingresada la cantidad se debe pedir por cada excursión 
el importe y el tipo de excursión (caminata  o vehículo). 
informar cual es el precio más caro, el más barato y el promedio

6- Informar cual es el tipo de excursión (caminata  o vehículo) más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)
"""


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()


        self.title("UTN FRA")
        self.minsize(320, 250)


        self.label_title = customtkinter.CTkLabel(master=self, text="Tour", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
    
    def btn_mostrar_on_click(self):
        
        nombre = prompt("UTN", "Ingrese su nombre")
        while nombre.isdigit() or nombre == None or nombre == "" or len(nombre) < 3:
            nombre = prompt("UTN", "Reingrese su nombre")
            if nombre == None:
                break
        
        edad = prompt("UTN", "Ingrese su edad")
        while edad.isdigit() == False or edad == None or nombre == "":
            edad = prompt("UTN", "Reingrese su edad")
            if edad == None:
                break
        
        genero = prompt("UTN", 'Ingrese su genero\nPor ej.: "Masculino"/"Femenino"/"No Binario"')
        while genero != "Masculino" and genero != "Femenino" and genero != "No Binario" or genero == None or genero == "":
            genero = prompt("UTN", "Reingrese su genero, respetando los ejemplos dados")
            if genero == None:
                break
        
        altura = prompt("UTN", "Ingrese su altura en centimetros")
        while altura.isdigit() == False or edad == None or genero == "":
            altura = prompt("UTN", "Reingrese su altura en centimetros")
            if altura == None:
                break
        
        
        
        
        edad = int(edad)
        altura = int(altura)
        
        if altura < 140:
            mensaje_altura = "bajo"
        elif altura <= 170:
            mensaje_altura = "medio"
        elif altura <= 190:
            mensaje_altura = "alto"
        else:
            mensaje_altura = "muy alto"
        
        alert("UTN", "Usted es {0}, tiene {1} años de edad, su género es {2} y su altura es: {3}".format(nombre, edad, genero, mensaje_altura))
        
        cantidad_exc = prompt("Excursiones", "Ingrese la cantidad de excursiones (entre 0 y 11)")
        while cantidad_exc == None or cantidad_exc.isdigit() == False:
            cantidad_exc = prompt("Excursiones", "Reingrese la cantidad de excursiones (entre 0 y 11)")
        cantidad_exc = int(cantidad_exc)
        
        contador_exc = 0
        precio_caro = 0
        tipo_mas_caro = ''
        precio_barato = 0
        tipo_mas_barato = ''
        promedio_precios = 0
        suma_de_precios = 0
        
        tipo_mas_elegido = ''
        contador_tipo_caminata = 0
        contador_tipo_vehiculo = 0
        
        while contador_exc < cantidad_exc:
            
            importe = prompt("Importe", "Ingrese su importe")
            while importe == None or not importe.isdigit():
                importe = prompt("Importe", "Reingrese su importe")
            importe_int = int(importe)
            
            tipo = prompt("Tipo de excursion", "Ingrese el tipo de excursion")
            while tipo != "Caminata" and tipo != "Vehiculo":
                tipo = prompt("Tipo de excursion", "Reingrese el tipo de excursion")
            
            while precio_barato == 0:
                precio_barato += importe_int
            
            if precio_barato == None or importe_int < precio_barato:
                precio_barato = importe_int
                

            if precio_caro == None or  importe_int > precio_caro:
                precio_caro = importe_int
                

            suma_de_precios += importe_int
            contador_exc += 1

            if tipo == "Caminata":
                contador_tipo_caminata += 1
            if tipo == "Vehiculo":
                contador_tipo_vehiculo += 1
        
        if contador_tipo_caminata > contador_tipo_vehiculo:
            tipo_mas_elegido = "Caminata"
        if contador_tipo_caminata < contador_tipo_vehiculo:
            tipo_mas_elegido = "Vehiculo"
        if contador_tipo_caminata == contador_tipo_vehiculo:
            tipo_mas_elegido = "Se eligieron ambos tipos de excursion por igual"
        
        promedio_precios = suma_de_precios / cantidad_exc
        
        mensaje = "La excursion mas barata vale: ${0}\n\
        La excursion mas cara vale: ${2}\n\
        El promedio de precios es de: ${4}\n\
        El tipo de excursión mas elegido es: {5}".format(precio_barato, tipo_mas_barato, precio_caro, tipo_mas_caro, promedio_precios, tipo_mas_elegido)
        
        alert("Informe", mensaje)
        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
