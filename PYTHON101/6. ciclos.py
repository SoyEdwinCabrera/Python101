# Ciclo, iteracion, bucle

# While = mientras evalue a Verdadero se va ejecutar el codigo identado hasta que evalue a falso
'''
i = 0 
while i < 10: # normalmente se utilizan variables mas pequeñas como i de indice
    if i < 5:
        print("El número", i, "es menor a 5")
    else:
        print("El número", i, "es mayor o igual a 5")

    i += 1 # Esta es la forma de abreviar i = i + 1

print("Terminó la iteración")
'''

# for
'''
for x in range (1, 11): # en esta expresion el primer valor es inclusivo, y el segundo es exclusivo
    print(x)
'''
while True:
    print("Escribe la opción deseada")
    print("1: Saludar")
    print("2: Salir")

    respuesta = int(input())

    if respuesta == 1:
        print("Saludos terrícola!")
    elif respuesta == 2:
        break # Break es una función para salir de iteraciones cuando se cumple una condición

print("Terminando programa")

