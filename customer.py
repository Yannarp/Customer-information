# Define an empty dictionary to store customer information
customers = {}

# Function to add a new customer to the dictionary
def add_customer(name, email, phone):
    customers[name] = {"Email": email, "Phone": phone}
    print("Customer added successfully!")

# Function to search for a customer in the dictionary
def search_customer(name):
    if name in customers:
        print(f"Name: {name}\nEmail: {customers[name]['Email']}\nPhone: {customers[name]['Phone']}")
    else:
        print("Customer not found!")

# Function to remove a customer from the dictionary
def remove_customer(name):
    if name in customers:
        del customers[name]
        print("Customer removed successfully!")
    else:
        print("Customer not found!")

# Sample usage
add_customer("John", "john@example.com", "1234567890")
search_customer("John")
remove_customer("John")
