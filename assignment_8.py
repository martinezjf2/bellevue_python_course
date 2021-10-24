# This week we will work with classes by creating a virtual garage. Your program will use the inheritance diagram from this week in order to create a parent class and two child classes.
# Your program will prompt the user to create at least one object of each type (Car and Pickup). Using a menu system and capturing user input your program will allow the user the choice of adding a car or pickup truck and define the vehicle's attributes. The program will use user input to define the vehicle's attributes.
# The options attribute in the parent class must be a python list containing a minimum of eight (8) options common to all vehicles. (i.e. power mirrors, power locks, remote start, backup camera, bluetooth, cruise control, etc).
# The user will choose from a list of options to add to the vehicle's options list and can must choose a minimum of one vehicle option per vehicle. When the user is finished adding vehicles to their virtual garage the program will output the vehicles in their garage and their attributes.


# The following information provides students with a breakdown of how this assignment will be assessed.
# 1. Object Oriented Programming and Inheritance - 30%
# Create a Vehicle class with the attributes and functions detailed in the class diagram. - 10%
# Create a Car class as a child of the Vehicle class with the attributes and functions detailed in the class diagram. - 10%
# Create a Pickup class as a child of the Vehicle class with the attributes and functions detailed in the class diagram. - 10%
# 2. Demonstrate usage of previously studied programming constructs (functions, conditionals, loops)  - 60%
# Using a function, display a menu prompting the user to add a Car or a Pickup to their virtual garage. - 15%
# Your program must allow the user to have multiple vehicles in their virtual garage and must have at least one Car and one Pickup. - 15 %
# Your program will prompt the user to define the attributes of the vehicles in their garage. - 10%
# The options attribute will be defined as a python list chosen by the user when presented with a menu of programmer chosen vehicle options that can apply to both cars and pickup trucks (i.e. power mirrors, power locks, remote start, backup camera, bluetooth, cruise control, etc) - 20%
# 3. When the user has finished adding and defining vehicles for their garage the program will output the vehicles with their accompanying attributes and options as specified by the user. -10 %



class Vehicle:
    def __init__(self, make, model, color, fuelType, options) :
        self.make=make
        self.model=model
        self.color=color
        self.fuelType= fuelType
        self.options=options

    def getMake(self) :
        return self.make

    def getModel(self) :
        return self.model

    def getColor(self) :
        return self.color

    def getFuelType(self) :
        return self.fuelType

    def getOptions(self) :
        return self.options


class Car(Vehicle) :
    def __init__(self, make, model, color, fuelType, options, engineSize, numDoors):
        Vehicle.__init__(self, make, model, color, fuelType, options)
        self.engineSize=engineSize
        self.numDoors=numDoors

    def getEngineSize(self) :
        return self.engineSize

    def getNumDoors(self) :
        return self.numDoors

    def printDetails(self) :
        print("Car Make : ", self.make)
        print("Car Model : ", self.model)
        print("Car Color : ", self.color)
        print("Car Fuel Type : ", self.fuelType)
        print("Car Options : ", self.options)
        print("Car Engine Size : ", self.engineSize)
        print("Car Number of Doors : ", self.numDoors)


class Pickup(Vehicle) :
    def __init__(self, make, model, color, fuelType, options, cabStyle, bedLength):
        Vehicle.__init__(make, model, color, fuelType, options)
        self.cabStyle=cabStyle
        self.bedLength=bedLength

    def getCabStyle(self) :
        return self.cabStyle

    def getBedLength(self) :
        return self.bedLength

    def printDetails(self) :
        print("Pickup Make : ", self.make)
        print("Pickup Model : ", self.model)
        print("Pickup Color : ", self.color)
        print("Pickup Fuel Type : ", self.fuelType)
        print("Pickup Options : ", self.options)
        print("Pickup Cab Style : ", self.cabStyle)
        print("Pickup Bed Length : ", self.bedLength)

garage=[]
while(True) :
    option = int(input("Enter \n1 for Car \n2 for Pickup \n3 for exit \n"))
    if(option==1):
        make=input("Enter Car Make : ")
        model=input("Enter Car Model : ") 
        color=input("Enter Car Color : ") 
        fuelType=input("Enter Car Fuel Type : ") 
        options=input("Enter Car option separated by spaces : ") 
        engineSize=int(input("Enter Car Engine Size : ")) 
        numDoors=int(input("Enter Car Number of Doors : ")) 
        p=Car(make, model, color, fuelType, options, engineSize, numDoors)   
        garage.append(p)
    elif (option==2):
        make=input("Enter Pickup Make : ")
        model=input("Enter Pickup Model : ") 
        color=input("Enter Pickup Color : ") 
        fuelType=input("Enter Pickup Fuel Type : ") 
        options=input("Enter Pickup option separated by spaces : ") 
        cabStyle=int(input("Enter Pickup Cab Style : ")) 
        bedLength=int(input("Enter Pickup Bed Length : ")) 
        t=Pickup(make, model, color, fuelType, options, cabStyle, bedLength)   
        garage.append(t)
    else:
        break




print("Vehicles Details is : ")
print("---------------------------------")
for i in garage:
    print(i.printDetails())