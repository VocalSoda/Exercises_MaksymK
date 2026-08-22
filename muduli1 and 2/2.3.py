a = input("side a: ");
b = input("side b: ");


try:
    perm = 2*int(a) + 2*int(b)
    area = int(a)*int(b)
    print("perimeter is: " +  str(perm))
    print("area is: " +  str(area))
except ValueError:
    print("a and b should be numbers")
    quit()
