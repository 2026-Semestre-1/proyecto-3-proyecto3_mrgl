import classseleccion
from classseleccion import seleccion
import random

class partido(seleccion):
    """"
Nombre:init
entrada:self,id_partido,equipo_1,equipo_2,fase,fecha
salida: muestra los archivos guardados de los diferentes self
restricciones:debe de ser str y int
"""""
    def __init__(self,id_partido,equipo_1,equipo_2,fase,fecha):
        self.id_partido=id_partido
        self.equipo_1=equipo_1
        self.equipo_2=equipo_2
        self.goles_equipo1=0
        self.goles_equipo2=0
        self.fase=fase
        self.fecha=fecha
        """"
Nombre:simular
entrada: recibe el self y los diferentes self de las diferentes funciones
salida: simula los partdios en base a diferentes factores
restricciones: debe de ser str y int
"""""
    def simular(self):
        fuerza1=self.equipo_1.calcular_fuerza_equipo()
        fuerza2=self.equipo_2.calcular_fuerza_equipo()
        diferencia=fuerza1-fuerza2
        if diferencia >30:
            self.goles_equipo1=random.randint(2,7)
            self.goles_equipo2=random.randint(0,3)
        elif diferencia>-30:
                self.goles_equipo1=random.randint(0,3)
                self.goles_equipo2=random.randint(2,7)
        elif diferencia>15:
                        self.goles_equipo1=random.randint(1,5)
                        self.goles_equipo2=random.randint(0,4)
        elif diferencia >-15:
                           self.goles_equipo1=random.randint(0,4)
                           self.goles_equipo2=random.randint(1,5)
        else: 
                 self.goles_equipo1=random.randint(0,4)
                 self.goles_equipo2=random.randint(0,4)
        """"
        Nombre: generar_ganador
        entrada: recibe los diferentes self
        salida: muestra los goles de los equipos
        restricciones: debe de ser int
        """""
    def generar_ganador(self):
          if self.goles_equipo1>self.goles_equipo2:
                  return self.equipo_1 
          elif self.goles_equipo2>self.equipo_1:
                  return self.equipo_2
          else:
                  return None
    """"
Nombre:simular_penales
entrada: recibe los diferentes self de las diferentes funciones
salida: muestra los goles de penales y el ganador
restricciones: debe de ser int
""""" 

    def simular_penales(self):
            penales_1=random.randint(0,5)
            penales_2=random.randint(0,5)
            while penales_1==penales_2:
                     penales_1=random.randint(0,5)
                     penales_2=random.randint(0,5)
            print(f"Penales {self.equipo_1}{penales_1} - {penales_2}{self.equipo_2}")
            if penales_1>penales_2:
                    return self.equipo_1
            else:
                    return self.equipo_2
    """"
Nombre:mostrar_resultados
entrada: recibe los self de las diferentes funciones
salida:muesta todos los resultados ganadores y perdedores
restricciones: debe de ser int y str
"""""
    def mostrar_resultados(self):
            print(f"""

{self.equipo_1}  {self.goles_equipo1}-{self.goles_equipo2}  {self.equipo_2}  

""")