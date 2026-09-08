
try:
    number = int(input("Insert a number: "))
except ValueError:
    
    print("insert a Number!")


for x in range(2, number):
        print(x)
        if number % x == 0:
          print(f"number {number} is NOT prime number")
          break        
            
         
else:  
    print(f"number {number} is prime number")
    

            
            
