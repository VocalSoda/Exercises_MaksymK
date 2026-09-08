
try:
    number = int(input("Insert a number: "))
except ValueError:
    
    print("insert a Number!")

while True:

    check_int = None
    
    for x in range(1, number-1):
        
        if number % x == 0:
            
            check_int = 1
        
    if check_int == 1:
        print(f"number {number} is a prime number")
        
        break
    else:
        print(f"number {number} is NOT prime number")
        
        break
            