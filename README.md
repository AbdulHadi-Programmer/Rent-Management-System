# Rent Management System 
## Overview:
The Rent Management System is designed to manage properties, tenants, and leases in a real estate context. The system provides functionalities such as adding tenants, adding properties, connecting tenants with properties through leases, and managing rent-related operations. The core entities of the system include Tenant, Property, and Lease.

## Classes:
### 1. Property Class:
Attributes:

Location (class variable): Represents the common location for all properties.
HouseName: Name of the property.
noOfRooms: Number of rooms in the property.
rent: Rent amount for the property.
Methods:

Detail(): Displays detailed information about the property.
### 2. Tenant Class:
Attributes:

name: Name of the tenant.
contactNum: Contact number of the tenant.
email: Email address of the tenant.
rent_history: List to store the rental payment history.
Methods:

add_rent(rent_amount): Adds rent amount to the tenant's rental history.
display_rent_history(): Displays the rent payment history of the tenant.
person_detail(): Displays personal details of the tenant.
update_details(new_name, new_contactNum, new_email): Updates tenant's personal details.
### 3. Lease Class:
Attributes:

tenant: Tenant associated with the lease.
property: Property associated with the lease.
duration: Duration of the lease.
Methods:

display_details(): Displays detailed information about the lease.
update_duration(new_duration): Updates the duration of the lease.
remove_tenant(): Removes the tenant from the lease.
### Operations:
Display Details:

show_tenants(): Displays details of all tenants.
show_properties(): Displays details of all properties.
Lease Management:

connect_property_with_tenants(): Connects properties with tenants through leases.
display_unleased_properties(unleased_properties): Displays details of unleased properties.
display_unleased_tenants(unleased_tenants): Displays details of unleased tenants.
display_valid_and_invalid_leases(): Displays valid and invalid leases, and updates unleased properties and tenants.
Tenant Management:

show_tenants(): Displays details of all tenants.
remove_tenants(): Removes tenants from the system.
add_rent(): Adds rent to a tenant's rental history.
show_rent_history(): Displays rent payment history of a tenant.
update_tenant_information(): Updates tenant information.
Property Management:

show_properties(): Displays details of all properties.
Lease Display:

print_lease_details(leases): Prints details of all leases.
Menu Loop:

The main menu allows users to perform various operations by choosing the corresponding option.
## Usage Example:
The main menu continuously prompts users to select an option until they choose to exit. Options include adding tenants, adding properties, connecting properties with tenants, and managing lease, tenant, and property details. The system provides a comprehensive way to manage a real estate portfolio.
