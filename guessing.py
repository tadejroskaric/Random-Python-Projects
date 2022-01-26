import random

number = random.randint(1, 10)

print("Hello, what's your name? ")
name = input()
print("Okay,", name, "guess a number between 1 and 10: ")

i = 1

while i < 6:
    guess = int(input("Your guess: "))
    if guess == number:
        print("You guessed the number in", i, "tries!")
        break
    elif guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")
    i = i+1
    if i == 6:
        print("You did not guess the number. It was", number, ":(.")
