from random_word import RandomWords
from randomwordfr import RandomWordFr
import os


def draw(false):
    try:
        with open(f'drawings/{false}.txt', 'r') as file:
            drawing = file.read()
    except FileNotFoundError:
        drawing = """




                       """
    return drawing


def english(word, guess):
    for _ in range(100):
        os.system("clear")
        print(f'{" ".join(guess)}                     uncorrect letters: {false}')
        print(draw(len(false)))
        if word == "".join(guess):
            print("Congrats! You win 🎉")
            exit()
        if len(false) == 9:
            break
        letter = input("Enter a letter: ")
        IN = False
        for index, value in enumerate(word):
            if letter == value:
                guess[index] = letter
                IN = True
        if IN is False and letter not in false:
            false.append(letter)
    print("You lose! The word was", word)


def french(word, definition, guess):
    for _ in range(100):
        os.system("clear")
        print(f'{" ".join(guess)}                     lettres incorrectes: {false}')
        print(draw(len(false)))
        if word == "".join(guess):
            print("Félicitations! Vous avez gagné 🎉")
            exit()
        if len(false) == 9:
            break
        letter = input("Entrez une lettre: ")
        IN = False
        for index, value in enumerate(word):
            if letter == value:
                guess[index] = letter
                IN = True
        if IN is False and letter not in false:
            false.append(letter)
    print("Vous avez perdu! Le mot était", word)
    print(f"Définition: {definition}")


os.system("clear")
false = []

match input("Select a language\n 1. English\n 2. French\n"):
    case "1":
        word = RandomWords().get_random_word()
        guess = ["_"]*len(word)
        english(word, guess)
    case "2":
        p = RandomWordFr().get()
        word = p["word"].lower()
        definition = p["definition"]
        guess = ["_"]*len(word)
        french(word, definition, guess)
