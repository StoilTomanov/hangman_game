import random


def play_hangman():
    list_of_words = [
        "apple",
        "car",
        "dog",
        "iron man",
        "camaro",
        "smartphone",
        "laptop",
        "processor",
        "water",
        "sky",
    ]
    has_user_won = False
    random_word = random.choice(list_of_words)
    random_word.join([letter.replace(letter, "_") for letter in random_word])
    print(random_word)
    allowed_attempts = 5
    while allowed_attempts > 0:
        user_choice = input("Guess a word: ")
        if random_word == user_choice:
            print("---")
            print("You win!!!")
            has_user_won = True
            break
        else:
            print("---")
            print("Don't give up. Try again :)")
            allowed_attempts -= 1
            continue
    print("---")
    if not has_user_won:
        print("You lost the battle, but not the war. Give it another go :)")
        print("The word was: ", random_word)


play_hangman()
