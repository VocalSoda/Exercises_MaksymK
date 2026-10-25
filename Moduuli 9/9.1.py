import random

class Car():
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = int(max_speed)
        self.speed = 0
        self.distance = 0
        
    def accelerate(self, new_speed):
        self.speed = self.speed + new_speed
        if self.speed >= self.max_speed:
            self.speed = self.max_speed
        elif self.speed <= 0:
            self.speed = 0
                
    def drive(self, hours : int):
        if self.speed > 0:
            self.distance = self.distance + self.speed*hours
        

car_list = []

for i in range(0, 10):
 car_list.append(Car(f"ABC-{i}", f"{random.randint(100, 200)}"))

for item in car_list:
    print(item.registration, item.max_speed)
    
while all(item.distance <= 10000 for item in car_list):
    for item in car_list: 
        item.accelerate(random.randint(-10, 15)) 
        item.drive(1) 
    
 
winners_list = []

for item in car_list:
    append_item = [item.registration, item.distance]   
    winners_list.append(append_item)  
  
winners_list.sort(key=lambda item: item[1], reverse=True)        
for item in winners_list:
    print(item)