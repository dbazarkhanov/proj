import random


def comp(options):
    return options[random.randint(0, 2)]


def user(options):
    choice = int(input('Your choice: ')) - 1
    while choice > 3 or choice < 1:
        choice = int(input('Please choose again: '))
    return options[choice]


def game():
    options = ['Rock', 'Paper', 'Scissors']
    print('1 - Rock', '2 - Paper', '3 - Scissors', sep='\n')
    comp_choice = comp(options)
    user_choice = user(options)
    if user_choice == comp_choice:
        print('Tie!')
    elif ((user_choice == 'Rock' and comp_choice == 'Paper') or
          (user_choice == 'Scissors' and comp_choice == 'Rock') or
          (user_choice == 'Paper' and comp_choice == 'Scissors')):
        print('You lose!')
    else:
        print('You win!')


def play():
    play_again = ''
    while play_again.lower() != 'no':
        game()
        play_again = input('Do you want play again? yes\\no \n')


play()
