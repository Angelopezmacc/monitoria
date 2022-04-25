#se importan los mÃ³dulos a utilizar

from tkinter import *
import tkinter as tk 
from math import *
import math as mt
import sympy as sp
from matplotlib import pyplot
import pandas as pd
import mod1


#===============================================================================================================================================================================================
#                               Caracteristicas de la pagina 
#===============================================================================================================================================================================================
mainW = tk.Tk()
mainW.title("Sistema de préstamo de materiales EICT-UR")
mainW.geometry("700x700")
mainW.configure(bg = "FireBrick")
#mainW.iconbitmap('/home/monitoria/Documentos/proyecto/logo.ico')  
#mainW.iconbitmap(r'logo.ico')  

#===============================================================================================================================================================================================
#                                       titulo
#===============================================================================================================================================================================================
tt = tk.Label(mainW, text="Bienvenido ",bg="FireBrick",fg= "black",font = ("Brodway", 20) )
tt.pack(padx = 5,pady=5,ipadx=5,ipady=5,fill=tk.X  ) 

#===============================================================================================================================================================================================
#                                     Funciones
#===============================================================================================================================================================================================

def thanks():
    thanks_window()
    mainW.destroy()
    
    
    
# #===============================================================================================================================================================================================
#                                    Etiquetas
#===============================================================================================================================================================================================
e1 = tk.Label(mainW,text="Espacio para un mensaje...",bg="royal blue",fg="white",font=17 )
e1.pack(padx = 5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    

#===============================================================================================================================================================================================
#                                 Menu desplegable 
#===============================================================================================================================================================================================
#calculadora financiera
mb = tk.Menubutton(mainW,text=" Validar credenciales ")
mb.menu = tk.Menu(mb)
mb["menu"] = mb.menu
#Opciones
mb.menu.add_command(label="Inciar sesiòn o autenticarse",command = main_account_screen )

mb.configure(font=20)
mb.pack(side=tk.TOP,padx=30,pady=30)

#Salir
mb = tk.Menubutton(mainW,text=" Salir")
mb.menu = tk.Menu(mb)
mb["menu"] = mb.menu
#Opciones
mb.menu.add_command(label=" Salir ",command = thanks )

mb.configure(font=20)
mb.pack(side=tk.TOP,padx=30,pady=30)

# Cerrar pestaña
#cal_m=tk.Menubutton(mainW,text=" Cerrar ", command = thanks)
#cal_m.pack(side=tk.TOP,padx=30,pady=30)
#cal_m.configure(font=40)
#cal_m.menu=tk.Menu(cal_m)
#cal_m["menu"]=cal_m.menu






mainW.mainloop()


