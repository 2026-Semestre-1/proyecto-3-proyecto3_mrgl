
from classJugador import jugador
from classEntrenador import Entrenador
from classPais import País



class seleccion(jugador,Entrenador,País):
    """"
Nombre:init
entrada: recibe self,codigo_equipo,pais,entrenador
salida: registra en self los valores de la funcion y diferentes valores no agregados
restricciones:debe de ser tipo lista,str y int
"""""
    def __init__(self,codigo_equipo,pais,entrenador):
           self.codigo=codigo_equipo
           self.pais=pais
           self.entrenador=entrenador
           self.jugadores=[]
           self.puntos=0
           self.diferencias_goles=0
           self.total_goles_favor=0
           self.total_goles_contra=0
           self.total_tarjetas_amarillas=0
           self.total_tarjetas_rojas=0
           self.fuerza_equipo=0
           """"
Nombre:mostrar_datos
entrada: recibe el self y el codigo
salida:muestra los valores de la seleccion
restricciones:debe de ser str
"""""
    def mostrar_datos(self):
        print(f"""
            Código de equipo:{self.codigo}
            País:{self.pais}
            Entrenador de la selección:{self.entrenador}
            Jugadores de la selección:{self.jugadores}
            Total de goles anotados:{self.total_goles_favor}
            Total de goles en contra:{self.total_goles_contra}
            Total_tarjetas
""")
        """"
Nombre:agregar_jugador
entrada: rcibe el self y jugador
salida:añade el jugador
restricciones:debe de ser str
"""""
    def agregar_jugador(self,jugador):
        if len(self.jugadores)>=23:
             print("Error:la selección ya tiene el máximo de 23 jugadores")
        else:
             self.jugadores=self.jugadores+[jugador]
             print(f"Jugador: {jugador} agregado")
             """"
Nombre:eliminar_jugador
entrada: recibe el dorsal y el self
salida:elimina el jugador
restricciones:
"""""     
    def eliminar_jugadores(self,dorsal):
        nueva_lista=[]
        for jugador in self.jugadores:
             if jugador.dorsal!=dorsal:
                  nueva_lista=nueva_lista+[jugador]
                  print(f"Jugador  {jugador} eliminado ")
                  """"
Nombre:asignar_entrenador
entrada: recibe el self y el entrenador
salida: muestra el entrenador
restricciones: debe de ser str
"""""
    def asignar_entrenador(self,entrenador):
         self.entrenador=entrenador
         print(f"Entrenador {entrenador} asignado ")
         """"
Nombre: registrar_resultado
entrada: recibe(self,goles_favor,goles_contra,tarjetas_am,tarjetas_roj
salida: añade los valores en resultados
restricciones: debe de ser int y str
"""""
    def registrar_resultado(self,goles_favor,goles_contra,tarjetas_am,tarjetas_roj):
         self.goles_favor=goles_favor
         self.goles_contra=goles_contra
         self.tarjetas_am=tarjetas_am
         self.tarjetas_roj=tarjetas_roj
         """"
Nombre: calcular_fuerza_equipo
entrada: recibe los diferentes valores de las diferentes funciones
salida: clacula la fuerza del euipo y lo guarda
restricciones: debe de ser str y int
"""""
    def calcular_fuerza_equipo(self):
         factor_entrenador=self.entrenador.experiencia_años*4
         if factor_entrenador>100:
              factor_entrenador=100
         factor_ranking=100-self.ranking_fifa

         #ordena por rango de mayor a menor puntaje
         orden_jugadores=self.jugadores[:]
         for i in range(len(orden_jugadores)-1):
              for j in range(len(orden_jugadores)-1-i):
                   if orden_jugadores[j].puntaje_individual< orden_jugadores[j+1].puntaje_individual:
                        temporal=orden_jugadores[j]
                        orden_jugadores[j]=orden_jugadores[j+1]
                        orden_jugadores[j+1]=temporal
         suma=0
         for k in range(11):
               suma+=orden_jugadores[k].puntaje_individual
         promedio_jugadores=suma/11
         fuerza_equipo=(promedio_jugadores*0.6)+(factor_entrenador*0.25)+(factor_ranking*0.15)
         return fuerza_equipo
         