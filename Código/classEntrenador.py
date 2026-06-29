import classPersona
from classPersona import Persona


class Entrenador(Persona):
    """""
    nombre:init 
    entrada: recibe self, nombre,apellido,fecha_nacimiento,nacionalidad,licencia,experiencia_años,sistema_juego
    salida: muestra los valores guardados
    restricciones: debe de ser str y int
    
    """
    def __init__(self, nombre,apellido,fecha_nacimiento,nacionalidad,licencia,experiencia_años,sistema_juego):
        self.nombre=nombre
        self.apellido=apellido
        self.fecha_nacimiento=fecha_nacimiento
        self.nacionalidad=nacionalidad
        self.licencia=licencia
        self.experiencia_años=experiencia_años
        self.sistema_juego=sistema_juego
        

        """""
    nombre:mostrar_datos
    entrada: recibe los diferentes valores de las funciones
    salida: muestra toda la informacion
    restricciones: debe de ser str
    
    """
    def mostrar_datos(self):
        print(f"""
            Nombre del entrenador:{self.nombre}
            licencia:{self.licencia}
            Años de experencia:{self.experiencia_años}
            Sistema de juego:{self.sistema_juego}
""")
        

        """""
    nombre:actualizar_datos
    entrada: recibe self,nombre,apellido,fecha_nacimiento,nacionalidad,licencia,experiencia_años,sistemadejuego
    salida: muestra la actualizacion de los datos
    restricciones: tiene que ser str y int
    
    """
    def actualizar_datos(self ,nombre,apellido,fecha_nacimiento,nacionalidad,licencia,experiencia_años,sistemadejuego):
        nombre=self.nombre
        apellido=self.apellido
        fecha_nacimiento=self.fecha_nacimiento
        nacionalidad=self.nacionalidad
        licencia=self.licencia
        experiencia_años=self.experiencia_años
        sistemadejuego=self.sistema_juego
        
