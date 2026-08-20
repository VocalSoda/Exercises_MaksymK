import math

grams = int(input("How many grams?: "))

if grams > 1000:
    gtokg = grams / 1000
    dot = str(gtokg).find(".")
    print("maara kiloina: " + str(gtokg)[:dot] + " grams: " + str(math.floor(((gtokg - int(gtokg)) * 1000))))
else:
    print("grams: " + str(grams))