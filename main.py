# program converting text to morse

import os
def clear(): os.system('cls')


morse_dict = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
}

restart = True

while restart:
    clear()
    print("********** TEXT TO MORSE CODE TRANSLATOR **********\n")

    user_input = input("Enter the text to be translated: ").lower()

    text_translated_to_morse = ""

    for letter in user_input:
        if letter != " ":
            text_translated_to_morse += f"{morse_dict[letter]} "
        else:
            text_translated_to_morse += " / "

    print(f"Your text in morse code: {text_translated_to_morse}\n\n")

    user_restart = input("Do you want to translate again? Y or N: ").upper()
    if user_restart != "Y":
        restart = False


