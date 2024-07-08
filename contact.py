contacts = []

def add_contact():
    contact = input("Enter the contact name to be added: ")
    phone_no = input("Enter the phone number: ")
    mail_id = input("Enter the mail ID: ")
    contacts.append({"name": contact, "phone_no": phone_no, "mail_id": mail_id})
    print(f"Contact '{contact}' is added to the list")

def delete_contact():
    contact = input("Enter the contact name to be deleted: ")
    for c in contacts:
        if c["name"] == contact:
            contacts.remove(c)
            print(f"Contact '{contact}' is deleted from the list")
            return
    print(f"Contact '{contact}' not found in the list")

def list_contacts():
    print("Contacts in the list:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone_no']}, Email: {contact['mail_id']}")

def update_contact():
    old_contact = input("Enter the contact name to update: ")
    for c in contacts:
        if c["name"] == old_contact:
            new_contact = input("Enter the new name for the contact: ")
            new_phone_no = input("Enter the new phone number: ")
            new_mail_id = input("Enter the new mail ID: ")
            c["name"] = new_contact
            c["phone_no"] = new_phone_no
            c["mail_id"] = new_mail_id
            print(f"Contact '{old_contact}' updated to '{new_contact}'")
            return
    print(f"Contact '{old_contact}' not found in the list")

def search_contact():
    search_name = input("Enter the contact name to search: ")
    for contact in contacts:
        if search_name.lower() in contact["name"].lower():
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone_no']}, Email: {contact['mail_id']}")
            return
    print(f"Contact '{search_name}' not found in the list")

while True:
    print("\n** Contact Book **")
    print("1. Add a new contact")
    print("2. Delete an existing contact")
    print("3. List the contacts")
    print("4. Update a contact")
    print("5. Search a contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        delete_contact()
    elif choice == "3":
        list_contacts()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")