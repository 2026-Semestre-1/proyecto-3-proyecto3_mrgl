import classPersona
from classPersona import Persona

class jugador(Persona) :
    """"
Nombre: init
entrada: recibe nombre,apellido,fecha_nacimiento,nacionalidad,dorsal,posicion,puntaje_individual
salida: muestra los self de los valores
restricciones:debe de ser str y int
"""""
    def __init__(self,nombre,apellido,fecha_nacimiento,nacionalidad,dorsal,posicion,puntaje_individual):
        self.nombre=nombre
        self.apellido=apellido
        self.fecha_nacimiento=fecha_nacimiento
        self.nacionalidad=nacionalidad
        self.dorsal=dorsal
        self.posicion=posicion
        self.total_tarjetas_amarillas=0
        self.total_tarjetas_rojas=0
        self.goles=0
        self.asistencias=0
        self.puntaje_individual=puntaje_individual
        """"
Nombre:motrar_datos
entrada:self y diferentes valores
salida:muestra todos los datos
restricciones:debe de ser str y int
"""""
    def mostrar_datos(self):
        print(f"""
                Nombre del jugador:{self.nombre}
                Apellido del jugador:{self.apellido}
                Fecha de nacimiento:{self.fecha_nacimiento}
                Nacionalidad:{self.nacionalidad}
                Dorsal:{self.dorsal}
                Estadisticas:
                        Goles:{self.goles}
                        Asistencias:{self.asistencias}
                Posición del jugador:{self.posicion}
                puntaje individual:{self.puntaje_individual}""")
    """"
Nombre: actualizar_datos
entrada: recibe nombre,apellido,fecha_nacimiento,nacionalidad,dorsal,posicion,puntaje_individual
salida: muestra los cambios de los valores otorgando nuevos valores
restricciones:debe de ser str y int
"""""
            
    def actualizar_datos(self,nombre,apellido,fecha_nacimiento,nacionalidad,dorsal,posicion,puntaje_individual):
        nombre=self.nombre
        apellido=self.apellido
        fecha_nacimiento=self.fecha_nacimiento
        nacionalidad=self.nacionalidad
        dorsal=self.dorsal
        posicion=self.posicion
        puntaje_individual=self.puntaje_individual
        """"
Nombre:registrar_gol
entrada: recibe el self y los diferentes valores de las funciones
salida:registra un gol
restricciones:debe de ser int
"""""
    def registrar_gol(self):
        self.goles+=1
        """"
Nombre:registrar_asistencias
entrada:self y diferentes valores de otras funciones
salida:registra 1 asistencia
restricciones:debe de ser int
"""""
    def registrar_asistencia(self):
        self.asistencias+=1
        """"
Nombre:registrar_tarjetas
entrada: recibe el tipo y el self
salida:muetras las trajetas segun el tipo
restricciones: debe de ser str y int
"""""
    def registrar_tarjetas(self,tipo):
        if tipo.lower()=="amarilla".lower():
            self.total_tarjetas_amarillas+=1
        elif tipo.lower()=="roja".lower():
            self.total_tarjetas_rojas+=1
        else:
            print("Error:trajeta no valida")