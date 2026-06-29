import tkinter as tk
from tkinter import *
from tkinter import ttk
from classEntrenador import Entrenador
from adminPais import adminPais
from classPais import País
from tkinter import messagebox
from adminEntrenador_Futbolista import admin_todo
from classfase import fase
from classgrupo import grupo
from classMundial import Mundial
from classPartido import partido
admin=adminPais()
admin.cargar_pais()
admin.cargar_seleccion()
adminju=admin_todo()
adminju.cargar_entrenador()
adminju.cargar_jugador()
adminMun=Mundial("COPA MUNDIAL",2026)

#interfaz de administración de países y selecciones
def interfaz_adPa():
    ventana=Toplevel()
    ventana.title("Administración de Países y Selecciones")
    ventana.config(bg="#015CB7")
    ventana.geometry("700x700")

    frame_botones=tk.Frame(ventana)
    frame_botones.place(relx=0.5,rely=0.5,anchor="center",width=500,height=450)


    boton_adminPais=tk.Button(frame_botones,text="administrar países",font=("Segoe Ui",12,"bold"),bg="#AFAFAF",fg="white",activebackground="#3b9d22",relief="flat",cursor="hand2",command=ventana_paises_seleccionados)
    boton_adminPais.pack(pady=25,padx=25,fill="x")
    boton_adminSelee=tk.Button(frame_botones,text="Administrar Selecciones",font=("Segoe Ui",12,"bold"),bg="#C5C5C5",fg="White",activebackground="#0C2268",relief="flat",cursor="hand2",command=agregar_seleccion)
    boton_adminSelee.pack(pady=25,padx=25,fill="x")
    boton_mostrarInfo=tk.Button(frame_botones,text="Ver tablas",font=("Segoe Ui",12,"bold"),bg="#C9C9C9",fg="white",activebackground="#3b9d22",relief="flat",cursor="hand2",command=tab_paises)
    boton_mostrarInfo.pack(padx=25,pady=25,fill="x")
    boton_regresar=tk.Button(frame_botones,text="Regresar",font=("Segoe Ui",12,"bold"),bg="#C3C3C3",fg="white",activebackground="#3b9d22",relief="flat",cursor="hand2",command=ventana.destroy)
    boton_regresar.pack()

def ventana_paises_seleccionados():#ventana de los entrys que guardan los datos
   
    ventana=Toplevel()
    ventana.title("Agregar país")
    ventana.config(bg="#0B567B")
    ventana.geometry("700x500")

    frame_pais=tk.LabelFrame(ventana,text="Países",padx=10,pady=10,width=700,height=700)
    frame_pais.pack(padx=50,pady=50)

    tk.Label(frame_pais,text="Código FIFA").pack()
    codigo=Entry(frame_pais)
    codigo.pack()

    tk.Label(frame_pais,text="Nombre del país").pack()
    nombre=Entry(frame_pais)
    nombre.pack()

    tk.Label(frame_pais,text="Continente").pack()
    continente=tk.Entry(frame_pais)
    continente.pack()

    tk.Label(frame_pais,text="Ranking FIFA").pack()
    ranking=tk.Entry(frame_pais)
    ranking.pack()
    def agregar_pais():#agrega el país al txt y a la tabla
      global admin
      admin.agregar_pais(codigo.get(),nombre.get(),continente.get(),ranking.get())
      messagebox.showinfo("País agregado con éxito",parent=ventana)
    
    tk.Button(frame_pais,text="Agregar País",command=agregar_pais).pack()
    tk.Button(frame_pais,text="Regresar",command=ventana.destroy).pack()


def tab_paises():#la tabla que agarra las clases y los archivos txt y muestra los datos
    ventana=Toplevel()
    ventana.title("Países registrados")
    ventana.config(bg="#42B80F")
    ventana.geometry("500x300")
    tk.Button(ventana,text="Regresar",command=ventana.destroy).pack(anchor="ne",padx=10,pady=5)
    tk.Label(ventana,text="Doble click a la linea para actualizar los datos").pack()

    tabla_paises=ttk.Treeview(ventana,columns=("codigo","nombre","continente","codigo_seleccion","entrenador","ranking"),show="headings")
    tabla_paises.heading("codigo",text="Código")
    tabla_paises.heading("nombre",text="Nombre")
    tabla_paises.heading("continente",text="Continente")
    tabla_paises.heading("codigo_seleccion",text="Código de la seleccion")
    tabla_paises.heading("entrenador",text="Entrenador")
    tabla_paises.heading("ranking",text="Ranking")
    tabla_paises.pack(fill="both",expand=True,padx=10,pady=10)
    global admin
    for pais in admin.lista_paises:
            codigo_seleccion=""
            entrenador=""
            for seleccion in admin.lista_selecciones:
                     if seleccion.pais==pais.nombre:
                          codigo_seleccion=seleccion.codigo#variable para definir las clases de la seleccion
                          entrenador=seleccion.entrenador
            tabla_paises.insert("","end",values=(pais.codigo_fifa,pais.nombre,pais.continente,codigo_seleccion,entrenador,pais.ranking_fifa))#mete los datos a la tabla


    def actualizar(event):#actualiza los datos de la tabla con .entry y con insert para meterlo a la tabla
         seleccion=tabla_paises.focus()#agarra la linea azul que queremos editar
         if seleccion:
            valor=tabla_paises.item(seleccion,"values")
            ventana_actualizar=Toplevel()
            ventana_actualizar.title("Actualizar")

            tk.Label(ventana_actualizar,text="Código").pack()
            codigo=tk.Entry(ventana_actualizar)
            codigo.insert(0,valor[0])
            codigo.pack()

            tk.Label(ventana_actualizar,text="Nombre").pack()
            nombre=tk.Entry(ventana_actualizar)
            nombre.insert(0,valor[1])
            nombre.pack()

            tk.Label(ventana_actualizar,text="Continente").pack()
            continente=tk.Entry(ventana_actualizar)
            continente.insert(0,valor[2])
            continente.pack()


            tk.Label(ventana_actualizar,text="Ranking").pack()
            ranking=tk.Entry(ventana_actualizar)
            ranking.insert(0,valor[5])
            ranking.pack()
            

            def guardar():
                 global admin 
                 for pais in admin.lista_paises:
                      if pais.codigo_fifa==valor[0]:
                           pais.actualizar_datos(codigo.get(),nombre.get(),continente.get(),ranking.get())#actualiza los datos
                      admin.guardar_pais()
                      messagebox.showinfo("datos actualizados",parent=ventana_actualizar)
            tk.Button(ventana_actualizar,text="Guardar",command=guardar).pack()
            tk.Button(ventana_actualizar,text="Cerrar",command=ventana_actualizar.destroy).pack()
    tabla_paises.bind("<Double-Button-1>",actualizar)#sirve para abrir el formularo de editar con doble click a la barra azul


   

def agregar_seleccion():#funcion para agregar a la seleccion en el archivo txt y a la tabla
    ventana=Toplevel()
    ventana.title("Agregar selección")
    ventana.config(bg="#B40C0C")
    ventana.geometry("700x500")

    frame_pais=tk.LabelFrame(ventana,text="Selección",padx=10,pady=10,width=700,height=700)
    frame_pais.pack(padx=50,pady=50)

    tk.Label(frame_pais,text="Código del Equipo").pack()
    codigo=Entry(frame_pais)
    codigo.pack()

    tk.Label(frame_pais,text="País").pack()
    nombre_del_pais=[]
    for pais in admin.lista_paises:
         nombre_del_pais=nombre_del_pais+[pais.nombre]

    if len(nombre_del_pais)==0:#lee que primero haya un país registrado
        nombre_del_pais=[""]


    paisslece_var=StringVar()
    menu=tk.OptionMenu(frame_pais,paisslece_var,*nombre_del_pais)
    menu.pack()

    tk.Label(frame_pais,text="Entrenador").pack()
    nombre_del_entrenador=[]
    for entrenador in adminju.lista_entrenadores:
         nombre_del_entrenador=nombre_del_entrenador+[entrenador.nombre]

    if len(nombre_del_entrenador)==0:#lee que primero haya un país registrado
        nombre_del_entrenador=[""]


    entrenador_var=StringVar()
    menu=tk.OptionMenu(frame_pais,entrenador_var,*nombre_del_entrenador)
    menu.pack()
    def agregar_selecciones():
         global admin
         for seleccion in admin.lista_selecciones:
            if seleccion.entrenador==entrenador_var.get():
                 messagebox.showerror("Error","entrenador ya escogido",parent=ventana)
                 return
         admin.agregar_selecciones(codigo.get(),paisslece_var.get(),entrenador_var.get())
         messagebox.showinfo("Selección agregada con éxito",parent=ventana)
    
    tk.Button(frame_pais,text="Agregar selección",command=agregar_selecciones).pack()
    tk.Button(frame_pais,text="Regresar",command=ventana.destroy).pack()
#######################################################################################################################################################
def interfaz_adJu():
    ventana=Toplevel()
    ventana.title("Administración de jugadores y entrenadores")
    ventana.config(bg="#1F0678")
    ventana.geometry("700x700")

    frame_botones=tk.Frame(ventana)
    frame_botones.place(relx=0.5,rely=0.5,anchor="center",width=500,height=450)


    boton_adminPais=tk.Button(frame_botones,text="agregar jugador",font=("Segoe Ui",12,"bold"),bg="#929292",fg="white",activebackground="#3b9d22",relief="flat",cursor="hand2",command=ventana_jugadores_entrenadores)
    boton_adminPais.pack(pady=25,padx=25,fill="x")
    boton_adminSelee=tk.Button(frame_botones,text="agregar entrenador",font=("Segoe Ui",12,"bold"),bg="#AFAFAF",fg="White",activebackground="#0C2268",relief="flat",cursor="hand2",command=ventana_entrenador)
    boton_adminSelee.pack(pady=25,padx=25,fill="x")
    boton_mostrarInfo=tk.Button(frame_botones,text="Ver tablas",font=("Segoe Ui",12,"bold"),bg="#7F7F7F",fg="white",activebackground="#3b9d22",relief="flat",cursor="hand2",command=tabla_jugadores)
    boton_mostrarInfo.pack(padx=25,pady=25,fill="x")
    boton_regresar=tk.Button(frame_botones,text="Regresar",font=("Segoe Ui",12,"bold"),bg="#A6A6A6",fg="white",activebackground="#3b9d22",relief="flat",cursor="hand2",command=ventana.destroy)
    boton_regresar.pack()

#################################################################################################################################################################################################################################
def ventana_jugadores_entrenadores():#ventana de los entrys que guardan los datos
   
    ventana=Toplevel()
    ventana.title("Agregar jugador")
    ventana.config(bg="#D1A516")
    ventana.geometry("700x500")

    frame_jugadores=tk.LabelFrame(ventana,text="Jugador",padx=10,pady=10,width=700,height=700)
    frame_jugadores.pack(padx=50,pady=50)

    tk.Label(frame_jugadores,text="Nombre").pack()
    nombre=Entry(frame_jugadores)
    nombre.pack()

    tk.Label(frame_jugadores,text="Apellido").pack()
    apellido=Entry(frame_jugadores)
    apellido.pack()

    tk.Label(frame_jugadores,text="Fecha de nacimiento").pack()
    fecha_naci=tk.Entry(frame_jugadores)
    fecha_naci.pack()

    tk.Label(frame_jugadores,text="Nacionalidad").pack()
    nacionalidad=tk.Entry(frame_jugadores)
    nacionalidad.pack()

    tk.Label(frame_jugadores,text="Dorsal").pack()
    Dorsal=tk.Entry(frame_jugadores)
    Dorsal.pack()

    tk.Label(frame_jugadores,text="Posición").pack()
    posicion=tk.Entry(frame_jugadores)
    posicion.pack()

    tk.Label(frame_jugadores,text="Puntaje individual").pack()
    puntaje_indi=ttk.Spinbox(frame_jugadores,from_=1,to=100,state="readonly")
    puntaje_indi.pack()

    tk.Label(frame_jugadores,text="Seleccion").pack()
    nombre_de_la_seleccion=[]
    for seleccion in admin.lista_selecciones:
         nombre_de_la_seleccion=nombre_de_la_seleccion+[seleccion.pais]

    if len(nombre_de_la_seleccion)==0:
         nombre_de_la_seleccion=[""]

    seleccions_var=StringVar()
    menu=tk.OptionMenu(frame_jugadores,seleccions_var,*nombre_de_la_seleccion)
    menu.pack()

    def agregar_jugador():#agrega el jugador al txt y a la tabla
      global admin
      if nombre.get()=="" or Dorsal.get()=="" or posicion.get()=="" or nacionalidad.get()=="" or fecha_naci.get()=="":
           messagebox.showerror("Error: no debe de tener espacios en blanco",parent=ventana)
           return
      if not Dorsal.get().isdigit():
           messagebox.showerror("Error", "el dorsal debe de ser solo numeros",parent=ventana)
           return
      adminju.agregar_jugador(nombre.get(),apellido.get(),fecha_naci.get(),nacionalidad.get(),Dorsal.get(),posicion.get(),puntaje_indi.get(),seleccions_var.get())
      messagebox.showinfo("Jugador agregado con éxito",parent=ventana)
    
    tk.Button(frame_jugadores,text="Agregar jugador",command=agregar_jugador).pack()
    tk.Button(frame_jugadores,text="Regresar",command=ventana.destroy).pack()
################################################################################################
def ventana_entrenador():
        ventana=Toplevel()
        ventana.title("Agregar jugador")
        ventana.config(bg="#06A9A6")
        ventana.geometry("700x500")

        frame_jugadores=tk.LabelFrame(ventana,text="Entrenador",padx=10,pady=10,width=700,height=700)
        frame_jugadores.pack(padx=50,pady=50)

        tk.Label(frame_jugadores,text="Nombre").pack()
        nombre=Entry(frame_jugadores)
        nombre.pack()

        tk.Label(frame_jugadores,text="Apellido").pack()
        apellido=Entry(frame_jugadores)
        apellido.pack()

        tk.Label(frame_jugadores,text="Fecha de nacimiento").pack()
        fecha_naci=tk.Entry(frame_jugadores)
        fecha_naci.pack()

        tk.Label(frame_jugadores,text="Nacionalidad").pack()
        nacionalidad=tk.Entry(frame_jugadores)
        nacionalidad.pack()

        tk.Label(frame_jugadores,text="Licencia").pack()
        licencia=tk.Entry(frame_jugadores)
        licencia.pack()

        tk.Label(frame_jugadores,text="Experiencia en años").pack()
        experiencia_años=tk.Entry(frame_jugadores)
        experiencia_años.pack()

        tk.Label(frame_jugadores,text="sistema de juego").pack()
        sistema_juego=tk.Entry(frame_jugadores)
        sistema_juego.pack()
        def agregar_entrenador():
            global admin
            if nombre.get()=="" or apellido.get()==""or fecha_naci.get()==""or nacionalidad.get()==""or licencia.get()==""or experiencia_años.get()==""or sistema_juego.get()=="":
                 messagebox.showerror("Error", "no debe de estar vacío")
                 return
            if not experiencia_años.get().isdigit():
                 messagebox.showerror("Error", "La experiencia debe de estar en números",parent=ventana)
                 return
            adminju.agregar_entrenador(nombre.get(),apellido.get(),fecha_naci.get(),nacionalidad.get(),licencia.get(),experiencia_años.get(),sistema_juego.get())
            messagebox.showinfo("Entrenador agregado con éxito",parent=ventana)
        tk.Button(frame_jugadores,text="Agregar entrenador",command=agregar_entrenador).pack()
        tk.Button(frame_jugadores,text="Regresar",command=ventana.destroy).pack()
#########################################################################################################################################################################################
def tabla_jugadores():
    ventana_listaJuga=Toplevel()
    ventana_listaJuga.title("Jugadores")
    ventana.config(bg="#D0EC19")
    ventana_listaJuga.geometry("800x500")

    tk.Label(ventana_listaJuga,text="Selección").pack()
    nombre_seleccion=[]
    for seleccion in admin.lista_selecciones:
        nombre_seleccion=nombre_seleccion+[seleccion.pais]
    if len(nombre_seleccion)==0:
         nombre_seleccion=["No hay selecciones registradas"]
    
    filtro_seleccion=StringVar()
    filtro_seleccion.set(nombre_seleccion[0])
    filtro_menu=tk.OptionMenu(ventana_listaJuga,filtro_seleccion,*nombre_seleccion)
    filtro_menu.pack()

   

    tabla_jugadores_sele=ttk.Treeview(ventana_listaJuga,columns=("nombre","apellido","dorsal","posicion","puntaje individual"),show="headings")
    tabla_jugadores_sele.heading("nombre",text="nombre")
    tabla_jugadores_sele.heading("apellido",text="apellido")
    tabla_jugadores_sele.heading("dorsal",text="dorsal")
    tabla_jugadores_sele.heading("posicion",text="posicion")
    tabla_jugadores_sele.heading("puntaje individual",text="puntaje individual")
    tabla_jugadores_sele.pack(fill="both",expand=True)

    def ponertabla():
        for fila in tabla_jugadores_sele.get_children():
              tabla_jugadores_sele.delete(fila)
        for jugador in adminju.lista_jugadores:
             print(f"{jugador.seleccion}{filtro_seleccion.get()}")
             if jugador.seleccion==filtro_seleccion.get():
                  tabla_jugadores_sele.insert("","end",values=(jugador.nombre,jugador.apellido,jugador.dorsal,jugador.posicion,jugador.puntaje_individual))
    ponertabla()
    tk.Button(ventana_listaJuga,text="Actualizar lista",command=ponertabla).pack(pady=5)
    def actualizar(event):
            seleccion=tabla_jugadores.focus()#agarra la linea azul que queremos editar
            if seleccion:
                valor=tabla_jugadores.item(seleccion,"values")
                ventana_actualizar=Toplevel()
                ventana_actualizar.title("Actualizar")

                tk.Label(ventana_actualizar,text="Nombre").pack()
                nombre=tk.Entry(ventana_actualizar)
                nombre.insert(0,valor[0])
                nombre.pack()

                tk.Label(ventana_actualizar,text="apellido").pack()
                apellido=tk.Entry(ventana_actualizar)
                apellido.insert(0,valor[1])
                apellido.pack()

                tk.Label(ventana_actualizar,text="dorsal").pack()
                dorsal=tk.Entry(ventana_actualizar)
                dorsal.insert(0,valor[2])
                dorsal.pack()


                tk.Label(ventana_actualizar,text="posicion").pack()
                posicion=tk.Entry(ventana_actualizar)
                posicion.insert(0,valor[3])
                posicion.pack()

                tk.Label(ventana_actualizar,text="puntaje individual").pack()
                puntaje_individual=ttk.Spinbox(ventana_actualizar,from_=1,to=100,state="readonly")
                puntaje_individual.insert(0,valor[4])
                puntaje_individual.pack()

            
            def guardar():
                 global admin 
                 for jugador in adminju.lista_jugadores:
                      if jugador.nombre==valor[0]:
                           jugador.actualizar_datos(nombre.get(),apellido.get(),dorsal.get(),posicion.get(),puntaje_individual.get())#actualiza los datos
                      admin.guardar_pais()
                      messagebox.showinfo("datos actualizados",parent=ventana_actualizar)
            tk.Button(ventana_actualizar,text="Guardar",command=guardar).pack()
            tk.Button(ventana_actualizar,text="Cerrar",command=ventana_actualizar.destroy).pack()
    tabla_jugadores_sele.bind("<Double-Button-1>",actualizar)#sirve para abrir el formularo de editar con doble click a la barra azul
    tk.Button(ventana_listaJuga,text="Regresar",command=ventana_listaJuga.destroy).pack(pady=5)
#######################################################################################################################################################################3
def configurar_mundial():
     ventana=Toplevel()
     ventana.config(bg="#BF0F0F")
     ventana.title("Configurar mundial")
     ventana.geometry("400x300")

     tk.Label(ventana,text="Cantidad de grupos(mínimo 2):").pack(pady=10)
     cantidad=tk.Entry(ventana)
     cantidad.pack()
     def iniciar():
          valor=cantidad.get()
          if not valor.isdigit():
               messagebox.showerror("Error","Debe de ingresar numeros",parent=ventana)
               return
         
          if int(valor)<2:
               messagebox.showerror("error","Mínimo 2 grupos")
               return
          for seleccion in admin.lista_selecciones:
               if not adminMun.validar_seleccion(seleccion):
                    messagebox.showerror("Error",f"{seleccion.pais} no tiene entre 11 y 20 jugadores",parent=ventana)
                    return
          adminMun.selecciones=admin.lista_selecciones
          adminMun.crear_grupos(int(valor))
          print(adminMun.grupos)
          ventana_grupo=Toplevel()
          ventana.title("Grupos")
          ventana.geometry("400x400")
          for grupo in adminMun.grupos:
               tk.Label(ventana_grupo,text=grupo.nombre_grupo,font=("Segoe UI",12,"bold")).pack(pady=5)
               for equipo in grupo.equipos:
                   print(equipo)
                   tk.Label(ventana_grupo,text=f"{equipo.pais}").pack()
          tk.Button(ventana_grupo,text="Cerrar",command=ventana_grupo.destroy).pack(pady=10)
     tk.Button(ventana,text="Crear Grupos",command=iniciar).pack(pady=20)
     tk.Button(ventana,text="Regresar",command=ventana.destroy).pack()



def Jugar_mundial():
     print        
            
     











    


#######################################################################################################################################################
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
boton_adminPais=tk.Button(marco_main,text="administrar países y selecciones",font=("Segoe Ui",12,"bold"),bg="#076529",fg="white",activebackground="#3b9d22",relief="flat",cursor="hand2",command=interfaz_adPa)
boton_adminPais.pack(pady=25,padx=25,fill="x")
boton_adminEntre=tk.Button(marco_main,text="Administrar entrenadres y jugadores",font=("Segoe Ui",12,"bold"),bg="#0C2268",fg="White",activebackground="#0C2268",relief="flat",cursor="hand2",command=interfaz_adJu)
boton_adminEntre.pack(pady=25,padx=25,fill="x")
boton_configMun=tk.Button(marco_main,text="Configurar Mundial",font=("Segoe Ui",12,"bold"),bg="#076529",fg="white",activebackground="#3b9d22",relief="flat",cursor="hand2",command=configurar_mundial)
boton_configMun.pack(padx=25,pady=25,fill="x")
boton_jugarM=tk.Button(marco_main,text="Jugar Mundial",font=("Segoe Ui",12,"bold"),bg="#0C2268",fg="White",activebackground="#0C2268",relief="flat",cursor="hand2")
boton_jugarM.pack(padx=25,pady=25,fill="x")
boton_Estadistica=tk.Button(marco_main,text="Ver Estadística",font=("Segoe Ui",12,"bold"),bg="#076529",fg="white",activebackground="#3b9d22",relief="flat",cursor="hand2")
boton_Estadistica.pack(padx=25,pady=25,fill="x")
ventana.mainloop()
