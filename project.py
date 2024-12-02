import random
import csv
import sys

def main():
    guess(get_word(),get_level(get_sys_argv()))

##get sys argument
def get_sys_argv():
    if len(sys.argv) == 2:
        level = sys.argv[1]
    else:
        level = "mid"
    return level

##how difficult game will be
def get_level(level):
    if level == "easy":
        return 0
    elif level == "mid":
        return 1
    elif level == "hard":
        return 2

##get all words and their meaning in dictionary
def get_all_words():
    ##to get acsses in get_word and get_help functions
    global words_and_expl
    words_and_expl ={}
    with open("project_words.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            word, expl = line
            words_and_expl[word] = expl

##get the word
def get_word():
    get_all_words()
    word = random.choice(list(words_and_expl.keys()))
    return word

def guess(word,level):
    word_list = list(word)
    show = ["_" for _ in range(6)]
    game = True
    number_of_tries = 0
    hint = True
    ##get hint in start for easy level
    if level == 0:
        print(f"Hint: {get_help(word)}")
    while game:
        if "_" in show and number_of_tries< 4:
            ##get hint one time in mid level
            if level == 1 and number_of_tries == 2 and hint:
                print(f"Hint: {get_help(word)}")
                hint = False
            print(*show, sep="")
            letter = (input("Letter: ")).lower()
            try:
                is_it_letter(letter)
                if letter in word:
                    for i in range(6):
                        if word_list[i] == letter:
                            show[i] = letter
                else:
                    number_of_tries +=1
                    get_deadman(number_of_tries)
            except ValueError:
                print("You should input one English letter")
        elif "_" not in show:
            print("You won! :)")
            game = False
        else:
            game = False
    print(f"The word: {word}")

def get_help(word):
    get_all_words()
    return words_and_expl[word]

def is_it_letter(letter):
    if len(letter) == 1 and letter in "qwertyuiopasdfghjklzxcvbnm":
        return True
    else:
        raise ValueError

## get an illustration in case of wrong letters
def get_deadman(number_of_tries):
    match number_of_tries:
        case 1:
            with open("deadman_0.txt") as file:
                print(file.read())
        case 2:
            with open("deadman_1.txt") as file:
                print(file.read())
        case 3:
            with open("deadman_2.txt") as file:
                print(file.read())
        case 4:
            with open("deadman_3.txt") as file:
                print(file.read())
                print("You lose it. :(")


if __name__ == "__main__":
    main()
