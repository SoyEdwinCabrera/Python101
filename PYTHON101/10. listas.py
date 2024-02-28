# en una lista es una estructura de datos que permite tener multiples datos involucrados en una sola variable

nombres = ["Edwin", "Juan", "Pedro"]
# La lista comienza a enumerar los elementos desde la posicion 0, de le conocen como indices
# 0 = Edwin, 1 = Juan, 2 = Pedro
# Diferenciar los indices que es la posición del elemento iniciando desde cero, de la longitud que son la cantidad de element
print(nombres[2])
nombres[1] = "Santiago" # Las listas son modificables
print(len(nombres))
print(type(nombres))
nombres.append("Jorge")
print(nombres)
nombres.remove("Santiago")
print(nombres)
del nombres[1] # En esta expresion eliminamos conociendo el indice
print(nombres)

print("Edwin" in nombres) # La expresión busca un argumento dentro de la lista, regresando un valor lógico

print("-----------------------------------")

nombres1 = ["Edwin", "Juan", "Pedro", "Santiago", "Jorge"]
print(nombres1)

for i, nombre in enumerate(nombres1):
    print("Se inscribio a la lista:", i, nombre)


print("Bienvenidos a la fiesta", nombres1[:3]) # si omitimos el indice, python entiende que queremos desde el inicio de las lista ES EXCLUSIVO
print("Lo sentimos", nombres1[3:]) # Lo mismo pasa en este caso porque ES INCLUSIVO

#f-strings formato elegante

for i, nombre in enumerate(nombres1):
    print( f"Se incribio {nombre} en la lista con el índice {i}") # con las llaves permite referenciar variables
    

