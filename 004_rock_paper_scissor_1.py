import random

def play():
    user = input('What\'s your choice? \n r for rock \n p for paper \n s for scissors \n:===> ')
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'Yayy!!! You Win!'
    
    return 'You Lost...'

def is_win(player, bot):
    if(player == 'r' and bot == 's') or (player == 'p' and bot == 'r') or \
    (player == 's' and bot == 'p'):
        return True

print(play())