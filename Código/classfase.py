from classPartido import partido

class fase:
    """"
Nombre:init
entrada: self y el nombre de la fase
salida:guarda los valores
restricciones:debe de ser lista y str
"""""
    def __init__(self,nombre_fase):
        self.nombre_fase=nombre_fase
        self.partidos=[]
        """"
Nombre: registrar_juego
entrada:self,equipo1,equipo2
salida: simula el encuentro entre los equipos
restricciones: debe de ser str
"""""
    def registrar_juego(self,equipo1,equipo2):
        encuentro=partido(equipo1,equipo2)
        encuentro.simular()
        self.partidos=self.partidos+[encuentro]
        """"
Nombre:jugar_fase
entrada: recibe los self
salida:juega las fases y muestra los clasificados
restricciones:debe de ser lista y str
"""""
    def jugar_fase(self):
        clasificados=[]
        for partido in self.partidos:
            ganador=partido.generar_ganador()
            if ganador ==None:
                ganador=partido.simular_penales()
            clasificados=clasificados+[ganador]
        return clasificados
    """"
Nombre: mostrar_juegos
entrada: recibe los self
salida: muestra los juegos
restricciones: debe de ser str
"""""
    def mostrar_juegos(self):
        for partidos in self.partidos:
            partidos.mostar_resultados()
            """"
Nombre:obtener_clasificados
entrada:todos los self
salida:obtiene los clasificados
restricciones:debe de ser lista y str
"""""
    def obtener_clasificados(self):
        clasificados=[]
        for partido in self.partidos:
            ganador=partido.generar_ganador()
            if ganador ==None:
                ganador=partido.simular_penales()
            clasificados=clasificados+[ganador]
        return clasificados