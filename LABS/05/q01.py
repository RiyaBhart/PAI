class Vehicle:
    def __init__(self, seatingcap):
        self.seatingcap = seatingcap

    def fare(self):
        return self.seatingcap * 100

class Bus(Vehicle):
    def fare(self):
        fare = super().fare()
        totalfare = fare + (fare * 0.10)  
        return totalfare


a = Vehicle(2)
print(a.fare())  

b = Bus(2)
print(b.fare())  
