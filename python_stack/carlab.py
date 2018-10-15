class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        
    def display_all(self):
        print("===================================")
        print("      Price: ", '\033[95m' + str(self.price) + '\033[00m')
        print("      Speed: ", self.speed)
        print("       Fuel: ", self.fuel)
        print("    Mileage: ", self.mileage)
        print("        Tax: ", self.tax)                                     
        print("===================================")

toyota_corrola = Car(2000, "35mph", "Full", "15mpg")
honda_civic = Car(2000, "5mph", "Not Full", "105mpg")
mazda_miata = Car(2000, "15mph", "Kind of Full", "95mpg")
ford_taurus = Car(2000, "25mph", "Full", "25mpg")
chevy_camaro = Car(2000, "45mph", "Empty", "25mpg")
bugatti_chiron = Car(20000000, "35mph", "Empty", "15mpg")

toyota_corrola.display_all()
honda_civic.display_all()
mazda_miata.display_all()
ford_taurus.display_all()
chevy_camaro.display_all()
bugatti_chiron.display_all()
