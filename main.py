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
p1 = Property("House1", 2, 12000)
p1.Detail()
p2 = Property("House2", 4, 25000)
p2.Detail()
properties = [p1, p2]

# properties = [
#         Property("House1", 2, 15000),
#         Property("House1", 3, 52000),
#         Property("House1", 2, 12000),
#         Property("House2", 1, 10000),
#         Property("House2", 4, 60000),
#         Property("House2", 5, 65000),
#         # Add more properties as needed
#     ]
#     # Display details for each property using a loop and enumerate
# for index, property_obj in enumerate(properties, start=1):
#     print(f"\nProperty {index} Details:")
#     property_obj.Detail()

 