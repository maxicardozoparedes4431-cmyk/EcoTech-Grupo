
class Empleado:
    """Clase que representa a un empleado"""

    def __init__(self, nombre:str, correo:str, departamento:str , id=None):
        self.nombre = nombre
        self.correo = correo
        self.id = id
        self.departamento = departamento

    def mostrardatos(self) -> str:
        return f"Nombre: {self.nombre}, Correo: {self.correo}, Departamento: {self.departamento}, ID: {self.id}"