class Bike:
    def __init__(self, price, max_speed):
        self.miles = 0
        self.price = price
        self.max_speed = max_speed
    def displayInfo(self):
        print("===================================")
        print("    Price: ", self.price)
        print("    Maximum Speed: ", self.max_speed)
        print("    Total Miles: ", self.miles)
        print("===================================")
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    def reverse(self):
        print("Reversing")
        if self.miles >= 5:
            self.miles -= 5
        return self

bike1 = Bike(200, 25)
bike2 = Bike(300, 35)
bike3 = Bike(1000, 75)

bike1.ride().ride().ride().reverse()
print("Bike1")
bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
print("Bike2")
bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
print("Bike3")
bike3.displayInfo()
