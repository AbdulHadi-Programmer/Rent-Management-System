## Rent Management System:
# first there is house name that house1
# House name = house1
# tenant is rental person = Person1 
# rent = 10000 rs or whatever currency 
# Contract = 1 month or 1 year that is store in list etc

print("Rent Management System Program".center(75, " "))
# create new tenant whenever function call
def create_tenant(name, contact):
    return {"name": name, "contact": contact, "contracts": []}

# create new property with tenant name and tenant
def create_property(name, rent):
    return {"name": name, "rent": rent, "tenant": None}

# create assign tenant to property
def assign_tenant_to_property(tenant, property):
    tenant["contracts"].append(property)
    property["tenant"] = tenant

# Display Tenants
def display_tenants(tenants):
    print("\nTenant Details:")
    for tenant in tenants:
        print(f"Name: {tenant['name']}, Contact: {tenant['contact']}, Contracts: {len(tenant['contracts'])}")

# Display Properties
def display_properties(properties):
    print("\nProperty Details:")
    for property in properties:
        tenant_info = property["tenant"]["name"] if property["tenant"] else "Vacant"
        print(f"Property: {property['name']}, Rent: {property['rent']}, Tenant: {tenant_info}")

####################################
#              Tenant              #
#################################### 
tenants = [
    create_tenant("Person1", "+92321456789"),
    create_tenant("Person2", "+92322567890"),
    create_tenant("Person3", "+92323678901"),
    create_tenant("Person4", "+92324789012")
]
####################################
#            Properties            #
#################################### 
properties = [
    create_property("House1", 10000),
    create_property("House2", 20000),
    create_property("House3", 15000),
    create_property("House4", 13000)
]
#################################### 
#        Functions to call         #
#################################### 
assign_tenant_to_property(tenants[0], properties[0])
assign_tenant_to_property(tenants[1], properties[1])
assign_tenant_to_property(tenants[2], properties[2])
assign_tenant_to_property(tenants[3], properties[3])
## Using loop to print the tenant and properties


##########################################
#      Display Tenant and Properties     #
##########################################
# display_tenants(tenants)
# display_properties(properties)

