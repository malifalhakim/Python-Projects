import random

def get_word(word):
    list_word = list(word.upper())
    for i in range(len(list_word)):
        list_word[i] = "-"

    return list_word


def status(amount_lives,used_letter,list_word):
    print(f"You have {amount_lives} lives left and you have used these letter : {' '.join(used_letter)}")
    print(f"Current word : {' '.join(list_word)}")

def guess_letter(used_letter,word,list_word,amount_lives):
    user_guess = input("\nGuess a letter : ").upper()
    word = word.upper()

    if user_guess in used_letter :
        print("\nYou have alredy use that letter.Guess another letter again.")
    elif user_guess in word:
        for i in range(len(word)) :
            if word[i] == user_guess:
                list_word[i] = user_guess

        used_letter.append(user_guess)
    else:
        print(f"Your letter,{user_guess} is not in the word")
        used_letter.append(user_guess)
        amount_lives -= 1

    return list_word,amount_lives

##PROGRAM UTAMA

#Configurasi Awal
list_of_word = ['Kurisu','Tohsaka','Josee','Asuna','Ayaka','HuTao','Mayuri','Ilyasviel','Suzuha','Emilia','Hina','Vivy']
random_get_word_index = random.randint(0,len(list_of_word) - 1)
random_get_word = list_of_word[random_get_word_index]


word = random_get_word
list_word = get_word(word)
amount_lives = 6
used_letter = []

status(amount_lives,used_letter,list_word)

while '-' in list_word :
    list_word,amount_lives = guess_letter(used_letter,word,list_word,amount_lives)
    status(amount_lives,used_letter,list_word)

    if amount_lives == 0 :
        print("\nYou LOSE!")
        print(f"The word is {word}")
        break
else:
    print("\nYou WIN!")