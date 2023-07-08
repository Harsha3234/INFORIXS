# importing the CSV file 
import csv

contact = {}  # To store the data indictionary 

def loadContacts():
    try:
        with open('contacts.txt', 'r') as file:
            reader = csv.reader(file)  # to read in CSV file
            for row in reader:
                name, number = row
                contact[name] = number  
        print("Contacts loaded successfully.")
    except FileNotFoundError:
        print("No contacts file found. Starting with an empty contact book.")

def saveContacts():
    try:
        with open('contacts.txt', 'w', newline='') as file:
            writer = csv.writer(file)  # to write in CSV file
            for name, number in contact.items():
                writer.writerow([name, number])  # Write each contact as a row in the CSV file
        print("Contacts saved successfully.")
    except IOError:
        print("Error occurred while saving contacts.")

def ShowContact():
    if not contact:
        print("Empty contact book")
    else:
        print("Name \t\t\t Contact Number")
        for name, number in contact.items():
            print(f"{name}\t\t{number}")  # to show each and every contact with name and phone number

# Load existing contacts from file
loadContacts()

while True:
    Choose = int(input("1. Add New Contact\n2. Search Contact\n3. Display Contact\n4. Edit Contact\n5. Delete Contact\n*Enter Your Choice*: "))

    if Choose == 1:
        # to add a new contact(Mobile number)
        Name = input("Enter the contact name: ")
        Number = input("Enter the mobile number: ")
        contact[Name] = Number
        saveContacts()


    elif Choose == 2:
        # to see the contact number with name
        SearchName = input("Enter the contact name to search: ")
        if SearchName in contact:
            print(f"{SearchName}'s Contact Number is: {contact[SearchName]}")
        else:
            print("Name Not Found")

    elif Choose == 3:
        # to show all contacts
        ShowContact()

    elif Choose == 4:
        # to edit a number
        EditContact = input("Enter the contact name to edit: ")
        if EditContact in contact:
            Number = input("Enter new mobile number: ")
            contact[EditContact] = Number
            saveContacts()
            print("Contact updated successfully!")
        else:
            print("Name not found in the contact book")

    elif Choose == 5:
        # To delete a contact from contacts
        DeleteContact = input("Enter the name to be deleted: ")
        if DeleteContact in contact:
            confirm = input('Do you want to delete this contact? (Y/N): ')
            if confirm.lower() == 'y':
                contact.pop(DeleteContact)
                saveContacts()
                print("Contact deleted successfully!")
            else:
                print("Deletion canceled")
        else:
            print("Name is not found in contact")

    else:
        break