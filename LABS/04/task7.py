class Vehicle:
    def __init__(self, seatingcapacity):
        self.seatingcapacity = seatingcapacity

    def fare(self):
        return self.seatingcapacity * 100

class Bus(Vehicle):
    def fare(self):
        basefare = super().fare()  
        maintenancecharge = basefare * 0.10
        totalfare = basefare + maintenancecharge
        return totalfare


bus = Bus(30)  
print("Total Bus fare is Rs.",bus.fare())
