print("Escribe tu nombre:")
nombre = input()
print("Escribe tu edad:")
edad = int(input())


# elif
# Operadores lógicos
# and (y) / or (o)
# and: Todas las expresiones son True
# or: Con que una de las expresiones sea True
# > < >= <=

''' Ejenplo operador and

if nombre == "Edwin" and edad > 30:
    print("Saludos Edwin, eres un adulto")
elif nombre == "Edwin" and edad <= 30:
    print("Saludos Edwin, eres un joven")
else:
    print("Saludos")

'''
# Ejemplo de AND y OR
if nombre == "Edwin" or nombre == "Santiago":
    print("Me gusta tu nombre")
else: 
    print("Que nombre tan extraño")