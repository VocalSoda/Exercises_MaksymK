import random


dice_amount = int(input("How many dice to roll?: "))

for x in range(dice_amount):
    dice = random.randrange(1, 6)
    print(f'{dice}')