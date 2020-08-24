# Juego del ahorcado
# Data Analytics Bootcamp

# Llamado a las librería random y traigo la lista de palabras del archivo palabras
import random
from palabras import palabras_lst

# se escoge una palabra aleatoria de la lista y se devuelve en mayusculas


def get_word():
    word = random.choice(palabras_lst)
    return word.upper()

# Definición de la construcción de la palabra


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []  # se acumulan las letras adivinadas
    guessed_words = []  # lista de palabras adivinadas
    tries = 6
    print("El juego del ahorcado")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    # Ciclos
    while not guessed and tries > 0:
        # Inicio, ingresa una palabra.
        guess = input(
            "Ingresa una letra para adivinar la palabra o adivina la palabra completa: ").upper()
        # Opción 1: El user da letra
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                # Si la letra ya había sido elegida
                print("Ya habías usado esta letra", guess)
                # En caso de no pertencer a la palabra
            elif guess not in word:
                print(guess, " no es parte de la palabra.")
                tries -= 1  # bajamos los intentos en uno
                guessed_letters.append(guess)
            else:  # Si se acierta a la palabra. Como se van guardando y cambiando los espacios por letras
                print("¡Muy bien!,", guess, "esta en la palabra")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]  # Se determinan las posiciones de las letras
                for index in indices:
                    word_as_list[index] = guess
                # se juntan los espacios con las letras
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                    # Opción 2: Si se coloca la palabra directamente
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("¡Has adivinado la palabra!", guess)
            elif guess != word:
                print(guess, "Intenta de nuevo. No es la palabra :( ")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:  # Opción 3: en caso de no ingresar una letra
            print("No es una opción válida. Por favor, ingresa una letra del alfabeto")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:  # En caso de ganar
        print("¡Felicidades! Le has dado a la palabra.")
    else:  # En caso de perder
        print("Te acabaste las oportunidades aquí... como con ella </3. La palabra era " +
              word + ". ¡Hasta luego!")

# Función del display del ahorcado


def display_hangman(tries):
    stages = [  # Colgado (tries == 0)
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,  # cabeza, torso, brazos y Sin un pie (tries == 1)

        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,  # cabeza, torso y una mano. Sin dos pies (tries == 2)

        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,  # torso, cabeza y una mano (tries == 3)

        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,  # Torso y cabeza (tries == 4)

        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,  # Cabeza (tries == 5)

        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,  # Inicio (tries == 6)

        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

# Final para volver a intentarlo o terminar el juego


def main():
    word = get_word()
    play(word)
    while input("¿Quieres volver a intentalro? (S/N) ").upper() == "S":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
