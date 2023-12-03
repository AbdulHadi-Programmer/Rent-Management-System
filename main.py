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

class Tenant:
    def __init__(self, name, gender, contactNum, email):
        self.name = name
        self.gender = gender
        self.contactNum = contactNum
        self.email = email
        
    def person_detail(self):
        # print(f'Tenant Detail:\nName: {self.name}\nGender: {self.gender}\nPhone Num: {self.contactNum}\nEmail: {self.email}\n')
        print(f'Name: {self.name}\nGender: {self.gender}\nPhone Num: {self.contactNum}\nEmail: {self.email}\n')
    
    # def contract(self):
    #     print(f'The Contract of {self.name} is:\nDuration: {self.duration}\n')

t1 = Tenant("Abdul Hadi", "Male", "+922319536","abc@gmail.com", "1 year")
t2 = Tenant("Jane Smith", "Female", "+987654321", "jane@example.com", "4 month")
t3 = Tenant("Bob Johnson", "Male", "+111222333", "bob@example.com", "2 years")
t4 = Tenant("John Doe", "Male", "+123456789", "john@example.com", "6 months")
tenants = [t1, t2, t3, t4]
# t1.person_detail()
# t1.contract()
for index, tenant in enumerate(tenants, start=1):
    print(f"\nTenant {index} Details:")
    tenant.person_detail()
    tenant.contract()

