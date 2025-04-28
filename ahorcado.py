import os

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_estado(palabra, letras_adivinadas):
    """Retorna la palabra con las letras adivinadas y guiones bajos para las no adivinadas."""
    return ' '.join(letra if letra in letras_adivinadas else '_' for letra in palabra)

def solicitar_letra(letras_adivinadas):
    """Solicita al jugador una letra válida que no haya sido usada antes."""
    while True:
        letra = input("Adivina una letra: ").strip().lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Debes ingresar solo una letra del alfabeto.")
        elif letra in letras_adivinadas:
            print("Ya adivinaste esa letra.")
        else:
            return letra

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
            break

        letra = solicitar_letra(letras_adivinadas)

        if letra in palabra:
            letras_adivinadas.add(letra)
            print("¡Correcto!")
        else:
            letras_adivinadas.add(letra)
            intentos -= 1
            print("Letra incorrecta.")

    if intentos == 0:
        print(f"\n¡Perdiste! La palabra era: {palabra}")

if __name__ == "__main__":
    juego_ahorcado()