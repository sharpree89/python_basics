# Create a class Car. In the __init__(), allow user to specify: price, speed, fuel, mileage. if price > 10,000 set tax to 15%, otherwise set tax to 12%
# Create six instances, each should have a method displayAll() that returns all info about the car as a string. in __init__(), call displayAll() to display info about the car once the attributes have been defined.

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price >= 10000:
            self.tax = 0.15 * self.price
        elif self.price < 10000:
            self.tax = 0.12 * self.price
        self.displayInfo()
    def displayInfo(self):
        print "Price: {}; Speed: {}; Fuel: {}; Mileage: {}; Tax: {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)
        print "*" * 50

carA = Car(12000, "65 mph", "Half Full", "15 mpg")
carB = Car(4000, "50 mph", "Almost Empty", "10 mpg")
carC = Car(60000, "95 mph", "Full", "36 mpg")
