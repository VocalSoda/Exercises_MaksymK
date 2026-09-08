try:
    pizza1_cm = float(input("Please provide diameter og pizza: "))
    pizza1_price = float(input("Please provide the price: "))
    
    pizza2_cm = float(input("Please provide diameter second pizza: "))
    pizza2_price = float(input("Please provide the second price: "))
except ValueError:
    print("please provide floats")
    
    
def pizza_calc(diameter1, price1, diameter2, price2):
    
    pizza1_sqm = diameter1/10000
    pizza1_price = price1/pizza1_sqm
    
    pizza2_sqm = diameter2/10000
    pizza2_price = price2/pizza2_sqm
    
    if pizza1_price < pizza2_price:
        print("Pizza 1 has better price per sqare meter")
    else:
        print("Pizza 2 has better price per square meter")
        

pizza_calc(pizza1_cm, pizza1_price, pizza2_cm, pizza2_price)