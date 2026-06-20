import tkinter as tk
from tkinter import *


""""
Nombre:
entrada:
salida:
restricciones:
"""""


class País:
    def __init__(self,codigofifa,nombres,continentes,ranking_fifa):
        self.codigo_fifa=codigofifa
        self.nombre=nombres
        self.continente=continentes
        self.ranking_fifas=ranking_fifa
    def mostrar_datos(self):
        codigo=self.codigo_fifa
        nombre=self.nombre
        continente=self.continente
        ranking=self.ranking_fifas
        print(f"""              
              Código del país:{codigo}
               Nombre del país:{nombre}
               Continente:{continente}
               Ranking de la FIFA:{ranking}
""")
    def actualizar_datos(self):
        joshua=joshua#Falta Terminarlo, hay que hacer los constructores y las clases primero
class Persona:
    def __init__(self,nombre,apellido,fecha_nacimiento,nacionalidad):
        self.nombre=nombre
        self.apellido=apellido
        self.fecha_nacimiento=fecha_nacimiento
        self.nacionalidad=nacionalidad
        if not isinstance(nombre,str):
            return "Error:el nombre tiene que ser en formato de letras"
        elif not isinstance(apellido,str):
            return "Error:El apellido tiene que ser en formato de letras"
        elif not isinstance(fecha_nacimiento,str):
            return "Error:La fecha de nacimiento debe de ser en formato de letras"
        elif not isinstance(nacionalidad,str):
            return "Error:La nacionalidad debe de ser de formato de letras"
        
    def mostrar(self):
        print(f"""
Nombre de la persona:{self.nombre}
Apellido de la persona:{self.apellido}
nacionalidad:{self.nacionalidad}
Fecha de nacimiento:{self.fecha_nacimiento}
""")
class Entrenador(Persona):
    def __init__(self, licencia,experiencia_años,sistemadejuego):
        self.licencia=licencia
        self.experiencia_años=experiencia_años
        self.sistemadejuego=sistemadejuego
        if not isinstance(licencia,str):
            return "Error:debe de ser de formato de letras"
       





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
