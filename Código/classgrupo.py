from classPartido import partido

class grupo:
    """"
Nombre:init
entrada:el nombre y el grupo
salida:muestra los self
restricciones:debe de ser lista y str
"""""
    def __init__(self,nombre_grupo):
        self.nombre_grupo=nombre_grupo
        self.equipos=[]
        self.partidos=[]
        """"
Nombre:agregar_equipos
entrada:seleccion
salida: muestra las selecciones
restricciones:el valor seleccion debe de ser str
"""""
    def agregar_equipo(self,seleccion):
        self.equipos=self.equipos+[seleccion]
        if len(self.equipos)>4:
            print("Error: se llego al máximo de equipos por grupo")
        else:
            print("Equipo agregado")
            """"
Nombre:jugar_partidos
entrada: recibe el self y valores de otras funciones
salida:juega los partidos
restricciones:debe de ser str y int
"""""
    def jugar_partidos(self):
        for i in range(len(self.equipos)-1):
            for j in range(i+1,len(self.equipos)):
                encuentro=partido(self.equipos[i],self.equipos[j])
                encuentro.simular()
                self.partidos=self.partidos+[encuentro]
                """"
Nombre:clacular_tabla
entrada:self y valores de otras funciones
salida:calcula la tabla con las diferencias de goles
restricciones:debe de ser int
"""""
    def calcular_tabla(self):

        for equipo in self.equipos:
            equipo.puntos=0
            equipo.diferencia_goles=0
        for partido in self.partidos:
            equipo_1=partido.goles_equipo1
            equipo_2=partido.goles_equipo2
        if equipo_1<equipo_2:
            partido.equipo_1.puntos=+3
        elif equipo_2>equipo_1:
            partido.equipo_2.puntos+=3
        else:
            partido.equipo_1.puntos+=1
            partido.equipo_2.puntos+=1
        partido.equipo_1.diferencias_goles+=equipo_1-equipo_2
        partido.equipo_2.diferencias_goles+=equipo_2-equipo_1
        """"
Nombre:obtener_calificados
entrada:recibe el self y otros valores de otras funciones
salida:obtiene los clasificados
restricciones:debe de ser str y lista
"""""
    def obtener_calificados(self):
        equipos_ordenados=self.equipos[:]
        for i in range(len( equipos_ordenados)-1):
              for j in range(len( equipos_ordenados)-1-i):
                   if  equipos_ordenados[j].puntaje_individual<  equipos_ordenados[j+1].puntaje_individual:
                        temporal= equipos_ordenados[j]
                        equipos_ordenados[j]= equipos_ordenados[j+1]
                        equipos_ordenados[j+1]=temporal
                   return [equipos_ordenados[0],equipos_ordenados[1]]
              """"
Nombre:mostrar_tabla
entrada:self y otros valores de otras funciones
salida:muestra las diferencias de goles y puntos
restricciones:debe de ser int y str
"""""
    def mostrar_tabla(self):
        print(f"Tabla del grupo {self.nombre_grupo}")
        print("Tabla - Puntos - Diferencias de goles")
        for equipo in self.equipos:
         print(f"{equipo.pais} - {equipo.puntos} - {equipo.diferencias_goles}")