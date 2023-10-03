#Ejercicio 1. (2 puntos) Programa que imprima si el número es positivo o negativo.
numero = float(input("Escriba un numero: "))
if(numero > 0):
    print("Es un número positivo")
elif(numero < 0):
    print("El número es negativo")
else: print("Es nulo")

#Ejercicio 2. (2 puntos) Programa que imprima si el número ingresado esta en el rango de 1 a 7.

numero2 = float(input("Escriba un numero: "))
if(numero <= 1 and numero >= 7):
    print("Dentro del ranfo de 1 a 7")
else: print("Fuera del rango")