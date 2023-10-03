class Empleado:    
    def __init__(self, nombre, edad, numEmpleado, sueldo):
        self.__nombre = str(nombre)
        self.__edad = int(edad)
        self.__numEmpleado = str(numEmpleado)
        self.__sueldo = float(sueldo)
    
    @property
    def getNombre (self):
        return self.__nombre
    @getNombre.setter
    def setNombre(self, nombre_new):
        self.nombre = nombre_new


    def calcSueldo(self, descuento, bono):
        return self.sueldo - descuento * bono

    def mostrarInfo(self):
        return "El empleado " + self.nombre, " tiene ", self.edad," con numero de empleado ", self.numEmpleado," tiene un sueldo de ", self.sueldo
    
#subclase

class Gerente(Empleado):
    def __init__(self, nombre, edad, numEmpleado, sueldo):
        super().__init__(nombre, edad, numEmpleado, sueldo)
        self.sucursal = sueldo
        
    def mostrarInfo(self):
        return "El empleado " + self.nombre, " tiene ", self.edad," con numero de empleado ", self.numEmpleado," tiene un sueldo de ", self.sueldo, " sucursal ", self.sucursal







#=====principal
#instanciando el objeto empleado1
empleado1 = Empleado('Jair Murillo', 23, 'A45', 30000)


print(empleado1.getNombre)

empleado1.nombre = "Luis"
print(empleado1.nombre)

#====

gerente1 = Gerente("Juan", 43, 'B43', 100000)

print(gerente1.mostrarInfo())