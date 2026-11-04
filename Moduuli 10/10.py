

class Elevator():
    
    def __init__(self, bottom_floor : int, elevator_length : int, current_floor : int):
       
       self.length = elevator_length
       self.current_floor = current_floor
       self.bottom_floor = bottom_floor

       
        
    def go_up(self): 
        
        if self.current_floor != self.length:
            
            self.current_floor = self.current_floor + 1
            print("The elevator is now on floor", self.current_floor) 
    
    def go_down(self):
        
        if self.current_floor != self.bottom_floor:
            
            self.current_floor = self.current_floor - 1
            print("The elevator is now on floor", self.current_floor)
            
    def go_to_target(self, elevetor_target : int):
        
        while self.current_floor != elevetor_target:
            
            if elevetor_target > self.current_floor:
                
                self.go_up()
            
            elif elevetor_target < self.current_floor:
                
                self.go_down()    
        
class Building():
         
        def __init__(self, elevator_bottom : int, elevator_top : int, number_of_elevators : int):
             
             self.elevator_list = []
             self.number_of_elevators = number_of_elevators
             self.elevator_top = elevator_top
             self.elevator_bottom = elevator_bottom
             
        def create_elevator(self):

                while len(self.elevator_list) < self.number_of_elevators:
                    
                    elevator = Elevator(self.elevator_bottom, self.elevator_top, 1)   
                    
                    self.elevator_list.append(elevator) 
                    
        def run_elevator(self, elevator_number : int, target_floor : int):
             
            elevator_number = elevator_number - 1 
             
            chosen_elevator = self.elevator_list[elevator_number]
             
            chosen_elevator.go_to_target(target_floor) 
        
        def fire_alarm(self):
            
            for item in self.elevator_list:
                
                item.current_floor = 0 
                
                print(f"fire alarm trigered, elevator is on floor {item.current_floor}")
        
                    
                    
                           
         
        
        
        
        
# elevator1 = Elevator(-3, 5, 4)
# elevator1.go_to_target(-3) 

building1 = Building(0, 5, 2) 

building1.create_elevator()

building1.run_elevator(1, 3) 

for item in building1.elevator_list:
    print(item.current_floor)
    
building1.fire_alarm()
    




