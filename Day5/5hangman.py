from random import choice
list_of_words = ['stick','lens','smart','mouth','spray', 'kind']
def start_game(list_of_words):
    wrong_letters= []
    print('Game started...')
    s_word =secret_word(list_of_words)
    print(f'You have to guess a word in 6 trys.word has {len(s_word)} letters.')
    a_try = 1
    modified_word = ''
    for x in range(len(s_word)):
        modified_word += '_'
    letter,a_try = get_input(a_try,modified_word,wrong_letters)
    return verify_letter(a_try,s_word,letter,modified_word,wrong_letters)

def secret_word(list_of_words):
    secret_word = choice(list_of_words)
    return secret_word
def get_input(a_try,modified_word,wrong_letters):  
    print(wrong_letters)
    letter = input(f'Guess a letter of word: {modified_word}')
    letter = letter.lower()
    if a_try<7:
        while letter not in 'abcdefghijklmnopqrstuvwxyz':
            print('You have not entered letter, please enter letter to guess word.')
            print(wrong_letters)
            letter = input(f'Guess a letter of word: {modified_word}')
        else:
            print(wrong_letters)
        a_try +=1
        return letter, a_try
    else:
        return 'Game Over...', a_try
    

def verify_letter(a_try,secret_word,letter,modified_word,wrong_letters):
    if letter == 'Game Over...':
        return 'Game Over...'
    print(0)
    if letter in secret_word:
        print('1',a_try)
        if letter in modified_word:
            print('You already guessed this letter.')
            letter,a_try =get_input(a_try,modified_word,wrong_letters)
            return verify_letter(a_try,secret_word,letter,modified_word,wrong_letters)
        i = secret_word.index(letter)
        temp_word = ''
        for x in range(len(modified_word)):
            print(x,i)
            if x == i:
                temp_word += letter     
            else:
                temp_word += modified_word[x]
        modified_word = temp_word
        if modified_word == secret_word:
            print(3,a_try)
            return f'You won! word is {secret_word}'
        else:
            print(4,a_try)
            letter, a_try =get_input(a_try,modified_word,wrong_letters)
            return verify_letter(a_try,secret_word,letter,modified_word,wrong_letters)
    else:
        print(2, a_try)
        wrong_letters.append(letter)
        letter,a_try =get_input(a_try,modified_word,wrong_letters)
        return verify_letter(a_try,secret_word,letter,modified_word,wrong_letters)
start_game(list_of_words)