"""
Ejercicio 1. (2 puntos) Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.

Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.

mostrar(): Muestra los datos de la persona.

esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad

"""

class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    @property
    def getNombre(self):
        return self.nombre
    @property
    def getEdad(self):
        return self.edad
    @property
    def getDNI(self):
        return self.DNI  
    @property
    def mostrar(self):
        return "Nombre: " + self.nombre + " Edad: "+ str(self.edad) + " DNI: " + str(self.DNI)  
    
persona = Persona("Juan", 23, 1567)
datos = persona.mostrar
print(datos)

"""
Ejercicio 2. (2 puntos) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.

Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.

mostrar(): Muestra los datos de la cuenta.

ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.

retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

"""

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    @property
    def getTitular(self):
        return self.titular
    
    @property
    def retiro( monto):
        return titular.cantidad - monto
    @property
    def mostrar(self):
        return "Titular: " + self.titular + " Cantidad: "+ str(self.cantidad)   

titular = Cuenta("Juan", 25000)

print(titular.mostrar)

titular.retiro(500)
print(titular.mostrar)



        
