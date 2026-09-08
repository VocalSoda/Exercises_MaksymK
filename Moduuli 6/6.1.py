import random

def dice_roll():
    dice = None
    while dice != 6:
        dice = random.randrange(1, 7)
        print(dice)
    
dice_roll()