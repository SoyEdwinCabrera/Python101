from datetime import datetime

print("*************************************************************")
print("*********************** BIENVENIDO A  ***********************")
print("******************  LA TIENDA DE MASCOTAS  ******************")
print("*************************************************************")

inventario = {
    "perros": 10,
    "gatos": 8,
    "pajaros": 25,
    "iguanas": 2
}

animales_totales = 0
for val in inventario.values():
    animales_totales += val

print("Por favor ingresa tu nombre")
nombre = input()
print("Por favor excribe tu apellido")
apellido = input()

# Concatenacion
nombre_completo = nombre + " " + apellido

print("Gracias por visitarnos,", nombre_completo)

compras = []

def mostrar_menu():
    print("")
    print("===========================================")
    print("Selecciona la opción que deseas:")
    print("1: Conocer cuántos animales tiene la tienda")
    print("2: Comprar un animal")
    print("3: Mostar compras")
    print("4: Salir de la tienda")

def mostrar_inventario():
    print("**** INVENTARIO ****")
    for llave, valor in inventario.items():
        print(f"    {llave}: {valor}")
    print("En total tenemos", animales_totales, "animales")

def comprar_animal():
    carrito = []
    while True:
        print("Qué animal deseas comprar? Solo puedes elegir 1 de cada especie")
        print("Escribe F para terminar la lista, o V para ver tu carrito")
        animal = input()

        if animal == "F": break

        if animal == "V":
            print(f"Tu carrito de compras contiene {carrito}")
            continue
        if animal not in inventario:
            print(f"Lo sentimos, no contamos con el animal {animal}")
        elif inventario[animal] == 0:
            print(f"Lo sentimos, no tenemos en existencia el animal {animal}")
        elif animal not in carrito:
            carrito.append(animal)
        else:
            print("Ese animal ya se encuentra en tu carrito")
        #print("has comprado un", animal)

    print("El contenido de tu carrito es")
    for animal in carrito:
        print(" ", animal)
        inventario[animal] -= 1

    # Agregar esta compra al carrito de compras
    fecha = datetime.now()
    compras.append( (nombre, carrito, fecha))
    # Compras tiene longitud 1 (solo tengo 1 compra)
        # Contiene una tupla: Nombre, Carrito, Fecha

def mostrar_compras():
    print(" ")
    print("********  COMPRAS REALIZADAS  ********")  
    for compra in compras: # Compra = tupla que contiene NOMBRE, CARRITO, FECHA
        print(f"  {compra[0]} compró {compra[1]} en {compra[2]}")

while True:    
    mostrar_menu()
    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comprar_animal()
    elif respuesta == 3:
        mostrar_compras()
    elif respuesta == 4:
        print("Gracias por tu visita")
        break
