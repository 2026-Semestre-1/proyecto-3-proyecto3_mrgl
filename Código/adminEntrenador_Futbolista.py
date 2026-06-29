from classEntrenador import Entrenador
from classJugador import jugador

class admin_todo:
    """""
    nombre: init 
    entrada:recibe los self
    salida:guarda los archivos y los valores
    restricciones:debe de ser archivo y lista
    
    """
    def __init__(self):
        self.lista_entrenadores=[]
        self.lista_jugadores=[]
        self.archivo_entrenador="entrenadores.txt"
        self.archivo_jugador="jugadores.txt"
    """""
    nombre:agregar_entrenador
    entrada:self,nombre,apellido,fecha_nacimiento,nacionalidad,licencia,experiencia_años,sistema_juego
    salida:agrega el entrenador
    restricciones: tiene que ser str y string
    
    """
    def agregar_entrenador(self,nombre,apellido,fecha_nacimiento,nacionalidad,licencia,experiencia_años,sistema_juego):
        entrenador=Entrenador(nombre,apellido,fecha_nacimiento,nacionalidad,licencia,experiencia_años,sistema_juego)
        self.lista_entrenadores=self.lista_entrenadores+[entrenador]
        self.guardar_entrenador()
    """""
    nombre:agregar_jugador
    entrada:self,nombre,apellido,fecha_nacimiento,nacionalidad,dorsal,posicion,puntaje_individual,seleccion
    salida:agrega el jugador
    restricciones:debe de ser str y int
    
    """
    def agregar_jugador(self,nombre,apellido,fecha_nacimiento,nacionalidad,dorsal,posicion,puntaje_individual,seleccion):
        Jugador=jugador(nombre,apellido,fecha_nacimiento,nacionalidad,dorsal,posicion,puntaje_individual)
        Jugador.seleccion=seleccion
        self.lista_jugadores= self.lista_jugadores+[Jugador]
        self.guardar_jugador()
    """"
    nombre: guardar_entrenador
    entrada: todos los self
    salida:guarda el entrenador
    restricciones:debe de ser archivo y str
    
    """
    def guardar_entrenador(self):
        archivo=open(self.archivo_entrenador,"w")
        for entrenador in self.lista_entrenadores:
            linea=f"{entrenador.nombre}:{entrenador.apellido}:{entrenador.fecha_nacimiento}:{entrenador.nacionalidad}:{entrenador.licencia}:{entrenador.experiencia_años}:{entrenador.sistema_juego} \n"
            archivo.write(linea)
        archivo.close()


    """""
    nombre:borrar_jugadores
    entrada: recibe self,jugador_borrar
    salida: borra el jugador
    restricciones:debe de ser str
    
    """
    def borrar_jugadores(self,jugador_borrar):
        nueva_tabla=[]
        for jugador in self.lista_paises:
            if jugador.nombre!=jugador_borrar:
                nueva_tabla=nueva_tabla+[jugador]
            self.lista_jugadores=nueva_tabla
            self.guardar_jugador()


    """""
    nombre: guardar_jugador
    entrada: todos los self
    salida:guarda el jugador
    restricciones:debe de ser str y archivos
    
    """
    def guardar_jugador(self):
        archivo=open(self.archivo_jugador,"w")
        for jugador in self.lista_jugadores:
            linea=f"{jugador.nombre}:{jugador.apellido}:{jugador.fecha_nacimiento}:{jugador.nacionalidad}:{jugador.dorsal}:{jugador.posicion}:{jugador.posicion}:{jugador.puntaje_individual}:{jugador.seleccion}"
            archivo.write(linea)
        archivo.close()
    """""
    nombre: cargar_entrenador
    entrada: todos los self
    salida:carga los entrenadores
    restricciones:debe de ser lista y str
    
    """
    def cargar_entrenador(self):
        self.lista_entrenadores=[]
        try:
            archivo=open(self.archivo_entrenador,"r")
            for linea in archivo:
                datos=linea.strip().split(":")
                entrenador=Entrenador(datos[0],datos[1],datos[2],datos[3],datos[4],int(datos[5],datos[6]))
                self.lista_entrenadores=self.lista_entrenadores+[entrenador]
            archivo.close()
        except:
            pass
    """""
    nombre:cargar_jugador
    entrada: todos los self
    salida:carga los jugadores
    restricciones:debe de ser lista y archivos
    
    """
    def cargar_jugador(self):
        self.lista_jugadores=[]
        try:
            archivo=open(self.archivo_jugador,"r")
            for linea in archivo:
                datos=linea.strip().split(":")
                Jugador=jugador(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],int(datos[6]))
                Jugador.seleccion=datos[7]
                self.lista_jugadores=self.lista_jugadores+[Jugador]
            archivo.close()
        except:
            pass
