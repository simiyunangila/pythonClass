class Car:
    motors="vehicles"
    def __init__(self,make,model,speed):
        self.make=make
        self.model=model
        self.speed=speed

    def acceleration(self,accelerate):
        self.accelerate=accelerate
        new =self.speed + accelerate
        return new   

    def decceleration(self,deccelerate):
        self.deccelerate=deccelerate
        new = self.speed - deccelerate
        return new
        
    def description(self):
        return f"{self.make} of {self.model} begins at speed {self.speed} "          

