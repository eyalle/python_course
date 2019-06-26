from random import randint
import getpass

RPS = {
    'ROCK': {'WINS': 'SCISSORS', 'LOSES': 'PAPER'},
    'PAPER': {'WINS': 'ROCK', 'LOSES': 'SCISSORS'},
    'SCISSORS': {'WINS': 'PAPER', 'LOSES': 'ROCK'}
    }

def get_comp_choice():
    random_int = randint(0,10000) % 3
    # print(f'random is {random_int}\n')
    if (random_int == 0):
        return_val = 'ROCK'
    elif (random_int == 1):
        return_val = 'PAPER'
    else:
        return_val = 'SCISSORS'

    return return_val

def check_win(user, comp):
    if (RPS[comp]['WINS'] == user):
        win_message = f'computer wins as {RPS[comp]["WINS"]} wins {user}\n'
    elif (RPS[user]['WINS'] == comp):
        win_message = f'user wins as {RPS[user]["WINS"]} wins {comp}\n'
    else:
        win_message = f'WEIRD: {user}\t{comp}\n'
    print(win_message)
    # return winner
    pass

user_choice = 'None'
while (not user_choice in RPS):
    # user_choice = input('please enter your choice: Rock, Paper or Scissors\n').upper()
    user_choice = (getpass.getpass('please enter your choice: Rock, Paper or Scissors\n')).upper()

comp_choice = get_comp_choice()
# print(f'user ==> comp\n{user_choice} ==> {comp_choice}\n')
while (comp_choice == user_choice):
    print(f'TIE! {comp_choice} = {user_choice}')
    user_choice = getpass.getpass('let\'s try again: Rock, Paper or Scissors\n').upper()
    comp_choice = get_comp_choice()

check_win(user_choice, comp_choice)

