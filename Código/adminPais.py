from classPais import País
from classseleccion import seleccion
class adminPais:

    def __init__(self):
        self.lista_paises=[]
        self.lista_selecciones=[]
        self.archivo_paises="paises.txt"
        self.archivo_selecciones="selecciones.txt"

    def agregar_pais(self,codigofifa,nombre,continente,ranking):
        pais=País(codigofifa,nombre,continente,ranking)
        self.lista_paises=self.lista_paises+[pais]
        self.guardar_pais()

    def agregar_selecciones(self,codigo,pais,entrenador):
        Seleccion=seleccion(codigo,pais,entrenador)
        self.lista_selecciones= self.lista_selecciones+[Seleccion]
        self.guardar_selecciones()

    def guardar_pais(self):
        archivo=open(self.archivo_paises,"w")
        for pais in self.lista_paises:
            linea=f"{pais.codigo_fifa}:{pais.nombre}:{pais.continente}:{pais.ranking_fifa} \n"
            archivo.write(linea)
        archivo.close()



    def borrar_pais(self,pais_borrar):
        nueva_tabla=[]
        for pais in self.lista_paises:
            if pais.codigo_fifa!=pais_borrar:
                nueva_tabla=nueva_tabla+[pais]
            self.lista_paises=nueva_tabla
            self.guardar_pais()



    def guardar_selecciones(self):
        archivo=open(self.archivo_selecciones,"w")
        for selecciones in self.lista_selecciones:
            linea=f"{selecciones.codigo}:{selecciones.pais}:{selecciones.entrenador}"
            archivo.write(linea)
        archivo.close()

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
    def cargar_seleccion(self):
        self.lista_selecciones=[]
        try:
            archivo=open(self.archivo_selecciones,"r")
            for linea in archivo:
                datos=linea.strip().split(":")
                pais=País(datos[0],datos[1],datos[2],datos[3])
                self.lista_selecciones=self.lista_selecciones+[seleccion]
            archivo.close()
        except:
            pass
