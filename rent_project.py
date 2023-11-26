## Rent Management System:
# first there is house name that house1
# House name = house1
# tenant is rental person = Person1 
# rent = 10000 rs or whatever currency 
# Contract = 1 month or 1 year that is store in list etc
print("Rent Management System Program".center(75, " "))

def create_tenant(name, contact):
    return {"name": name, "contact": contact, "contracts": []}

def create_property(name, rent):
    return {"name": name, "rent": rent, "tenant": None}

def assign_tenant_to_property(tenant, property, duration, unit):
    tenant["contracts"].append({"property": property, "duration": duration, "unit": unit})
    property["tenant"] = tenant


def display_properties(properties):
    print("\nProperty Details:")
    for property in properties:
        tenant_info = property["tenant"]["name"] if property["tenant"] else "Vacant"
        print(f"Property: {property['name']}, Rent: {property['rent']}, Tenant: {tenant_info}")

def display_tenants(tenants):
    print("\nTenant Details:\n")
    for tenant_index, tenant in enumerate(tenants, start=1):
        print(f"Tenant {tenant_index}:\n   Name: {tenant['name']}, Contact: {tenant['contact']}, Contracts: {len(tenant['contracts'])}")
        for contract_index, contract in enumerate(tenant['contracts'], start=1):
            print(f"   Contract {contract_index}: Property: {contract['property']['name']}, Duration: {contract['duration']} {contract['unit']}")
# list of Tenant to add:
tenants = [
    create_tenant("Person1", "+92321456789"),
    create_tenant("Person2", "+92322567890"),
    create_tenant("Person3", "+92323678901"),
    create_tenant("Person4", "+92324789012")
]
# List of Properties:
properties = [
    create_property("House1", 10000),
    create_property("House2", 20000),
    create_property("House3", 15000),
    create_property("House4", 13000)
]


for i in range(len(properties)):
    duration = int(input(f"Enter the contract duration for {properties[i]['name']}: "))
    unit = input(f"Enter the unit (month/year) for {properties[i]['name']}: ").lower()
    assign_tenant_to_property(tenants[i], properties[i], duration, unit)

# display_tenants(tenants)
# display_properties(properties)

while True:
    choice = int(input('Enter The Option:\n1) Add New Tenant\n2) Remove Existing Tenant\n3) Show All Tenants\n'))
    def main():
        if choice == 1:
            name = input("Enter The name of New Tenant: ").capitilize()
            contact = input("Enter the Contact Number with Country Code: ")
            create_tenant(name, contact)
            pass # Add new tenant
        elif choice == 2:
            name = input("Enter The name of Tenant to remove: ").capitilize()
            if name in tenants:
                tenants.discard(name)
            else:
                print(f"Invalid Input\n{name} is not Found")
            pass # Remove Existing Tenant
        
        elif choice == 3:
            pass # Show All Tenants
        else :
            break
