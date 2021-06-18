import random

guesses = []
myComputer = random.randint(1,100)
player = int(input("Enter a number between 1 to 100 : "))
if player>=1 and player<=100:
    guesses.append(player)
else:
    print("Please enter a number between 1 to 100")

while player!=myComputer:
    if player>myComputer:
        print("Opps sorry! Your guessing number is too high")
        print("please try again")
    else:
        print("Opps sorry! Your guessing number is too low")
        print("please try again")
    player = int(input("Enter a number betweeon 1 to 100 : "))
    guesses.append(player)
else:
    print("You have guesses right number! Good job!")
    print("Its took you {} guesses".format(len(guesses)))
    print("These were your guesses : ")
    print(guesses)