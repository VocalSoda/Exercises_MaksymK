import random
a = [0,1,2,3,4,5,6,7,8,9]
b = [0,1,2,3,4,5,6]
smallpass = []
bigpass = []
for x in a: 
    smallpass.insert(1, random.choice(a))
    bigpass.insert(1, random.choice(b))

    if len(smallpass) == 3:
            print(smallpass)

    if len(bigpass) == 4:
            print(bigpass)
            break
    
