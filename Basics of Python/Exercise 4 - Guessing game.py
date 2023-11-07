print("""Guessing Game
try to guess the name - good luck!""")

name = "Matilda"
guess = None
guesses = 0

while guess != name:
    guess = input("Guess the name: ").capitalize()
    if guess == name:
        guesses += 1
        print("Congratulations!")
        print(f"Guesses: {guesses}")
    elif guesses == 5:
        guesses += 1
        print("Hint: HER name starts with the letter \"M\"\n")
    elif guesses == 10:
        guesses += 1
        print("Hint: \"M...a...\"\n")
    else:
        guesses += 1
        print("Guess again...")
        