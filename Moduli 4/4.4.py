import random
draw = random.randrange(0, 10)

while True:
    try:
        usr = int(input("Insert Number between 0 and 10: "))
        if draw > usr:
            print("too low!")
        elif draw < usr:
            print("too high!")
        
        else:
            print("CORRECT")
    except ValueError:
        print("Number please!")
