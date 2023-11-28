## Rent Management System:
# first there is house name that house1
# House name = house1
# tenant is rental person = Person1 
# rent = 10000 rs or whatever currency 
# Contract = 1 month or 1 year that is store in list etc
print("Rent Management System Program".center(75, " "))
###################################################
def create_tenant(name, contact, unit, duration):
    return {"name": name, "contact": contact, "property": None, "duration": duration, "unit": unit}

def create_property(name, rent):
    return {"name": name, "rent": rent}

def assign_tenant_to_property(tenant, property, duration, unit):
    tenant["property"] = property
    tenant["duration"] = duration
    tenant["unit"] = unit
    property["tenant"] = tenant
    

def display_properties(properties):
    print("\nProperty Details:")
    for property in properties:
        print(f"Property: {property['name']}, Rent: {property['rent']}")   ##, Tenant: {tenant_info}")


# Two New Functions:
def connect_tenants_and_properties(tenants, properties):
    for i in range(min(len(tenants), len(properties))):
        assign_tenant_to_property(tenants[i], properties[i], tenants[i]["duration"], tenants[i]["unit"])

    if len(tenants) > len(properties):
        print("Warning: More tenants than properties. You can add new properties.")
        add_property_choice = input("Do you want to add a new property? (y/n): ").lower()

        if add_property_choice == 'y':
            # Add new property
            property_name = input("Enter the name of the new property: ").title()
            rent = int(input("Enter the rent amount for the new property: "))
            new_property = create_property(property_name, rent)
            properties.append(new_property)

            # Assign the new property to the remaining tenants
            for i in range(len(properties), len(tenants)):
                tenants[i]["property"] = new_property
                tenants[i]["duration"] = tenants[i]["duration"]
                tenants[i]["unit"] = tenants[i]["unit"]
                new_property["tenant"] = tenants[i]

            print(f"New property '{property_name}' added successfully.")

    print("\nAssigned Tenants and Properties:")
    for i, tenant in enumerate(tenants, start=1):
        property_name = tenant['property']['name'] if tenant['property'] else "N/A"
        duration = tenant['duration'] if tenant['duration'] else "N/A"
        unit = tenant['unit'] if tenant['unit'] else "N/A"
        print(f"Tenant {i}: Name: {tenant['name']}, Property: {property_name}, Duration: {duration} {unit}")

def display_tenants_properly(tenants):
    print("\nTenant Details:")
    for tenant in tenants:
        print(f"\nName: {tenant['name']}, Contact: {tenant['contact']}, Duration: {tenant['duration']} {tenant['unit']}")



# list of Tenant to add:
tenants = [
    create_tenant("Person1", "+92321456789", unit="month", duration=6),
    create_tenant("Person2", "+92322567890", unit="year", duration=2),
    create_tenant("Person3", "+92323678901", unit="month", duration=3),
    create_tenant("Person4", "+92324789012", unit="year", duration=1)
]
# List of Properties:
properties = [
    create_property("House1", 10000),
    create_property("House2", 20000),
    create_property("House3", 15000),
    create_property("House4", 13000)
]

def get_user_choice():
    while True:
        try:
            choice = int(input('Enter The Option:\n1) Add New Tenant\n2) Remove Existing Tenant\n3) Show All Tenants\n4) Show All Properties\n5) Show Tenant With Their Property\n6) Add new Property\n-> Enter the Option: '))
            return choice
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a valid integer.")


while True:
    # Var of a function:
    choice = get_user_choice()
    
    if choice == 1:
        # Add new tenant
        name = input("Enter The name of New Tenant: ").title()
        contact = input("Enter the Contact Number with Country Code: ")
        try:
            duration = int(input("Enter The Duration (Time) in num: "))
        except ValueError as e:
            print(e)
            duration = input("Enter The Duration (Time) in num: ")
            if 0 < duration < 12:
                pass
            else:
                print()
        except Exception as e:
            print(e)
            duration = input("Enter The Duration (Time) in num: ")
            
        unit = input("Enter The Time Period (Month/year): ").lower()
        # New Tenant Created 
        new = create_tenant(name, contact, unit, duration)
        tenants.append(new)
        print(f"Tenant {name} added successfully.")
        if len(properties) > len(tenants):
            print("The number of properties is already greater than the number of tenants.")
        else:
            # Add New Property
            name = input("Enter The name of New Tenant: ").title()
            rent = int(input("Enter The Rent Amount: "))
            new_property = create_property(name, rent)
            properties.append(new_property)
            print("Property added successfully.")
        pass
    
    elif choice == 2:
    # Remove Existing Tenant
        name = input("Enter The name of Tenant to remove: ").title()
        for tenant in tenants:
            if tenant["name"] == name:
                tenants.remove(tenant)
                print(f"Tenant {name} removed successfully.")
                break
        else:
            print(f"Tenant {name} not found.")

    elif choice == 3:
        display_tenants_properly(tenants)
        
    elif choice == 4:
        display_properties(properties)
        
    elif choice == 5:
        # 
        # print("\nAssigned Tenants and Properties:")
        # for i, tenant in enumerate(tenants):
        #     print(f"Tenant {i}: Name: {tenant['name']}, Property: {tenant['property']}, Duration: {tenant['duration']}")
        #
        a = connect_tenants_and_properties(tenants, properties)
        print(a)
    
    elif choice == 6:
        name = input("Enter The Properties Name: ")
        rent = int(input("Enter the Rent Amount: "))
        cp = create_property(name, rent)
        properties.append(cp)

    else:
        break  # Exit the loop if the choice is not 1, 2, or 3

