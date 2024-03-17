from random import choice
list_of_words = ['stick','lens','smart','mouth','spray', 'kind']
def start_game(list_of_words):
    wrong_letters = []
    a_lives = 6
    word = choice(list_of_words)
    Dashed_word = ''.join(['_ ' for i in range(len(word))])
    l = ask_a_letter(a_lives,wrong_letters,Dashed_word)
    l = validate_letter(l,wrong_letters,Dashed_word)
    while True:
        if check_letter(l,word):
            Dashed_word = change_dashed_word(Dashed_word,word,l)
            if '_' not in Dashed_word:
                result= f'You won! The word was {word}.'
                break
            else:
                l = ask_a_letter(a_lives,wrong_letters,Dashed_word)
                l = validate_letter(l,wrong_letters,Dashed_word)
                continue
        else:
            if l not in wrong_letters:
                wrong_letters.append(l)
            a_lives -=1
            if a_lives!=0:
                l = ask_a_letter(a_lives,wrong_letters,Dashed_word)
                l = validate_letter(l,wrong_letters,Dashed_word)
                continue
            else:
                result = f'Game Over! You do not have more lives. The word was {word}'
                break
    return result
        
             
def change_dashed_word(Dashed_word: str,word,l):    
    Dashed_word = Dashed_word.split()
    for i in range(len(word)):
        if l==word[i]:
            Dashed_word[i]=l
    Dashed_word = ' '.join(Dashed_word)
    return Dashed_word
def ask_a_letter(a_lives,wrong_letters,Dashed_word):
    print("\n" + "*"*20 + "\n")
    return input(f'wrong letters: {wrong_letters}.\nYou have {a_lives} lives remaining.\n Please enter a letter: {Dashed_word}')
def validate_letter(l,wrong_letters,Dashed_word):
    while not (len(l)==1 and l.isalpha()):
        l = ask_a_letter(wrong_letters,Dashed_word)
    return l
def check_letter(l,word):
    if l in word:
        return True
    return False

start_game(list_of_words)
