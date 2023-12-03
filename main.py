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
# p1 = Property("House1", 2, 12000)
# p1.Detail()
# p2 = Property("House2", 4, 25000)
# p2.Detail()
# properties = [p1, p2]

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
    
    def update_details(self, new_name, new_gender, new_contactNum, new_email):
        self.name = new_name
        self.gender = new_gender
        self.contactNum = new_contactNum
        self.email = new_email
        print(f'Tenant details updated.\n')


# t1 = Tenant("Abdul Hadi", "Male", "+922319536","abc@gmail.com")
# t2 = Tenant("Jane Smith", "Female", "+987654321", "jane@example.com")
# t3 = Tenant("Bob Johnson", "Male", "+111222333", "bob@example.com")
# t4 = Tenant("John Doe", "Male", "+123456789", "john@example.com")
# tenants = [t1, t2, t3, t4]
## t1.person_detail()
## t1.contract()
# for index, tenant in enumerate(tenants, start=1):
#     print(f"\nTenant {index} Details:")
#     tenant.person_detail()
    
# Write a Lease Class to connect tenant with property:
class Lease:
    def __init__(self, tenant, property, duration):
        self.tenant = tenant
        self.property = property
        self.duration = duration
        
    def display_details(self):
        print(f'Lease Details for {self.tenant.name}:\nProperty: {self.property.HouseName}\nDuration: {self.duration}')  # Fix the typo here

    def update_duration(self, new_duration):
        self.duration = new_duration
        print(f'Duration for {self.tenant.name} updated to {self.duration}\n')

    def remove_tenant(self):
        print(f'Removing tenant {self.tenant.name} from the lease.\n')
        self.tenant = None  # Setting tenant to None indicates that the lease is now vacant
# l1 = Lease(tenants[0], properties[0])
# l2 = Lease(tenants[1], properties[1])
# l3 = Lease(tenants[2], properties[2])
#################################################
print("\n\n\nExample Showeing:\n\n")
# Example usage:
"""property1 = Property("House1", 2, 12000)
tenant1 = Tenant("Abdul Hadi", "Male", "+922319536", "abc@gmail.com")
lease1 = Lease(tenant1, property1, "1 year")
property2 = Property("House2", 2, 52000)
tenant2 = Tenant("Abdul Bari", "Male", "+922319536", "Xyz@gmail.com")
lease2 = Lease(tenant2, property2, "4 year")
# Display details before any changes
lease1.display_details()
# Update tenant details
tenant1.update_details("Updated Abdul Hadi", "Male", "+922319537", "updated_abc@gmail.com")
# Update lease duration
lease1.update_duration("2 years")
# Display details after updates
lease1.display_details()
# Remove tenant from the lease
lease1.remove_tenant()
lease2.display_details()
"""
