# Create a class called Bike with the following:
#price, speed, miles
#create 3 instances
#use __init__() to specify price and speed, also set intial miles to 0
#add functions displayInfo()-display price, speed, and miles, ride()-display "riding" and increase miles by 10, reverse()-decrease total miles by 5
#have first instance ride 3 times, reverse once, and display info
#have second instance ride twice, reverse twice, and display info
#have third instance reverse three times and display info
#prevent bike from having negative miles

class Bike(object):
    def __init__(self, price, speed):
        self.price = price
        self.speed = speed
        self.miles = 0
    def displayInfo(self):
        print "Price: {} Speed: {} Miles: {}".format(self.price, self.speed, self.miles)
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        print "Miles: {}".format(self.miles)
        return self
    def reverse(self):
        if self.miles <= 5:
            print "Sorry, cannot reverse!"
        else:
            print "Reversing"
            self.miles -= 5
        print "Miles: {}".format(self.miles)
        return self

bike1 = Bike(250, 25)
bike1.ride().ride().ride().reverse().displayInfo()
print "*" * 50

bike2 = Bike(400, 35)
bike2.ride().ride().reverse().reverse().displayInfo()
print "*" * 50

bike3 = Bike(75, 10)
bike3.ride().reverse().reverse().displayInfo()
print "*" * 50
