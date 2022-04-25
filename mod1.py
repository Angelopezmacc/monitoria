from tkinter import *
import tkinter as tk 
from math import *
import math as mt
import sympy as sp
from matplotlib import pyplot
import pandas as pd


def ventana_prueba():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.configure(bg="FireBrick")
    

    file_name = "prueba.xlsx"
    df = pd.read_excel(file_name)
    print(df.head())
    e2=tk.Label(win,text="resultado",bg="royal blue",fg= "black",font = ("vernada", 15))
    e2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
    e3=tk.Label(win,text=df.head(), padx = 5,pady=10,width=50)
    e3.pack()
        

    
    win.mainloop()
    
def thanks_window():
    messagebox.showinfo(message="Mensaje", title="Título")
    Button(text="OK", command=delete_thanks_window).pack()
    
def delete_thanks_window():
    thanks_window.destroy()
