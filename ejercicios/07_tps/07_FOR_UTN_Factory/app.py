'''
Nombre: Matias
Apellido: Wolf
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):
    

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        #Listas
        self.lista_nombres = []
        self.lista_edades = []
        self.lista_generos = []
        self.lista_tecnologias = []
        self.lista_puestos = []
        
        #Ingreso de datos
        for listas in range(10):
            
            nombre = prompt("UTN Software Factory", "Ingrese su nombre")
            while len(nombre) < 3 or not nombre.isalpha():
                nombre = prompt("UTN Software Factory", "Reingrese su nombre correctamente")
            self.lista_nombres.append(nombre)
            
            edad = int(prompt("UTN Software Factory", "ingrese su edad"))
            while edad < 18:
                edad = int(prompt("UTN Software Factory", "Reingrese su edad correctamente (mayor de edad)"))
            self.lista_edades.append(edad)
            
            genero = prompt("UTN Software Factory", "Ingrese su genero ('F','M','NB')")
            while genero != "F" and genero != "M" and genero != "NB":
                genero = prompt("UTN Software Factory", "Reingrese su genero correctamente ('F','M','NB')")
            self.lista_generos.append(genero)
            
            tecnologia = prompt("UTN Software Factory", "Ingrese la tecnologia que desarrolla ('PYTHON','JS','ASP.NET')")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("UTN Software Factory", "Reingrese la tecnologia que desarrolla correctamente ('PYTHON','JS','ASP.NET')")
            self.lista_tecnologias.append(tecnologia)
            
            puesto = prompt("UTN Software Factory", "Ingrese su puesto ('Jr','Ssr','Sr')")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt("UTN Software Factory", "Reingrese su puesto correctamente ('Jr','Ssr','Sr')")
            self.lista_puestos.append(puesto)
        
        #Informar
        ################################################PUNTO A###############################################################
        
        contador_A = 0
        for i in range(len(self.lista_generos)):
            if self.lista_generos[i] == "NB" and \
                (tecnologia == "ASP.NET" or tecnologia == "JS") and \
                (self.lista_edades[i] > 24 and self.lista_edades[i] < 41) and \
                self.lista_puestos[i] == "Ssr":
                contador_A += 1
        mensaje = f"La cantidad de postulantes de genero no binario que programan en ASP.NET o JS son: {contador_A}"
        print(mensaje)
        
        ################################################PUNTO B###############################################################
        
        nombre_minimo = None
        edad_minima = None
        
        for i in range(len(self.lista_puestos)):
            if self.lista_puestos[i] == "Jr":
                if edad_minima == None or self.lista_edades[i] < edad_minima:
                    edad_minima = self.lista_edades[i]
                    nombre_minimo = self.lista_nombres[i]

        if nombre_minimo == None and edad_minima == None:
            print("No hay ningun postulante Jr")
        else:
            print(f"El postulante Jr mas joven es: {nombre_minimo}")
        
        ################################################PUNTO c###############################################################
        
        contador_edades_M = 0
        acumulador_edades_M = 0
        contador_edades_F = 0
        acumulador_edades_F = 0
        contador_edades_NB = 0
        acumulador_edades_NB = 0
        
        for i in range(len(self.lista_generos)):
            if self.lista_generos[i] == "M":
                contador_edades_M += 1
                acumulador_edades_M += self.lista_edades[i]
            elif self.lista_generos[i] == "F":
                contador_edades_F += 1 
                acumulador_edades_F += self.lista_edades[i]
            else:
                contador_edades_NB += 1
                acumulador_edades_NB += self.lista_edades[i]
        
        if contador_edades_M != 0:
            promedio_edades_M = acumulador_edades_M / contador_edades_M
            mensaje = f"El promedio de edades de los postulantes masculinos es: {promedio_edades_M}"
        else:
            mensaje = "No hay postulantes masculinos"
        
        if contador_edades_F != 0:
            promedio_edades_F = acumulador_edades_F / contador_edades_F
            mensaje += f"El promedio de edades de las postulantes femeninas es: {promedio_edades_F}"
        else:
            mensaje += "No hay postulantes femeninos"
        
        if contador_edades_NB != 0:
            promedio_edades_NB = acumulador_edades_NB / contador_edades_NB
            mensaje += f"El promedio de edades de los postulantes no binarios es: {promedio_edades_NB}"
        else: 
            mensaje += "No hay postulantes no binarios"
        
        
        
        
        
        print(mensaje)
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
