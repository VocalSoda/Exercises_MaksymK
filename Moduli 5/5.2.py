number_list = []

while True:
    
    usr_input = input("Please enter an integer or an empty space to stop: ")
    
    if usr_input == " ":
        
        print(sorted(number_list, reverse=True)[:5])
        
        break
    
    try:
            new_int=int(usr_input)
            
            number_list.append(new_int)
            
    except ValueError:   
            
            print("Please insert number or an empty space to finish!")
            
            
    
        
  

    
    
        
    
    