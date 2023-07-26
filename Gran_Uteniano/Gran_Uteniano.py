import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Wolf
División: Z

Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
Los participantes en la placa son: Giovanni, Gianni y Facundo. Fausto no fue nominado y Marina no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:
A) Nombre del votante
B) Edad del votante (debe ser mayor a 13)
C) Género del votante (Masculino, Femenino, Otro)
D) El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:
A- El promedio de edad de las votantes de género Femenino 
B- Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
C- Nombre del votante más joven qué votó a Gianni.
D- Nombre de cada participante y porcentaje de los votos qué recibió.
E- El nombre del participante que debe dejar la casa (El que tiene más votos)

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_nombres = []
        self.lista_edades = []
        self.lista_generos = [] 
        self.lista_participantes = []


    def btn_mostrar_on_click(self):
        #########################################PUNTO A#########################################################
        #A- El promedio de edad de las votantes de género Femenino 
        
        contador_femenino = 0
        acumulador_femenino = 0
        for i in range(len(self.lista_generos)):
            if self.lista_generos[i] == "Femenino":
                acumulador_femenino += self.lista_edades[i]
                contador_femenino += 1
                
        if contador_femenino >= 1:
            promedio_edad_femenino = acumulador_femenino / contador_femenino
        else:
            promedio_edad_femenino = "No hubo votantes femeninos"
        
        print(f"El promedio de edades de votantes femeninos es: {promedio_edad_femenino:.2f}")
        
        #########################################PUNTO B#########################################################
        #B- Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
        
        contador_masculino = 0
        for i in range(len(self.lista_edades)):
            if (self.lista_generos[i] == "Masculino" and 
                self.lista_edades[i] > 24 and self.lista_edades[i] < 41 and 
                (self.lista_participantes[i] == "Giovanni" or self.lista_participantes[i] == "Facundo")):
                contador_masculino += 1

        print(f"La cantidad de votantes masculinos entre 25 y 40 años que votaron a Facundo son: {contador_masculino}")

        #########################################PUNTO C#########################################################
        #C- Nombre del votante más joven qué votó a Gianni.
        
        minimo = None
        nombre_minimo = None
        for i in range(len(self.lista_participantes)):
            if self.lista_participantes[i] == "Gianni":
                if minimo == None or self.lista_edades[i] < minimo:
                    minimo = self.lista_edades[i]
                nombre_minimo = self.lista_nombres[i]
        
        if nombre_minimo == None and minimo == None:
            print("Ningun votante eligió a Gianni")
        else:
            print(f"El votante mas joven que eligió a Gianni es: {nombre_minimo} de {minimo} años de edad")

        #########################################PUNTO D#########################################################
        #D- Nombre de cada participante y porcentaje de los votos qué recibió.
        
        contador_Giovanni = 0
        contador_Facundo = 0
        contador_Gianni = 0
        porcentaje_votos_Giovanni = 0
        porcentaje_votos_Gianni = 0
        porcentaje_votos_Facundo = 0
        
        for i in range(len(self.lista_participantes)):
            if self.lista_participantes[i] == "Giovanni":
                contador_Giovanni += 1
            elif self.lista_participantes[i] == "Facundo":
                contador_Facundo += 1
            else:
                contador_Gianni += 1
        
        porcentaje_votos_Giovanni = (contador_Giovanni * 100) / len(self.lista_participantes)
        porcentaje_votos_Facundo = (contador_Facundo * 100) / len(self.lista_participantes)
        porcentaje_votos_Gianni = (contador_Gianni * 100) / len(self.lista_participantes)
        
        print(f"El porcentaje de votos para Giovanni es: {porcentaje_votos_Giovanni:.2f}%\n\
        El porcentaje de votos para Gianni es: {porcentaje_votos_Gianni:.2f}%\n\
        El porcentaje de votos para Facundo es: {porcentaje_votos_Facundo:.2f}%")
        
        #########################################PUNTO E#########################################################
        #E- El nombre del participante que debe dejar la casa (El que tiene más votos)
        
        if contador_Facundo > contador_Gianni and contador_Facundo > contador_Giovanni:
            participante_expulsado = "Facundo"
            porcentaje_expulsado = porcentaje_votos_Facundo
        elif contador_Gianni > contador_Giovanni:
            participante_expulsado = "Gianni"
            porcentaje_expulsado = porcentaje_votos_Gianni
        else:
            participante_expulsado = "Giovanni"
            porcentaje_expulsado = porcentaje_votos_Giovanni
        mensaje = f"Quien debe abandonar la casa es: {participante_expulsado} con el {porcentaje_expulsado}% de los votos"
        print(mensaje)
        
    def btn_cargar_on_click(self):
        continuar = True
        while continuar == True:
            #A) Nombre del votante
            nombre_votante = prompt("Gran Uteniano", "Ingrese su nombre")
            while not nombre_votante.isalpha or len(nombre_votante) < 3:
                nombre_votante = prompt("Gran Uteniano", "Reingrese su nombre correctamente")
            
            self.lista_nombres.append(nombre_votante)
            
            #B) Edad del votante (debe ser mayor a 13)
            edad_votante = int(prompt("Gran Uteniano", "Ingrese su edad (Unicamente pueden votar mayores de 13 años)"))
            while edad_votante < 13:
                edad_votante = int(prompt("Gran Uteniano", "Reingrese su edad correctamente"))
            
            self.lista_edades.append(edad_votante)

            #C) Género del votante (Masculino, Femenino, Otro)
            genero_votante = prompt("Gran Uteniano", 'Ingrese su genero ("Masculino","Femenino","Otro")')
            while (genero_votante != "Masculino" and genero_votante != "Femenino" and genero_votante != "Otro") or not genero_votante.isalpha:
                genero_votante = prompt("Gran Uteniano", "Reingrese su genero respetando los ejemplos dados anteriormente")
            
            self.lista_generos.append(genero_votante)
            
            #D) El nombre del participante a quien le dará el voto negativo (Debe estar en placa)
            voto = prompt("Gran Uteniano", '¿Quien desea que abandone la casa?\n("Facundo","Gianni","Giovanni")')
            while (voto != "Facundo" and voto != "Gianni" and voto != "Giovanni") or not voto.isalpha:
                voto = prompt("Gran Uteniano", "Reingrese su voto correctamente")
            
            self.lista_participantes.append(voto)
            
            continuar = question("Gran Uteniano", "¿Hay algun otro televidente que desee votar?")
            if continuar == False:
                break
if __name__ == "__main__":
    app = App()
    app.mainloop()

