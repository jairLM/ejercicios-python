#Ejercicio 1
numeros = [1,2,3,4,5,6,7,8,9,10]
for elementos in numeros:
    print(f'El cuadro de ', elementos, ' es ', pow(elementos, 2), ' y el cubo es ', pow(elementos, 3))


#Ejercicio 2

cadenas =[]
contador = 0
while(contador < 5):
    valores = str(input('Ingresa un string: '))
    cadenas.append(valores)
    contador+=1

print(cadenas[::-1])


#Ejercicio 3
contadorCalif = 1
calif = {}
print(calif)
while(contadorCalif <= 10):
    calif[f'calif{contadorCalif}'] = float(input(f'Ingrese la calificacion {contadorCalif}: '))
    contadorCalif+=1


def promedio():
    sumatoria = 0
    for i in calif:        
        sumatoria = sumatoria + calif[i]
        return sumatoria


        
        

     
print(promedio())
