import random

hands = ['rock', 'scissors', 'paper']
results = {'win': '🎉win', 'lose': '💀lose', 'draw': '🫡draw try again'}


def start_message():
    print('🎮Start \'rock-paper-scissors\'')


def is_hand(string):
    if string.isdigit():
        number = int(string)
        if number >= 0 and number <= 2:
            return True
        else:
            return False
    else:
        return False


def get_player():
    print('Input your hand')
    input_message = ''
    index = 0
    for hand in hands:
        input_message += str(index) + ':' + hand
        if index < 2:
            input_message += ', '
        index += 1
    return input(input_message)


def get_computer():
    return random.randint(0, 2)


def get_hand_name(hand_number):
    return hands[hand_number]


def view_hand(your_hand, computer_hand):
    print('My hand is ' + get_hand_name(your_hand))
    print('Rival\'s hand is ' + get_hand_name(computer_hand))


def get_result(hand_diff):
    if hand_diff == 0:
        return 'draw'
    elif hand_diff == -1 or hand_diff == 2:
        return 'win'
    else:
        return 'lose'


def view_result(result):
    print(results[result])


def play():
    your_hand = get_player()
    while not is_hand(your_hand):
        your_hand = get_player()

    your_hand = int(your_hand)
    computer_hand = get_computer()
    hand_diff = your_hand - computer_hand

    view_hand(your_hand, computer_hand)
    result = get_result(hand_diff)
    view_result(result)
    if result == 'draw':
        play()


start_message()
play()