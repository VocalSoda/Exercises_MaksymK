import math

talents = input("please enter the amount of talents: ");
pounds = input("please enter the amount of pounds: ");
lots = input("please enter the amount of lots: ");

try:
        kglot =  0.0133
        kgpound = kglot * 32
        kgtal = kgpound * 20

        print("kg in lots: "+str(int(lots)*kglot))
        print("kg in pounds: "+str(int(pounds)*kgpound))
        print("kg in talents: "+str(int(talents)*kgtal))
        summ = (int(talents)*kgtal) + (int(pounds)*kgpound) + (int(lots)*kglot)
        sumstr = str(summ)
        dot = sumstr.find(".")
        print("In modern units " + str(summ)[:dot] + " Kilograms" + " and " +  str(math.floor(((summ - int(summ)) * 1000))) + " grams")
   
except ValueError:
    print("please enter numbers");