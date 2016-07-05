import os
from Tkinter import *

def apagar():
    h = horas.get()
    m = minutos.get()
    if h == "" and m == "":
        h = 0
        m = 10
    elif h == "" and m != "":
        h = 0
        m = int(m)
    elif h != "" and m == "":
        h = int(h)
        m = 0
    else:
        h = int(h)
        m = int(m)
    tiempo = (h * 3600) + (m * 60)
    comando = "shutdown -s -t " + str(tiempo)
    os.system(comando)
    horas.set("")
    minutos.set("")

def abortar():
    os.system("shutdown -a")
    horas.set("")
    minutos.set("")

ventana = Tk()
ventana.title("Apagar Sistema")
ventana.geometry("230x80")
horas = StringVar()
minutos = StringVar()
l_horas = Label(ventana, text = "Horas: ").grid(row = 0, column = 0)
txt_horas = Entry(ventana, textvariable = horas).grid(row = 0, column = 1)
l_minutos = Label(ventana, text = "Minutos: ").grid(row = 1, column = 0)
txt_minutos = Entry(ventana, textvariable = minutos).grid(row = 1, column = 1)
aceptar = Button(ventana, text = "Apagar", fg = "#c82626", command = apagar).place(x = 60, y = 50)
cancelar = Button(ventana, text = "Cancelar", fg = "#1322e3", command = abortar).place(x = 110, y = 50)
ventana.mainloop()
