import random

lista_palabras = ("python", 
                  "programacion", "desarrollo", "juego", "ahorcado", "computadora", "algoritmo" )

palabraS = list()

palabra_secreta = random.choice(lista_palabras)
intentos = len(palabra_secreta)

print("BIENVENIDO AL JUEGO DEL AHORCADO")
print(f"Tienes {intentos} vidas")

while intentos > 0:
    letra = input("ingresa una letra: ")

    if letra in palabra_secreta:
        palabraS.append(letra)
        print("PALABRA,","".join([1 if 1 in palabraS else "_" for 1 in palabra_secreta]))

    else:
        intentos -= 1
        print(f"Te quedan {intentos} vidas")