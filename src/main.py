from persistencia.crear_bd import crear_tablas

from dominio.empleado import Empleado
from dominio.departamento import Departamento

from persistencia.empleado_dao import EmpleadoDAO
from persistencia.departamento_dao import DepartamentoDAO

crear_tablas()

departamento1 = Departamento(nombre="Recursos Humanos")
departamento2 = Departamento(nombre="Marketing")

DepartamentoDAO.insertar(departamento1)
DepartamentoDAO.insertar(departamento2)

empleado = Empleado(nombre="Ana Pérez", correo="ana@ecotech.cl", telefono="987654321", sueldo=1200, departamento=departamento1.nombre)
empleado2 = Empleado(nombre="Marcos López", correo="marcos@ecotech.cl", telefono="987654322", sueldo=1300, departamento=departamento2.nombre)

EmpleadoDAO.insertar(empleado)

print("Empleado 1: ", empleado.nombre, empleado.id, empleado.departamento)

EmpleadoDAO.insertar(empleado2)

print("Empleado 2: ", empleado2.nombre, empleado2.id, empleado2.departamento)

