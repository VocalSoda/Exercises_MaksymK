lst = []
while True:
    a = input("Please insert the number: ")
    if a == " ":
        print(f"Smallest number from the list is {min(lst)} and largest is {max(lst)}")
        break
    else:
        try:
            lst.insert(1, int(a))
        except ValueError:
            print("please insert number or space")
    


    

        
    