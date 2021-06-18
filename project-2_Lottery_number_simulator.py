#pick out four numbers (1st,2nd,3rd,4th,5th) from 1 to 200
import random

lottery_numbers = []

for i in range(5):
    number = random.randint(1,200)
    while number in lottery_numbers:
        number = random.randint(1,200)
    lottery_numbers.append(number)

print("{} number is the first position".format(lottery_numbers[0]))
print("{} number is the second position".format(lottery_numbers[1]))
print("{} number is the third position".format(lottery_numbers[2]))
print("{} number is the fourth position".format(lottery_numbers[3]))
print("{} number is the fiveth position".format(lottery_numbers[4]))