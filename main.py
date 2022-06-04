#se importan los mÃ³dulos a utilizar

from tkinter import *
import tkinter as tk 
from math import *
import math as mt
import pandas as pd
from tkinter import *
import os
import mod1
import prueba
from tkinter import messagebox
import xlsxwriter


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
tt = tk.Label(mainW, text="Bienvenido al software de préstamo de materiales de la EICT",bg="FireBrick",fg= "black",font = ("Brodway", 15) )
tt.pack(padx = 5,pady=5,ipadx=5,ipady=5,fill=tk.X  ) 

#===============================================================================================================================================================================================
#                                     Funciones
#===============================================================================================================================================================================================
def ventana_prueba():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.configure(bg="FireBrick")
    

    file_name = "materiales.xlsx"
    df = pd.read_excel(file_name)
    print(df.iloc[1]['material'])
    
    # e2=tk.Label(win,text="resultado",bg="royal blue",fg= "black",font = ("vernada", 15))
    # e2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
    # e3=tk.Label(win,text=df.head(), padx = 5,pady=10,width=50)
    # e3.pack()
    e2=tk.Label(win,text="Ingrese el número de la fila",bg="royal blue",fg= "white",font = ("vernada", 15))
    e2.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    entrada1=tk.Entry(win)
    entrada1.pack(padx = 5,pady=10,ipadx=5,ipady=10)
    
    e3=tk.Label(win,text="Ingrese su número de documento",bg="royal blue",fg= "white",font = ("vernada", 15))
    e3.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    entrada2=tk.Entry(win)
    entrada2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
    
    e4=tk.Label(win,text="Ingrese la fecha deseada",bg="royal blue",fg= "white",font = ("vernada", 15))
    e4.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    entrada3=tk.Entry(win)
    entrada3.pack(padx = 5,pady=10,ipadx=5,ipady=10)
    
    e5=tk.Label(win,text="Ingrese la hora deseada",bg="royal blue",fg= "white",font = ("vernada", 15))
    e5.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    entrada4=tk.Entry(win)
    entrada4.pack(padx = 5,pady=10,ipadx=5,ipady=10)
    
    def realizar_reserva():
        username1 = username_verify.get()
        material = df.iloc[int(entrada1.get())-2]['material']
        documento = entrada2.get()
        fecha = entrada3.get()
        hora = entrada4.get()
        
        archivo = xlsxwriter.Workbook("prueba.xlsx")
        hoja = archivo.add_worksheet()
        hoja.write(1,0,fecha)
        
        
        
        
    
    calcular=tk.Button(win,text="realizar reserva",command=realizar_reserva)
    calcular.pack(side=tk.TOP,padx=30,pady=30)
    calcular.configure(font=30)

def thanks_window():
    messagebox.showinfo(message="Gracias por utilizar el programa", title="Título")
    # tkMessageBox.showerror("Gracias por utilizar el programa")
    Button(text="OK", command=delete_thanks_window).pack()
    
def delete_thanks_window():
    thanks_window.destroy()
    
def thanks():
    thanks_window()
    mainW.destroy()
    
# ndsv
def thanks_window2():
    messagebox.showinfo(message="Por favor, autentiquese en la ventana que se va a abrir", title="Título")
    # tkMessageBox.showerror("Gracias por utilizar el programa")
    Button(text="OK", command=delete_thanks_window2).pack()
    
def delete_thanks_window2():
    thanks_window.destroy()
    
def thanks2():
    thanks_window2()
    mainW.destroy()
    
def destruir_ventana():
    Button(text="OK", command=delete_thanks_window).pack()

def delete_thanks_window():
    destruir_ventana.destroy()
    mainW.destroy()
# Login

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files and username1 == "admin":
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess2()
 
        else:
            password_not_recognised()
    elif username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
    
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
# login usuario normales 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=ventana_prueba).pack()
    autenticado = True

#login admin    
def login_sucess2():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("250x250")
    Label(login_success_screen, text="Usted se ha autenticado como administrador...").pack()
    Button(login_success_screen, text="OK", command=thanks_window).pack()
    autenticado = True
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text=" Invalid Username or Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text=" Invalid Username or Password ").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="FireBrick", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    
 
    main_screen.mainloop()
 

# #===============================================================================================================================================================================================
#                                    Etiquetas
#===============================================================================================================================================================================================
e1 = tk.Label(mainW,text="Por favor elija alguna opción del siguiente menú",bg="royal blue",fg="white",font=17 )
e1.pack(padx = 5,pady=5,ipadx=5,ipady=5,fill=tk.X)

#===============================================================================================================================================================================================
#                                 Menu desplegable 
#===============================================================================================================================================================================================
# #calculadora financiera
mb = tk.Menubutton(mainW,text=" Validar credenciales ")
mb.menu = tk.Menu(mb)
mb["menu"] = mb.menu
#Opciones
mb.menu.add_command(label="Inciar sesiòn o autenticarse",command = thanks2 )

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

mainW.mainloop()
main_account_screen()
# Cerrar pestaña
#cal_m=tk.Menubutton(mainW,text=" Cerrar ", command = thanks)
#cal_m.pack(side=tk.TOP,padx=30,pady=30)
#cal_m.configure(font=40)
#cal_m.menu=tk.Menu(cal_m)
#cal_m["menu"]=cal_m.menu









