import random

def dice_roll(user_input):
    dice = None
    while dice != user_input:
        dice = random.randrange(1, user_input+1)
        print(dice)
    
dice_roll(21)