import random


def number(min_num, max_num):
    return random.randint(min_num, max_num)


def user(min_num, max_num):
    return int(input(f'Guess number between {min_num} and {max_num}: '))


def game(min_num, max_num):
    low = min_num
    high = max_num
    cmp_number = number(low, high)
    user_number = user(low, high)

    while user_number != cmp_number:
        user_number = int(input('Wrong! Try again: '))

    print('Congratulations, you won!')


game(int(input('Min number: ')), int(input('Max number: ')))
