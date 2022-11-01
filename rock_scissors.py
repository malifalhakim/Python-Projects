import random

input_check = False

while not input_check:
    user_choice = input("What is your choice ( 'r' for rock , 's' for scissors , and 'p' for paper)? ")
    if user_choice == 'r' or user_choice == 's' or user_choice == 'p':
        input_check = True

com_choice = random.choices(['r','s','p'])

if user_choice == 'r' :
    if com_choice == 'r':
        print("Draw")
    elif com_choice == 's':
        print("Win")
    else :
        print("Lose")
elif user_choice == 's':
    if com_choice == 'r':
        print("Lose")
    elif com_choice == 's':
        print("Draw")
    else :
        print("Win")
else:
    if com_choice == 'r':
        print("Win")
    elif com_choice == 's':
        print("Lose")
    else:
        print("Draw")
