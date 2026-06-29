from classgrupo import grupo
from classfase import fase

class Mundial:
    """"
Nombre: init
entrada: recibe el self,nombre,año
salida: muestra todos los valores guardados
restricciones: debe de ser list,str y int
"""""
    def __init__(self,nombre,año):
        self.nombre=nombre
        self.año=año
        self.paises=[]
        self.selecciones=[]
        self.grupos=[]
        self.fases=[]
        self.campeon=None
        """"
Nombre: registrar_pais
entrada: rcibe el self,pais
salida: muetra los países registardos
restricciones:debe de ser str
"""""
    def registrar_pais(self,pais):
        self.paises=self.paises+[pais]
        print(f"País {pais} registrado ")
        """"
Nombre: registrar_seleccion
entrada: self y seleccion
salida: muestra la seleccion
restricciones: debe de ser str
"""""
    def registrar_seleccion(self,seleccion):
        self.selecciones=self.selecciones+[seleccion]
        print(f"Seleccion {seleccion} registrada")

        """"
Nombre:validar_seleccion
entrada: self y seleccion
salida:valida que tengan los minimos jugadores y los maximos
restricciones:debe de ser str
"""""


    def validar_seleccion(self,seleccion):
        if len(seleccion.jugadores)<11:
            print(f"error:la seleccion {seleccion.pais} tiene menos de 11 jugadores ")

        elif len(seleccion.jugadores)>20:
            print(f"Error:la seleccion {seleccion.pais} tiene más de 20 jugadores")
            return False
        else:
            return True
        """"
Nombre: crear_grupos
entrada:self cantidad_grupos
salida: muestra los grupos
restricciones:debe de ser str
"""""
    def crear_grupos(self,cantidad_grupos):
       
        if cantidad_grupos>4:
            print("Error:cantidad de grupos excedido")
            return
        self.grupos=[]
        numero_grupo=1
        for i in range(cantidad_grupos):
            Grupo=grupo(f"Grupo {numero_grupo}")
            for j in range(0,len(self.selecciones),cantidad_grupos):
                Grupo.agregar_equipo(self.selecciones[j])
            self.grupos=self.grupos+[Grupo]
            print(f"Equipos en grupo:{Grupo.equipos}")
            numero_grupo+=1
            """"
Nombre:jugar_fase_grupos
entrada: los valores de self
salida:muestra las fase de los grupos
restricciones:debe de ser str y list
"""""
    def jugar_fase_grupos(self):
        for Grupo in self.grupos:
            grupo.jugar_partidos()
            grupo.calcular_tabla()
        clasificados=[]
        for Grupos in self.grupos:
            dos_mejores=grupo.obtener_calificados()
            clasificados=clasificados+dos_mejores
        return clasificados
    """"
Nombre:armar_fase_eleminatoria
entrada: recibe self,nombre_fase,clasificados
salida: arma la fase de eliminacion
restricciones:debe de ser str
"""""
    def armar_fase_eleminatoria(self,nombre_fase,clasificados):
        Fase=fase(nombre_fase)
        for i in range(0,len(clasificados),2):
            fase.registrar_juego(clasificados[i],clasificados[i+1])
        self.fases=self.fases+[Fase]
        return Fase
    """"
Nombre:jugar_fase_eliminatoria
entrada: recibe los self
salida:juega las fases
restricciones:debe de ser str
"""""
    def jugar_fase_eliminatoria(self):
        clasificados=fase.jugar_fase()
        return clasificados
    """"
Nombre:determinar_campeon
entrada:recibe todos los self
salida:arma las fases y las juega
restricciones: debe deser string y list
"""""
    def determinar_campeon(self):
        clasificados=[]
        for Grupo in self.grupos:
            dos_mejores=grupo.obtener_calificados()
            clasificados=clasificados+dos_mejores

        Fase=self.armar_fase_eleminatoria("Dieciseisavos",clasificados)
        clasificados=self.jugar_fase_eliminatoria(Fase)

        Fase=self.armar_fase_eleminatoria("Octavos",clasificados)
        clasificados=self.jugar_fase_eliminatoria(Fase)

        Fase=self.armar_fase_eleminatoria("Cuartos",clasificados)
        clasificados=self.jugar_fase_eliminatoria(Fase)

        Fase=self.armar_fase_eleminatoria("Semifinal",clasificados)
        clasificados=self.jugar_fase_eliminatoria(Fase)

        Fase=self.armar_fase_eleminatoria("Final",clasificados)
        clasificados=self.jugar_fase_eliminatoria(Fase)

        self.campeon=clasificados[0]
        print(f"campeon:{self.campeon}")
        """"
Nombre:mostrar_tabla_general
entrada:recibe todos los self
salida: muestra las tablas de los equipos
restricciones: debe de ser str
"""""
    def mostrar_tabla_general(self):
        for Grupo in self.grupos:
            Grupo.mostrar_tabla()
    
    """""
nombre:generar_reporte
entrada:
salida:
restrcciones

"""

    def generar_reporte(self):
        print()