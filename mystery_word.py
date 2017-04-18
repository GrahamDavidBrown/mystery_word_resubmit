import random


def mystery_word():
    win = False
    dictionary = open("/usr/share/dict/words")
    dictionary_list = []
    short_words = []
    med_words = []
    long_words = []
    secret_blanks = []
    letters_in = []
    dictionary_list = dictionary.readlines()
    difficulty = 4
    correct_guesses = 0
    bad_guesses = 0
    for word in dictionary_list:
        if len(word) <= 4:
            short_words.append(word)
        if len(word) > 4 and len(word) < 8:
            med_words.append(word)
        else:
            long_words.append(word)
    while difficulty > 3 or difficulty < 1:
        try:
            difficulty = int(input("Easy(1), Medium(2), Hard(3): "))
        except:
            pass
    if difficulty == 1:
        secret_word = random.choice(short_words).lower()
        secret_word = secret_word[0:-1]
    elif difficulty == 2:
        secret_word = random.choice(med_words).lower()
        secret_word = secret_word[0:-1]
    elif difficulty == 3:
        secret_word = random.choice(long_words).lower()
        secret_word = secret_word[0:-1]
    for letter in secret_word:
        secret_blanks.append('_')
    # print(secret_word)
    while bad_guesses < 5:
        print(secret_word)
        user_in = input('guess a letter: ')
        count = 0
        good_guess = False
        curr_letter = 'picklepuss'
        for letter in secret_word:
            if user_in == letter and letter != "" and letter not in letters_in:
                secret_blanks[count] = letter
                correct_guesses += 1
                good_guess = True
                curr_letter = letter
            count += 1
        curr_letter = user_in
        if(curr_letter not in letters_in and good_guess):
            letters_in += curr_letter
        if not good_guess and curr_letter != '' and curr_letter not in letters_in:
            bad_guesses += 1
        for letter in secret_blanks:
            print(letter + ' ', end='')
        print('\n')
        if correct_guesses == len(secret_word):
            win = True
            break
    if win:
        print('you win!')
    else:
        print('you lose, the word was: ' + secret_word)



mystery_word()
