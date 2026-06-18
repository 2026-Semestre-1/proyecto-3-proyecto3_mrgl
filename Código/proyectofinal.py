import tkinter as tk
from tkinter import *


""""
Nombre:
entrada:
salida:
restricciones:
"""""


class País:
    def __init__(self):
        self.codigo_fifa=""
        self.nombre=""
        self.continente=""
        self.ranking_fifa=0
    def registrarP(self,):

        pai="paises.txt"
        archivo=open(pai,"a")
        contenido=








ventana=tk.Tk()
ventana.title("COPA MUNDIAL")
ventana.geometry("800x800")
fondo=PhotoImage(file="logo2026.png")
ventana.configure(bg="")
fondo_label=Label(ventana,image=fondo)
fondo_label.place(x=0,y=0,relwidth=1,relheight=1)
fondo_label=fondo

marco_main=tk.Frame(ventana,bg="gold",bd=2,relief="ridge")
marco_main.place(relx=0.5,rely=0.5,anchor="center",width=500,height=450)
####################################################################################################################################################################################################
boton_adminPais=tk.Button(marco_main,text="administrar países y selecciones",font=("Segoe Ui",12,"bold"),bg="#076529",fg="white",activebackground="#3b9d22",relief="flat",cursor="hand2")
boton_adminPais.pack(pady=25,padx=25,fill="x")
boton_adminEntre=tk.Button(marco_main,text="Administrar entrenadres y jugadores",font=("Segoe Ui",12,"bold"),bg="#0C2268",fg="White",activebackground="#0C2268",relief="flat",cursor="hand2")
boton_adminEntre.pack(pady=25,padx=25,fill="x")
boton_configMun=tk.Button(marco_main,text="Configurar Mundial",font=("Segoe Ui",12,"bold"),bg="#076529",fg="white",activebackground="#3b9d22",relief="flat",cursor="hand2")
boton_configMun.pack(padx=25,pady=25,fill="x")
boton_jugarM=tk.Button(marco_main,text="Jugar Mundial",font=("Segoe Ui",12,"bold"),bg="#0C2268",fg="White",activebackground="#0C2268",relief="flat",cursor="hand2")
boton_jugarM.pack(padx=25,pady=25,fill="x")
boton_Estadistica=tk.Button(marco_main,text="Ver Estadística",font=("Segoe Ui",12,"bold"),bg="#076529",fg="white",activebackground="#3b9d22",relief="flat",cursor="hand2")
boton_Estadistica.pack(padx=25,pady=25,fill="x")
ventana.mainloop()
