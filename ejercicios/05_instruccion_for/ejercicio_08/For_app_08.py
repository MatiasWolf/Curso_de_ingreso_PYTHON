import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Wolf
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        numero = int(prompt("UTN", "Ingrese un numero"))
        for valor in range(2, numero):
            if numero % valor == 0:
                print(f"{numero} no es primo")
                return False
        print(f"{numero} es primo")
        return True
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()