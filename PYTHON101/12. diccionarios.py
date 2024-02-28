# Son listas de elementos llave:valor
# En otros lenguajes = Arreglos asociativos

persona = {"nombre": "Edwin",
           "edad": 800,
           "apellido": "Cabrera"}

persona["apodo"] = "Ringa Tech"

print (persona.keys(    ))

print (persona.values(    ))

print (persona.items( ))

print("****************************")

for key in persona.keys():
    print(key)

print("****************************")

for values in persona.values():
    print(values)

print("****************************")

for items in persona.items():
    print(items)

print("****************************")

for key, value in persona.items(): # al utilizar items el sistema regresa tuplas
    print(f"La llave {key} tiene el valor {value}")

print("****************************")

print ("direccion" in persona) # Se puede utilizar para validar

print ("apodo" in persona)
