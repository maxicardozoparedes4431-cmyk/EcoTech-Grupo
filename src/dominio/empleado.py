
class Empleado:
    """Clase que representa a un empleado"""

    def __init__(self, nombre:str, correo:str, telefono:str, sueldo:int, id=None, departamento=None):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.id = id
        self.sueldo = sueldo
        self.departamento = departamento

    def mostrardatos(self) -> str:
        return f"Nombre: {self.nombre}, Correo: {self.correo}, Teléfono: {self.telefono}, ID: {self.id}"

    def calcular_pago(self) -> int:
        return self.sueldo