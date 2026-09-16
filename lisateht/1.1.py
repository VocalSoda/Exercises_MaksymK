usr_input = int(input("Enter height: "))
i=int(1)
c=int(0)
c = 1
while c <= usr_input:
    abc =  "*"*i
    num = usr_input - c
    cba = " "*num
    print(cba+abc)
    c= c+1
    i = i +2
