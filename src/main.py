from persistencia.crear_bd import crear_tablas

from dominio.empleado import Empleado
from dominio.departamento import Departamento

from persistencia.empleado_dao import EmpleadoDAO
from persistencia.departamento_dao import DepartamentoDAO

crear_tablas()

departamento1 = Departamento(nombre="Recursos Humanos")
departamento2 = Departamento(nombre="Marketing")

# DepartamentoDAO.insertar(departamento1)
# DepartamentoDAO.insertar(departamento2)

empleado = Empleado(nombre="Ana Pérez", correo="ana@ecotech.cl", departamento=departamento1.nombre)
empleado2 = Empleado(nombre="Marcos López", correo="marcos@ecotech.cl", departamento=departamento2.nombre)

empleado3 = Empleado(nombre="Maximiliano Cardozo", correo="Maximliano@ecotech.cl", departamento=departamento2.nombre)

EmpleadoDAO.insertar(empleado3)

# print("Empleado 1: ", empleado.nombre, empleado.id, empleado.departamento)

# EmpleadoDAO.insertar(empleado2)

# print("Empleado 2: ", empleado2.nombre, empleado2.id, empleado2.departamento)

encontrado = EmpleadoDAO.buscar_por_id(empleado.id)

print("Encontrado:", encontrado)
print("Listado:")

for item in EmpleadoDAO.listar():
    print(item.mostrardatos())
