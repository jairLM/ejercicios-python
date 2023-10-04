#Ejercicio 1. (1.5 puntos) Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

interruptor = True
while interruptor != False:
    print("""

        1.- opcion 1
        2.- opcion 2
        3.- opcion 3
        4.- salir


    """)
    opcion = int(input("Selecciona una opcion "))
    if(opcion == 4):
        interruptor = False


#Ejercicio 2. (1.5 puntos) Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

nNumeros = int(input("Cuantos numeros deseas mostrar: "))

index = 0
print("Numero primos: ")
while index <= nNumeros:
    if(index %2 != 0):
        print(index)

    index+=1

    
#Ejercicio 3. (1.5 puntos) Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.

pago = 10
index2 = 0
mesesPorPagar = 20

while index2 <= mesesPorPagar:

    pago = pago * 2 

    index2 += 1

    
    

print("El pago final sera de: ", pago)

