import math

luku1 = input("provide first number: ")
luku2 = input("provide second number: ")
luku3 = input("provide third number: ")


try:
    numlist = [luku1, luku2, luku3]
    numbers = [int(x) for x in numlist]
    summ = print("summa: "+ str(sum(numbers)))
    avg = print("avg: "+str(sum(numbers)/len(numbers)))
    tulo = math.prod(numbers)
    print("tulo: "+str(tulo))
except ValueError:
     print("papers please")
     
