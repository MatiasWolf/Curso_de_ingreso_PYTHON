import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca_lamparita = self.combobox_marca.get()
        cantidad_lamparita = int(self.combobox_cantidad.get())
        valor_lamparita = 800
        descuento = 0
        descuento_extra = 0

        #Venta de 3 lamparitas
        if cantidad_lamparita == 3:
            if marca_lamparita == "ArgentinaLuz":
                descuento = 15
            elif marca_lamparita == "FelipeLamparas":
                descuento = 10
            else:
                descuento = 5
        elif cantidad_lamparita == 4:
            if marca_lamparita == "ArgentinaLuz" or marca_lamparita == "FelipeLamparas":
                descuento = 25
            else:
                descuento = 20
        elif cantidad_lamparita == 5:
            if marca_lamparita == "ArgentinaLuz":
                descuento = 40
            else:
                descuento = 30
        elif cantidad_lamparita >= 6:
            descuento = 50
            
        total_importe = valor_lamparita * cantidad_lamparita
        descuento_aplicado = total_importe * descuento / 100
        importe_con_descuento = total_importe - descuento_aplicado
        
        mensaje = "Su importe final es de {0} \nCon un descuento aplicado del {1}%".format(importe_con_descuento, descuento)
        
        if importe_con_descuento > 4000:
            descuento_extra = importe_con_descuento * 5/100
            importe_final_con_descuento = importe_con_descuento - descuento_extra
            mensaje_extra = "Debido a que el importe supera los $4000, se le aplica un nuevo descuento del 5% \n Su importe final es de {0}".format(importe_final_con_descuento)
            mensaje = "Su importe final es de {0} \nCon un descuento aplicado del {1}% \n{2}".format(importe_con_descuento, descuento, mensaje_extra)
        alert("Titulo", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()