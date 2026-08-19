a = input("side a: ");
b = input("side b: ");


if  int(a) and int(b) > 0:

    perm = 2*int(a) + 2*int(b)
    area = int(a)*int(b)
    print("perimeter is: " +  str(perm))
    print("area is: " +  str(area))

else:

    print("Please insert integer")