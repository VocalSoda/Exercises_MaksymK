try:
    freedom_unit = int(input("please provide the amount of gallons you have: "))
except ValueError:
    print("Freedom likes integers!")
    
def freedom_to_normal(gallon_amount):  
    if gallon_amount < 0:
        print("Negative value provided")
    else:
        liter_amount = gallon_amount*3.785
        print(f"Amount of gallons:{gallon_amount} is roughly {liter_amount} in liters")
        

freedom_to_normal(freedom_unit)


        

