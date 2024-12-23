import random

choices = ['r','p','s']

choice_meaning={
    'r': 'Rock',
    's': 'Scissors',
    'p': "Paper",
}

user_score = 0
ai_score = 0
final_number = 3

while True:
    user_choice = input('Select from Rock, Paper, Scissors: (r, p, s) ')

    ai_choice = random.choice(choices)

    if user_choice in choices:
        print(f'Your choice is {choice_meaning[user_choice]}. AI choice is {choice_meaning[ai_choice]}.')

        if user_choice == ai_choice:
            print('Tie')
        elif user_choice == 'r' and ai_choice == 's':
            print('user + 1 score!')
            user_score += 1
        elif user_choice == 'p' and ai_choice == 'r':
            print('user + 1 score!')
            user_score += 1
        elif user_choice == 's' and ai_choice == 'p':
            print('user + 1 score!')
            user_score += 1
        else:
            print('Ai + 1 score!')
            ai_score += 1
    else:
        print('Invalid input')

    print(f'User score: {user_score} / AI score: {ai_score}')
    
    if user_score == final_number or ai_score == final_number:
        break

    print('\n', '-'*15, '\n')

if user_score == final_number:
    print(f'User won with score: {user_score}')
else:
    print(f'AI won with score: {ai_score}')