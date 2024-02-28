# Funcniones Pre-definidas = print, type(), range(), input()

# Nosotros podemos definir funciones dependiendo la operacion que necesitemos

def saludar(nombre):
    print("Hola", nombre) # pass # Python espera que al asignar una funcion tenga al menos una linea de codigo. Pero utilizando pass para definir una funcion pero esta vacia

# Celsius a Fahrenheit: (C * 1.8) + 32
def convertir_a_Fahrenheit(c):
    return (c * 1.8) + 32

# saludar("Edwin") 
# saludar("Juan") 
# saludar("Sergio") 

print( convertir_a_Fahrenheit(10))
print( convertir_a_Fahrenheit(30))
print( convertir_a_Fahrenheit(80))
