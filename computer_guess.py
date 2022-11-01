import random
import os

os.system("cls")

def computer_guess(x):
    low = 1
    high = x
    while True:
        guess = random.randint(low,high)
        feedback = input(f"Is {guess} too hight(h),too low(l),or correct(c) ? ")
        if feedback == "h" :
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print("Correct!!!")
            break

computer_guess(1000)
        

