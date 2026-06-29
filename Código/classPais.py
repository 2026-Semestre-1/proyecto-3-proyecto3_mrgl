class País:
    """"
Nombre:init
entrada: recibe self,codigofifa,nombres,continentes,ranking_fifa
salida:guarda los valores
restricciones:debe de ser str
"""""
    def __init__(self,codigofifa,nombres,continentes,ranking_fifa):
        archivo_paises="paises.txt"
        self.codigo_fifa=codigofifa
        self.nombre=nombres
        self.continente=continentes
        self.ranking_fifa=ranking_fifa
        """"
Nombre:mostrar_datos
entrada: todos los self
salida:muestra los datos
restricciones:debe de ser str
"""""
    def mostrar_datos(self):
        codigo=self.codigo_fifa
        nombre=self.nombre
        continente=self.continente
        ranking=self.ranking_fifa
        print(f"""              
              Código del país:{codigo}
               Nombre del país:{nombre}
               Continente:{continente}
               Ranking de la FIFA:{ranking}
""")
        """"
Nombre:actualizar_datos
entrada:self,codigofifa,nombres,continentes,ranking_fifa
salida:actualiza los datos
restricciones:debe de ser str
"""""
    def actualizar_datos(self,codigofifa,nombres,continentes,ranking_fifa):
        self.codigo_fifa=codigofifa
        self.nombre=nombres
        self.continente=continentes
        self.ranking_fifa=ranking_fifa
