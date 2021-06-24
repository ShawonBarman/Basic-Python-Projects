import random

# create function for fullfil this condition : r>s, s>p, p>r
def is_win(player,component):
    #return true if the player win
    if (player=='r' and component=='s') or (player=='s' and component=='p') or (player=='p' and component=='r'):
        return True

while True:
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n please enter your choice: ")
    computer = random.choice(['r','p','s'])
    if user == computer:
        print("Opps, it\' a tie. Lets try again\n")
    if is_win(user,computer):
        print("Wow, You win! nice job!")
        break
    if is_win(computer,user):
        print("Opps sorry! you lost! Lets try again\n")

