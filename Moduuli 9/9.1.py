class Car():
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0
        
car = Car("123", "80")

print(f"{car.registration} and {car.max_speed}, {car.distance}")