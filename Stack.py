'''def push(stack, element):
    stack.insert(0, element)
    return stack

def pop(stack):
    if len(stack) == 0:
        return None
    else:
        return stack.pop(0)   


stack = []   

while True:
    print("\n===== Stack Menu =====")
    print("1. Push Element")
    print("2. Pop Element")
    print("3. Display Stack")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter element to push: ")
        push(stack, item)
        print("Element pushed successfully.")

    elif choice == '2':
        item = pop(stack)
        if item is None:
            print(" Stack Underflow! Stack is empty.")
        else:
            print(" Popped element:", item)

    elif choice == '3':
        print("Current Stack (top at 0th index):", stack)

    elif choice == '4':
        print("Exiting program. Goodbye ")
        break

    else:
        print("Invalid choice! Please try again.")'''



def AddCustomer(customerName, Customer):
    """
    Adds a new customer (PUSH operation)
    Top of stack = last element
    """
    customerName.append(Customer)
    print(f"Customer '{Customer}' added successfully.")

def DeleteCustomer(customerName):
    """
    Deletes a customer (POP operation)
    Removes the last added customer
    """
    if len(customerName) == 0:
        print("No customers to delete (Stack Underflow).")
    else:
        removed = customerName.pop()
        print(f" Customer '{removed}' deleted successfully.")

customerName = []

while True:
    print("\n===== Customer Stack Menu =====")
    print("1. Add Customer (Push)")
    print("2. Delete Customer (Pop)")
    print("3. Display Customers")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter customer name: ")
        AddCustomer(customerName, name)

    elif choice == '2':
        DeleteCustomer(customerName)

    elif choice == '3':
        if len(customerName) == 0:
            print("No customers in the list.")
        else:
            print("Current Customers (bottom → top):", customerName)

    elif choice == '4':
        print("Exiting program. Goodbye ")
        break

    else:
        print("Invalid choice! Please try again.")

