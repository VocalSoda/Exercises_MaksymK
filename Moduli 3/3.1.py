from random import randrange
from threading import Timer

size = input("Please insert the lenght of your Zander: ")


try:
    if int(size) <= 42:
        choice = int(input("Please release the fish, it is too small and you will be arested (press 1) or keep it at your own risk (press 2): "))
        if choice == 1:
            print("Good choice!");
        elif choice == 2:
            conseq = randrange(3)
            if conseq % 2 == 0:
                print("Alright keep it this time, BUT never comeback!")
            else:
                print("Busted!")
                
    else:
        print("Nice Catch!")
except ValueError:
    print("Please insert ZAnder size in cm")

                    
            


