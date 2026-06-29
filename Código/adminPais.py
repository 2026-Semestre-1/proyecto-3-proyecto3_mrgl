from classPais import País
from classseleccion import seleccion
class adminPais:
    """"
Nombre:init 
entrada:recibe los self y los archivos
salida:guarda los archivos
restricciones:debe de ser txt y list
"""""
    def __init__(self):
        self.lista_paises=[]
        self.lista_selecciones=[]
        self.archivo_paises="paises.txt"
        self.archivo_selecciones="selecciones.txt"
    """"
Nombre:agregar_pais
entrada:ecibe self,codigofifa,nombre,continente,ranking
salida:agrega el pais
restricciones:debe de ser str
"""""
    def agregar_pais(self,codigofifa,nombre,continente,ranking):
        pais=País(codigofifa,nombre,continente,ranking)
        self.lista_paises=self.lista_paises+[pais]
        self.guardar_pais()
    """"
Nombre:agregar_selecciones
entrada: recibe self,codigo,pais,entrenador
salida:agrega las selecciones
restricciones:tiene que ser str
"""""
    def agregar_selecciones(self,codigo,pais,entrenador):
        Seleccion=seleccion(codigo,pais,entrenador)
        self.lista_selecciones= self.lista_selecciones+[Seleccion]
        self.guardar_selecciones()
    """"
Nombre:guardar_pais
entrada:recibe los self
salida:guarda el pais en el txt
restricciones:tiene que ser archivos y strings
"""""
    def guardar_pais(self):
        archivo=open(self.archivo_paises,"w")
        for pais in self.lista_paises:
            linea=f"{pais.codigo_fifa}:{pais.nombre}:{pais.continente}:{pais.ranking_fifa} \n"
            archivo.write(linea)
        archivo.close()

    """"
Nombre: borrar_pais
entrada: recibe self,pais_borrar
salida: borra el pais
restricciones:tiene que ser str
"""""

    def borrar_pais(self,pais_borrar):
        nueva_tabla=[]
        for pais in self.lista_paises:
            if pais.codigo_fifa!=pais_borrar:
                nueva_tabla=nueva_tabla+[pais]
            self.lista_paises=nueva_tabla
            self.guardar_pais()


    """"
Nombre: guardar_selecciones
entrada: todos los self
salida:guarda las selecciones
restricciones:debe deser archivos y str
"""""
    def guardar_selecciones(self):
        archivo=open(self.archivo_selecciones,"w")
        for selecciones in self.lista_selecciones:
            linea=f"{selecciones.codigo}:{selecciones.pais}:{selecciones.entrenador}"
            archivo.write(linea)
        archivo.close()
    """"
Nombre: cargar_pais
entrada: todos los self
salida: carga los paises
restricciones: debe de ser list y archivos
"""""
    def cargar_pais(self):
        self.lista_paises=[]
        try:
            archivo=open(self.archivo_paises,"r")
            for linea in archivo:
                datos=linea.strip().split(":")
                pais=País(datos[0],datos[1],datos[2],int(datos[3]))
                self.lista_paises=self.lista_paises+[pais]
            archivo.close()
        except:
            pass
    """"
Nombre:cargar_seleccion
entrada: todos los self
salida: carga la seleccion ppara mosrarla
restricciones: debe deser lista y archivos
"""""
    def cargar_seleccion(self):
        self.lista_selecciones=[]
        try:
            archivo=open(self.archivo_selecciones,"r")
            for linea in archivo:
                datos=linea.strip().split(":")
                Seleccion=seleccion(datos[0],datos[1],datos[2],datos[3])
                self.lista_selecciones=self.lista_selecciones+[Seleccion]
            archivo.close()
        except:
            pass
