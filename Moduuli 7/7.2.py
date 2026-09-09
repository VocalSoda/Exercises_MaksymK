name_set = set()

while True:
    name = input("please provide the name: ")
    if name in name_set:
        print("Name exists!")
    else:
        print("New name")
        
    name_set.add(name)
        
    if name == " ":
       for x in name_set:
        print(x)
        
       break
    
    
    
    