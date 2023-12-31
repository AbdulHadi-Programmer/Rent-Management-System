# Rent Management System :

class Property:
    Location = "Gazderabad" # I make location a class var because my all properties belong to this area
    def __init__(self, HouseName, noOfRooms, rent):
        self.HouseName = HouseName
        self.noOfRooms = noOfRooms
        self.rent = rent
        
    def Detail(self):
        print(f'The Property Detail:\nHouseName: {self.HouseName}\nLocation: {self.Location}\nNo of Rooms: {self.noOfRooms}\nRent: {self.rent}\n')

p1 = Property("House1", 2, 15000)
p2 = Property("House2", 3, 52000)
p3 = Property("House3", 2, 15000)
p4 = Property("House4", 2, 15000)
p5 = Property("House5", 4, 60000)
p6 = Property("House6", 5, 65000)
properties = [p1, p2, p3, p4, p5, p6]

class Tenant:
    def __init__(self, name, contactNum, email):
        self.name = name
        self.contactNum = contactNum
        self.email = email
        self.rent_history = []


    def add_rent(self, rent_amount):
        self.rent_history.append(rent_amount)
        message = f'Rent of {rent_amount} added to {self.name}\'s Rental History.'
        return message
    
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


t1 = Tenant("Alex Johnson", "+922319536","alex@gmail.com") # Make object of class to store in list 
t2 = Tenant("Jane Smith", "+987654321", "jane@example.com")
t3 = Tenant("Bob Johnson", "+111222333", "bob@example.com")
t4 = Tenant("John Doe", "+123456789", "john@example.com")
t5 = Tenant("Maxwell", "+145236541", "max@gmail.com")
tenants = [t1, t2, t3, t4, t5] # Storing All tenant with the objects name 

def show_tenants():
     """Display details of all tenants."""
    for index, tenant in enumerate(tenants, start=1):
        print(f"\nTenant {index} Details:")
        tenant.person_detail()
        
def show_properties():
    """Display details of all properties."""
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
        print(f'Lease Details for {self.tenant.name}:\nProperty: {self.property.HouseName}\nDuration: {self.duration}')

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

#### Leases Detail Function:

def display_unleased_properties(unleased_properties):
    """Display details of unleased properties."""
    if unleased_properties:
        print("\nUnleased Properties:")
        for index, unleased_property in enumerate(unleased_properties, start=1):
            print(f"\nUnleased Property {index} Details:")
            unleased_property.Detail()

def display_unleased_tenants(unleased_tenants):
    """Display details of unleased tenants."""
    if unleased_tenants:
        print("\nUnleased Tenants:")
        for index, tenant in enumerate(unleased_tenants, start=1):
            print(f"\nUnleased Tenant {index} Details:")
            tenant.person_detail()

def display_valid_and_invalid_leases():
    """Display valid and invalid leases, and return unleased properties and tenants."""
    global unleased_tenants, unleased_properties
    valid_leases = []
    invalid_properties = []  # Invalid Properties
    invalid_tenants = []  # Invalid Tenants

    # Set of all properties and tenants
    all_properties = set(properties)
    all_tenants = set(tenants)

    # Iterate through leases
    for lease in leases:
        # Check if the property and tenant in the lease are present in the lists
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

    # Tenants without a lease
    unleased_tenants = all_tenants - set(l.tenant for l in leases)

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
            
    return unleased_properties, unleased_tenants

# Separate Lease Function: 
def manage_leases():
    """Manage unleased tenants and properties."""
    ask = 0
    while ask != 3:  # Continue prompting until the user chooses to exit
        ask = int(input("\nEnter the following:\n1) Display Unleased Tenants\n2) Display Unleased Properties\n3) Exit\n*) Enter the option: "))

        if ask == 1:
            display_unleased_tenants(unleased_tenants)
        elif ask == 2:
            display_unleased_properties(unleased_properties)
        elif ask == 3:
            print("Exiting...")
        else:
            print("Invalid option. Please enter a valid option.")

def update_unleased_properties():
    """Update unleased properties based on current leases."""
    global unleased_properties
    # Properties without a tenant
    unleased_properties = set(p.property for p in properties) - set(p.property for p in leases)

def connect_property_with_tenants():
    """Connect properties with tenants."""
    global leases

    # Convert sets to lists
    unleased_properties_list = list(unleased_properties)
    unleased_tenants_list = list(unleased_tenants)

    # Display unleased properties and tenants
    display_unleased_properties(unleased_properties_list)
    display_unleased_tenants(unleased_tenants_list)

    try:
        # Check if unleased tenant list is empty
        if not unleased_tenants_list:
            print("No unleased tenants found.")
            add_new_tenant = input("Do you want to add a new tenant? (yes/no): ").lower()
            if add_new_tenant == "yes":
                print("Add new Tenant: ")
                name = input('Enter The name of tenant: ')
                Num = input('Enter the Number: ')
                email = input('Enter the email: ')
                t = Tenant(name, Num, email)
                tenants.append(t)
                # Add logic to add a new tenant (you can call a function for adding a new tenant)
                pass
            else:
                print("Passing the program.")
                return

        # Get user input for connecting tenant with property
        tenant_index = int(input("Enter the Tenant Number to connect: ")) - 1
        property_index = int(input("Enter the Property Number to connect: ")) - 1
        duration = input("Enter the lease duration (e.g., 1 year, 6 months): ")

        # Create a lease object and add it to the leases list
        new_lease = Lease(unleased_tenants_list[tenant_index], unleased_properties_list[property_index], duration)
        leases.append(new_lease)

        print(f"Successfully connected {unleased_tenants_list[tenant_index].name} with {unleased_properties_list[property_index].HouseName} for {duration}.")
    except ValueError:
        print("Invalid input. Please enter valid numbers for Tenant and Property.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
def print_lease_details(leases):
    """Print lease details."""
    for index, lease in enumerate(leases, start=1):
        print(f"\nLease {index} Details:")
        lease.display_details()

# The main Menu Code :
while True:
    try:
        choice = int(input("\nEnter What you want to perform:\n1) Add new Tenant\n2) Add Property\n3) Connect Property with Tenants\n4) Show All Tenants\n5) Show All Property\n6) Remove Tenants\n7) Add Rent\n8) Show Rent History\n9) Update Tenant Information\n10) Show All Leases\n11) Exit\n*) Enter the Option:- "))

        if choice in [3, 10]:
            unleased_properties, unleased_tenants = display_valid_and_invalid_leases()
        
        if choice == 1:  # Add Tenant
            print("Add new Tenant: ")
            name = input('Enter The name of tenant: ')
            Num = input('Enter the Number: ')
            email = input('Enter the email: ')
            t = Tenant(name, Num, email)
            tenants.append(t)
            
        elif choice == 2:  # Add Property
            HouseName = input("Enter The name of House: ")
            noOfRooms = int(input(f"Enter the no of rooms in {HouseName}: "))
            rent = int(input("Enter the rent amount for the property: "))
            p = Property(HouseName, noOfRooms, rent)
            properties.append(p)
            show_properties()
            
        elif choice == 3:  # Connect Property with Tenants
            connect_property_with_tenants()
            
        elif choice == 4:  # Show All Tenants
            show_tenants()
            
        elif choice == 5:  # Show All Properties
            show_properties()
            
        elif choice == 6:  # Remove Tenants
            show_tenants()
            ask = int(input("Enter the Tenant Number To Remove: ")) - 1
            if 0 <= ask < len(tenants):
                removed_tenant = tenants.pop(ask)
                print(f"Successfully removed Tenant: {removed_tenant.name}")
                update_unleased_properties()
            else:
                print("Invalid tenant index. Please enter a valid index.")
                
        elif choice == 7:  # Add Rent
            print_lease_details(leases)
            ask = int(input("Enter the Tenants Number For Adding Rent: ")) - 1
            if 0 <= ask < len(tenants):
                rent = int(input("Enter the rent Amount: "))
                tenant = tenants[ask]
                result = tenant.add_rent(rent)
                print(result)  # Now result will contain the message
            else:
                print("Invalid tenant index. Please enter a valid index.")
            
        elif choice == 8:  # Show Rent History
            show_tenants()
            ask = int(input("Enter the Tenants Number For Showing Rent History: ")) - 1
            if 0 <= ask < len(tenants):
                tenants[ask].display_rent_history()
            else:
                print("Invalid tenant index. Please enter a valid index.")
        
        elif choice == 9:  # Update Tenant Information
            show_tenants()
            ask = int(input("Enter the Tenants Number For Upgrading Information: ")) - 1
            new_name = input('Enter the Name: ')
            new_contactNum = input('Enter the Phone Number: ')
            new_email = input('Enter the new email: ')
            tenants[ask].update_details(new_name, new_contactNum, new_email)
            show_tenants()
        
        elif choice == 10:  # Show All Leases
            unleased_properties, unleased_tenants = display_valid_and_invalid_leases()
            # display_unleased_tenants(unleased_tenants) # Not show the tenant , only the leases
        
        elif choice == 11:  # Exit
            break
        
        else:
            print("Invalid option. Please enter a valid option.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")