# Rent Management System :
# Two classes Tenants, Properties
# Write a function that connect particular tenant to particular property 
# Write two list of tenants and properties
# Property is a class
# properties is a list 
## Add User Interaction '
## Add Data Validation and we can also use Error Handling
##

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
p1 = Property("House1", 2, 15000)
p2 = Property("House2", 3, 52000)
p3 = Property("House3", 2, 15000)
p4 = Property("House4", 2, 15000)
p5 = Property("House5", 4, 60000)
p6 = Property("House6", 5, 65000)
properties = [p1, p2, p3, p4, p5, p6]
"""properties = [
        Property("House1", 2, 15000), # Direct make class as list element
        Property("House2", 3, 52000),
        Property("House3", 2, 12000),
        Property("House4", 1, 10000),
        Property("House5", 4, 60000),
        Property("House6", 5, 65000),
        # Add more properties as needed
    ]"""
#     # Display details for each property using a loop and enumerate
# for index, property_obj in enumerate(properties, start=1):
#     print(f"\nProperty {index} Details:")
#     property_obj.Detail()

class Tenant:
    def __init__(self, name, contactNum, email):
        self.name = name
        self.contactNum = contactNum
        self.email = email
        self.rent_history = []


    def add_rent(self, rent_amount):
        self.rent_history.append(rent_amount)
        print(f'Rent of {rent_amount} added to {self.name}\'s history.\n')
    
    def display_rent_history(self):
        print(f'Rent History for {self.name}: {self.rent_history}\n')
        print(f'The Total Sum Of Rent Amount is {sum(self.rent_history)}')
    
    def person_detail(self):
        print(f'Name: {self.name}\nPhone Num: {self.contactNum}\nEmail: {self.email}\n')
    
    def update_details(self, new_name, new_contactNum, new_email):
        self.name = new_name
        self.contactNum = new_contactNum
        self.email = new_email
        print(f'Tenant details updated.\n')


t1 = Tenant("Abdul Hadi", "+922319536","abc@gmail.com") # Make object of class to store in list 
t2 = Tenant("Jane Smith", "+987654321", "jane@example.com")
t3 = Tenant("Bob Johnson", "+111222333", "bob@example.com")
t4 = Tenant("John Doe", "+123456789", "john@example.com")
tenants = [t1, t2, t3, t4] # Storing All tenant with the objects name 
# t_detail = [t1.person_detail(), t2.person_detail(), t3.person_detail(), t4.person_detail() ]
## t1.person_detail()
def show_tenants():
    for index, tenant in enumerate(tenants, start=1):
        print(f"\nTenant {index} Details:")
        tenant.person_detail()
        
def show_properties():
    for index, property_obj in enumerate(properties, start=1):
        print(f"\nProperty {index} Details:")
        property_obj.Detail()
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
        # print(f'Removing tenant {self.tenant.name} from the lease.\n')
        # self.tenant = None  # Setting tenant to None indicates that the lease is now vacant
        if self.tenant:
            print(f'Removing tenant {self.tenant.name} from the lease.\n')
            self.tenant = None
        else:
            print('No tenant to remove from the lease.\n')
    
l1 = Lease(tenants[0], properties[3], "1 year")
l2 = Lease(tenants[1], properties[1], "9 month")
l3 = Lease(tenants[2], properties[0], "3 year")
l4 = Lease(tenants[3], properties[2], "2 month")
leases = [l1, l2, l3, l4]

#################################################
# print("\n\n\nExample Showeing:\n\n")
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
# # Rent Added Funcion (Example usage):
# t1 = Tenant("Abdul Hadi", "Male", "+922319536", "abc@gmail.com")
# l1 = Lease(t1, Property("House1", 2, 15000), "1 year")
# # Add rent for the tenant
# t1.add_rent(15000)
# t1.add_rent(14000)
# t1.add_rent(10000)
# # Display rent history
# t1.display_rent_history()
# After writing the menu , if i have time then i can also add the program into the category
# like: Tenants = Add, Update , Remove, Show All tenants
# Properties = Add, 
# lease = Show All Lease, Connect Both, Add
#### Leases Detail Function:
def display_valid_and_invalid_leases():
    global invalid_properties, invalid_tenants
    valid_leases = []
    invalid_properties = []  # Invalid Properties
    invalid_tenants = []     # Invalid Tenants

    # Set of all properties
    all_properties = set(properties)

    # Iterate through leases
    for lease in leases:
        # Check if the property in the lease is present in the list of properties
        if lease.property in properties and lease.tenant in tenants:
            valid_leases.append(lease)
        else:
            # If property or tenant is missing, append to the respective invalid list
            if lease.property not in properties:
                invalid_properties.append(lease.property)
            if lease.tenant not in tenants:
                invalid_tenants.append(lease.tenant)

    # Properties without a tenant
    unleased_properties = all_properties - set(p.property for p in leases)

    # Display details for valid leases
    if valid_leases:
        print("\nValid Leases:")
        for index, lease in enumerate(valid_leases, start=1):
            print(f"\nValid Lease {index} Details:")
            lease.display_details()
    else:
        print("No valid leases found.")

    # Display details for invalid properties
    if invalid_properties:
        print("\nInvalid Properties:")
        for index, invalid_property in enumerate(set(invalid_properties), start=1):
            print(f"\nInvalid Property {index} Details:")
            invalid_property.Detail()

    # Display properties without a tenant
    if unleased_properties:
        print("\nUnleased Properties:")
        for index, unleased_property in enumerate(unleased_properties, start=1):
            print(f"\nUnleased Property {index} Details:")
            unleased_property.Detail()

    # Check if there are more tenants than properties
    if len(tenants) > len(properties):
        print("\nWarning: There are more tenants than properties.")
        print("Some tenants may not have properties leased.")

    
while True:
    try:
        choice = int(input("\nEnter What you want to perform:\n1)  Add new Tenant\n2)  Add Property\n3)  Connect Property with Tenants\n4)  Show All Tenants\n5)  Show All Property\n6)  Remove Tenants\n7)  Add Rent\n8)  Show Rent History\n9)  Update Tenant Information\n10) Show All Leases\n11) Exit\n*) Enter the Option:- "))
        if choice == 1:  # Add Tenant
            print("Add new Tenant")
            name = input('Enter The name of tenant: ')
            Num = input('Enter the Number: ')
            email = input('Enter the email: ')
            t = Tenant(name, Num, email)
            tenants.append(t)
        elif choice == 2:  # Add Property
            #  HouseName, noOfRooms, rent
            HouseName = input("Enter The name of House: ")
            noOfRooms = int(input(f"Enter the no of rooms in {HouseName}: "))
            rent = int(input("Enter the rent amount for the property: "))
            p = Property(HouseName, noOfRooms, rent)
            properties.append(p)
            show_properties()   
        elif choice == 3:   # Connect both
            display_valid_and_invalid_leases()
            invalid_properties
            ####################################################
            # This is a pending Section in this first
            # 1) I want to check if tenant is less than properties or equal than
            # 2) If it was less than properties then add tenant and then add lease with new properties as we can select it 
            # 3) If the tenants was more show the error using exception handling
            # 4) Then add new properties 
            # 5) And only Show that property on lease which is vacant mean if 4 tenant and 6 properties then show the last 2 properties to add the tenant to that property 
            # 6) And then add these two in the lease class and then append the lease objct into the list
            
            # Lease :
            # tenant, property, duration
            # show_tenants()
            # show_properties()
            
        # property1 = Property("House1", 2, 12000)
        # tenant1 = Tenant("Abdul Hadi", "Male", "+922319536", "abc@gmail.com")
        # lease1 = Lease(tenant1, property1, "1 year")
            pass    
        elif choice == 4:   # Show All Tenants
            show_tenants()
            
        elif choice == 5:   # Show All properties
            show_properties()
                
        elif choice == 6:   # Remove Tenants
            show_tenants()
            ask = int(input("Enter the Tenants Number To Remove: ")) - 1  # -1 because index 
            tenants.pop(ask)
            print(f"Successfully removed Tenants")

        elif choice == 7:   # Add Rent
            show_tenants()
            ask = int(input("Enter the Tenants Number For Adding Rent: ")) - 1
            if 0 <= ask < len(tenants):
                rent = int(input("Enter the rent Amount: "))
                a = tenants[ask]
                a.add_rent(rent)
                b = tenants[ask].person_detail()
                print(b)
            else:
                print("Invalid tenant index. Please enter a valid index.")
            
        elif choice == 8:   # Show Rent History
            show_tenants()
            ask = int(input("Enter the Tenants Number For Showing Rent History: ")) - 1
            if 0 <= ask < len(tenants):
                tenants[ask].display_rent_history() # t1.displayrent()     ## show rent history
            else:
                print("Invalid tenant index. Please enter a valid index.")
        
        elif choice == 9:   # Upgrade tenant info
            show_tenants()
            ask = int(input("Enter the Tenants Number For Upgrading Information: ")) - 1
            new_name = input('Enter the Name: ')
            new_contactNum = input('Enter the Phone Number: ')
            new_email = input('Enter the new email: ')
            tenants[ask].update_details(new_name, new_contactNum, new_email)
            show_tenants()

        elif choice == 10:   # Search and display lease details for a specific tenant
            show_tenants()
            ask = int(input("Enter the Tenants Number For Displaying Lease Details: ")) - 1
            lst = [l1, l2, l3, l4]
            lst[ask].display_details()
        
        elif choice == 11:   # Exit
            break
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")