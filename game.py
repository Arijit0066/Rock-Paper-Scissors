import random


def game(comp, player):
    if comp == player:
        return None
    elif comp == 'r':
        if player == 'p':
            return True
        elif player == 's':
            return False
    elif comp == 'p':
        if player == 's':
            return True
        elif player == 'r':
            return False
    elif comp == 's':
        if player == 'r':
            return True
        elif player == 'p':
            return False
    



print("Rock(r)  Paper(p)  Scissors(s)")
rando = random.randint(1,3)
if rando == 1:
    comp = 'r'
elif rando == 2:
    comp = 'p'
elif rando == 3:
    comp = 's'

print("Computer Already Choosed")
player = input("Your Turn: ")
final = game(comp, player)
print("comp = ", comp)

if final == None:
    print("It's a Tie!!")
elif final == True:
    print("You Win!!")
else:
    print("You Lose!!")
