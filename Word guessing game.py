import random

def get_input():
    while True:
        user_input = input('Enter Your guess: ')
        if user_input.isalpha():
            return user_input
        print('Your input was not correct. Please enter again.')

def get_input_from_list(words):
    user_input = get_input()

    while user_input.lower() not in words:
        print('You should guess a word from the given words list!')
        print('Please enter a correct word.')
        user_input = get_input()

    return user_input.lower()

def print_game_intro():
    print('-'*15)
    print('Hi, Welcome to the Guess Game.')
    print('All words:' , list_of_words)
    print('Please start guessing.')
    print('-'*15)

def run_game(number_of_rounds, words):
    print_game_intro()
    print(f'number of guesses: {number_of_rounds}')
    correct_word = random.choice(words)

    for i in range(number_of_rounds):
        user_input = get_input_from_list(words)

        if user_input == correct_word:
            print('You Won!')
            return
        else:
            print('You guessed wrong!')
            print(f'Please try again! number of rounds left: {number_of_rounds-1-i}')

    print('You lost')

list_of_words = ['sun', 'glass', 'coffee', 'today', 'moon', 'orange', 'old', 'young', 'paper', 'mom', 'dady' , 'sister', 'brother', 'father', 'mother', 'uncle', 'cousin', 'flower', 'monutine', 'sea', 'leave', 'docter']

run_game(3, list_of_words)