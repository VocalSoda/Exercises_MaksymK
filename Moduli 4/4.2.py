import math

while True:
    try: 
        inch = int(input("How many inches?: "))
        cent = inch * 0.39
        if inch < 0:
            print("inch should've been higher than 0!")
            break
        print(f"{inch} in centimeters is {math.floor(cent)}")
    except ValueError:
        print("Please provide an integer!")
