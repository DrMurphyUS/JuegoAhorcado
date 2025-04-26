import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_estado(palabra_secreta, letras_adivinadas):
    estado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado += letra + " "
        else:
            estado += "_ "
    return estado.strip()

def juego_ahorcado():
    limpiar_pantalla()
    palabra_secreta = input("Jugador 1, ingresa la palabra secreta: ").lower()
    limpiar_pantalla()

    letras_adivinadas = []
    intentos_restantes = 6

    print("¡Comienza el juego del ahorcado!")
    
    while intentos_restantes > 0:
        estado_actual = mostrar_estado(palabra_secreta, letras_adivinadas)
        print("\nPalabra: " + estado_actual)
        print(f"Intentos restantes: {intentos_restantes}")
        
        if "_" not in estado_actual:
            print("\n¡Felicidades! Has adivinado la palabra.")
            break

        intento = input("Adivina una letra: ").lower()

        if intento in letras_adivinadas:
            print("Ya has adivinado esa letra.")
        elif intento in palabra_secreta:
            letras_adivinadas.append(intento)
            print("¡Bien hecho!")
        else:
            letras_adivinadas.append(intento)
            intentos_restantes -= 1
            print("Letra incorrecta.")

    else:
        print(f"\n¡Perdiste! La palabra secreta era: {palabra_secreta}")

juego_ahorcado()