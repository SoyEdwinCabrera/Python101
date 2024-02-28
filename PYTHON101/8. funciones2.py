# random 
import random

#randint(min, max)

resultado = random.randint(1, 100)
print (resultado)

# Se puede asignar un valor por defecto dentro de la funcion, pero si ingreso algun argumento lo omite

def saludar_y_sumar(nombre, num1, num2 = 0):
    print ("Saludos", nombre)
    print("Resultado de la suma", num1+num2)

saludar_y_sumar("Edwin", 15, 85)
saludar_y_sumar("Edwin", 18, )
saludar_y_sumar("Edwin", 325, 4000)

