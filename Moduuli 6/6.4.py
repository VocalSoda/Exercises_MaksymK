import random
int_list = []

for x in range(10):
    integ = random.randint(1, 10)
    int_list.append(integ)
    
def list_sum(list):
    print(list)
    big_int = int()
    for x in list:
        big_int=big_int+x
    print(big_int)


list_sum(int_list)