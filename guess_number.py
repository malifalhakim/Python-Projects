import random
import os

os.system("cls")

print('GUESSING NUMBER GAME'.center(40))
print("\n")

def guess(limit_number):
    print(f"Guess the number between 1 and {limit_number}")
    secret_number = random.randint(1,limit_number)

    while True :
        guess_number = int(input("Guess the number: "))
        if guess_number == secret_number :
            print("Congratulations . You win !")
            break
        elif guess_number > secret_number :
            print("The number you choose is too high")
        else:
            print("The number you choose is too low")


limit_number = int(input("Put the limit number for the game : "))
guess(limit_number)