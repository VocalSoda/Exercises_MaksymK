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
        
class Race():
    
    def __init__(self, name, kilometers, car_list : list):
        
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list
        self.hours = 0
        
    def hour_passes(self): 
          
        for item in self.car_list:
            
            item.accelerate(random.randint(-10, 15)) 
            item.drive(1)
            
        self.hours = self.hours +1  
        print(self.hours)  
            
    def print_status(self):
           
        for item in self.car_list:
            print(f"{item.registration} | {item.max_speed} | {item.distance}")
             
    def race_finished(self):
        
        return any(item.distance >= self.kilometers for item in self.car_list)
         
         
         

car_list = []

for i in range(0, 9):
 car_list.append(Car(f"ABC-{i}", f"{random.randint(100, 200)}"))
 
race = Race("Grand Demolition Derby", 8000, car_list)
 
while True:
     
     race.hour_passes()
     
     if race.hours % 10 == 0:
         race.print_status()
     
     if race.race_finished():
        break    
     
     
 