# Juego del ahorcado
# Data Analytics Bootcamp


import random
from palabras import palabras_lst


def get_word():
    word = random.choice(palabras_lst)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("El juego del ahoracado")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Ingresa una letra para adivinar la palabra: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Una letra buena", guess)
            elif guess not in word:
                print(guess, " no es parte de la palabra.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("¡Muy bien!,", guess, "esta en la palabra")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("¡Has adivinado la palabra!", guess)
            elif guess != word:
                print(guess, "No es la palabra :( ")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("No has adivinado")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("¡Felicidades! Le has dado a la palabra, crack.")
    else:
        print("Te acabaste las oportunidades aquí... como con ella </3. La palabra era " +
              word + ". ¡Hasta luego!")


def display_hangman(tries):
    stages = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,

        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,

        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,

        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,

        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,

        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,

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


def main():
    word = get_word()
    play(word)
    while input("¿Quieres volver a intentalro? (S/N) ").upper() == "S":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
