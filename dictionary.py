contacts = []
name = input("enter the name:")
phone_number = input("Enter the phone number:")
email = input("enter the email address:")

contact_info = f"Name: {name}, Phone: {phone_number}, Email: {email}"

contacts.append(contact_info)
print("\nUpdated contact list:")
for contact in contacts:
    print(contact)