class Persona:
    """"
Nombre:
entrada:
salida:
restricciones:
"""""
    def __init__(self,nombre,apellido,fecha_nacimiento,nacionalidad):
        self.nombre=nombre
        self.apellido=apellido
        self.fecha_nacimiento=fecha_nacimiento
        self.nacionalidad=nacionalidad
        if not isinstance(nombre,str):
            return "Error:el nombre tiene que ser en formato de letras"
        elif not isinstance(apellido,str):
            return "Error:El apellido tiene que ser en formato de letras"
        elif not isinstance(fecha_nacimiento,str):
            return "Error:La fecha de nacimiento debe de ser en formato de letras"
        elif not isinstance(nacionalidad,str):
            return "Error:La nacionalidad debe de ser de formato de letras"
        """"
Nombre:
entrada:
salida:
restricciones:
"""""
    def mostrar(self):
        print(f"""
Nombre de la persona:{self.nombre}
Apellido de la persona:{self.apellido}
nacionalidad:{self.nacionalidad}
Fecha de nacimiento:{self.fecha_nacimiento}
""")