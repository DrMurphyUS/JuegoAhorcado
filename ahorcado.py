import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_estado(palabra, letras):
    return ' '.join([letra if letra in letras else '_' for letra in palabra])

def juego_ahorcado():
    limpiar_pantalla()
    palabra = input("Jugador 1, ingresa la palabra secreta: ").strip().lower()
    limpiar_pantalla()

    letras_adivinadas = set()
    intentos = 6

    print("¡Comienza el juego del ahorcado!")

    while intentos > 0:
        estado = mostrar_estado(palabra, letras_adivinadas)
        print(f"\nPalabra: {estado}")
        print(f"Intentos restantes: {intentos}")

        if "_" not in estado:
            print("\n¡Felicidades! Adivinaste la palabra.")
            return

        letra = input("Adivina una letra: ").strip().lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Ingresa solo una letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra.")
        elif letra in palabra:
            letras_adivinadas.add(letra)
            print("¡Correcto!")
        else:
            letras_adivinadas.add(letra)
            intentos -= 1
            print("Letra incorrecta.")

    print(f"\n¡Perdiste! La palabra era: {palabra}")

if __name__ == "__main__":
    juego_ahorcado()