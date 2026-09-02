import math
import random
pointamount = 0
maxpointamount = int(input("What is point amount?: "))
cornerA = [-1, 1]
cornerB = [1, -1]
cornerC = [1, 1]
cornerD = [-1, -1]
npoint = 0
while pointamount < maxpointamount:
    pointamount = pointamount +1
    randpoints = [random.uniform(-1, 1), random.uniform(-1, 1)]
    if -1<=randpoints[0] <=1 and -1<=randpoints[1]<=1:
        if randpoints[0]**2 + randpoints[1]**2 < 1:
            npoint = npoint+1
            pie = (4*npoint)/maxpointamount
            print(f"{pie}")

   

