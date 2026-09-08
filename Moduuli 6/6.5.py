import random
int_list = []

for x in range(10):
    integ = random.randint(1, 10)
    int_list.append(integ)
    
def cut_down_list(list):
    
    small_list = []
    
    for x in list:
        
        if x % 2 == 0:
            
            small_list.append(x)
            
    print(small_list)
    return small_list
    
print(int_list)
cut_down_list(int_list)
        
    
        