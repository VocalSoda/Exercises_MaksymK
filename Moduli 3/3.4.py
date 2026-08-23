while True:
    try:
        year = int(input("Please enter a year: "))
        break
    except ValueError:
        print("Please entern an integer!")

def year_check(year):
   
    if year % 100 == 0 and year % 400 == 0:
        print(f"Year {year} is a leap year that is also divisible by 400")
    elif year % 4 == 0:
            print(f"Year {year} is a leap year!")
    else:
        print(f"Year {year} is NOT a leap year!")


year_check(year)
    
    

