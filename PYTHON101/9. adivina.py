import random

def tirar_dados():
    return random.randint(2, 12)

def pedir_respuesta():
    print("Ingresa tu prediccion")
    print("1.Par")
    print("2. Impar")
    print("3. Salir del juego")

    return int(input())
      
def imprimir_resultado(numero, prediccion):
    # not, % modulo
    # Saber si un numero es par o impar
    # Dividir entre 2 y si el remanente es 0, es per. Si es 1, es impar
    # Resultado = 5/2: Resultado seria 2 con remante 1
    # Resultado = 6/2: Resultado es 3, con remanente 0
    es_par = numero % 2 == 0 
    # es_par, prediccion = 1: Gane
    # no es_par, prediccion = 2, Gane
    # Perdi
    if es_par and prediccion == 1:
        print("Ganaste! Número de los dados:", numero)
    elif not es_par and prediccion == 2:
        print("Ganaste! Número de los dados:", numero)
    else:
        print("Perdiste! Número de los dados:", numero)
                        
while True:
    numero = tirar_dados()
    prediccion = pedir_respuesta()
    if prediccion == 3:
        break
    imprimir_resultado(numero, prediccion)

print("Gracias por jugar")