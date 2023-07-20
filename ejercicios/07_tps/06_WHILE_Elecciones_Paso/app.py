'''
Nombre: Matias
Apellido: Wolf
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

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
        continuar = True
        acumulador_votos = 0
        contador_candidatos = 0
        acumulador_edades = 0
        maximo = 0
        minimo = 0
        bandera_primer_ingreso = False
        
        while continuar == True:
            
            candidato = prompt("PASO", "Ingrese el nombre del candidato a las paso")
            contador_candidatos += 1
            
            edad_candidato = prompt("PASO", "Ingrese la edad del candidato")
            edad_candidato = int(edad_candidato)
            while edad_candidato <= 25:
                edad_candidato = prompt("PASO", "Reingrese la edad correcta del candidato")
                edad_candidato = int(edad_candidato)
            acumulador_edades = acumulador_edades + edad_candidato
            
            votos = prompt("PASO", "Ingrese la cantidad de votos recibidos por el candidato")
            votos = int(votos)
            while votos < 0:
                votos = prompt("PASO", "Reingrese la cantidad correcta de votos recibidos por el candidato")
                votos = int(votos)
            acumulador_votos = acumulador_votos + votos
            #nombre del candidato con mas votos
            
            if votos > maximo or bandera_primer_ingreso == False:
                maximo = votos
                candidato_maximo = candidato
            
            #nombre y edad del candidato con menos votos
            if votos < minimo or bandera_primer_ingreso == False:
                minimo = votos
                candidato_minimo = candidato
                edad_candidato_minimo = edad_candidato
            bandera_primer_ingreso = True

            continuar = question("PASO", "¿Hay mas candidatos para ingresar?")
            if continuar == False:
                break
        
        promedio_edades = acumulador_edades / contador_candidatos
        mensaje_1 = f"El candidato con mas votos es: {candidato_maximo}\n\
        El candidato con menos votos es: {candidato_minimo}, de {edad_candidato_minimo} años de edad\n\
        El promedio de edades de los candidatos es: {promedio_edades}\n\
        El total de votos emitidos es: {acumulador_votos}"
        
        print(mensaje_1)
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
