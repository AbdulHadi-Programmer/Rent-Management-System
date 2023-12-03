# Rent Management System :
# Two classes Tenants, Properties
# Write a function that connect particular tenant to particular property 
# Write two list of tenants and properties
# Property is a class
# properties is a list 
class Property:
    Location = "Gazderabad" # I make location a class var because my all properties belong to this area
    def __init__(self, HouseName, noOfRooms, rent):
        self.HouseName = HouseName
        self.noOfRooms = noOfRooms
        self.rent = rent
        
    def Detail(self):
        print(f'The Property Detail:\nHouseName: {self.HouseName}\nLocation: {self.Location}\nNo of Rooms: {self.noOfRooms}\nRent: {self.rent}\n')
# Now Property class is properly Working:
obj1 = Property("House1", 2, 12000)
obj1.Detail()
obj2 = Property("House2", 4, 25000)
obj2.Detail()
properties = []


 