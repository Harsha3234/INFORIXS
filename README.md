# INFORIXS
1. Importing the CSV file:
# The code begins by importing the csv module, which provides functionality for working with CSV files.

2. contact Dictionary:
# This dictionary is used to store the contact data, where the contact name is the key and the corresponding mobile number is the value.

3. loadContacts() Function:
# This function is responsible for loading existing contacts from a CSV file called "contacts.txt" and populating the contact dictionary.
# It uses a try-except block to handle the case when the file is not found. If the file is found, it reads the contents using the csv.reader() function and iterates over each row.
# Each row contains a name and a number, which are then added to the contact dictionary.
# If the file is not found, it prints a message indicating that the contact book is empty.

4. saveContacts() Function:
# This function is responsible for saving the current state of the contact book (i.e., the contact dictionary) to the CSV file.
# It uses a try-except block to handle any errors that might occur during the file write operation.
# It opens the "contacts.txt" file in write mode using the open() function with the 'w' mode and 'newline=""' parameter.

5. ShowContact() Function:
# This function is responsible for displaying all the contacts in the contact book.
# It checks if the contact dictionary is empty and prints an message.
# If the dictionary is not empty, it prints a table-like format with the name and contact number for each entry in the contact dictionary.

6. Load existing contacts:
 # After defining the functions, the code calls the loadContacts() function to load any existing contacts from the "contacts.txt" file. If the file is not found, it starts with an empty contact book.

1. Main program loop:
# The code enters an infinite loop using while True.
# It prompts the user to enter their choice by displaying a menu of options (1. Add New Contact, 2. Search Contact, 3. Display Contact, 4. Edit Contact, 5. Delete Contact, or any other key to exit).
# The user's choice is stored in the Choose variable as an integer using the int(input()) function.

1. Handling user choices:
# Based on the user's choice, the code performs different actions using conditional statements (if-elif-else).

# If the choice is 1, it prompts the user to enter the contact's name and mobile number, adds the contact to the contact dictionary, and calls saveContacts() to save the updated contact book.

# If the choice is 2, it prompts the user to enter a name to search for in the contact book. It then checks if the name exists in the contact dictionary and displays the corresponding mobile number if found.

# If the choice is 3, it calls the ShowContact() function to display all the contacts in the contact book.

# If the choice is 4, it prompts the user to enter a name to edit and checks if it exists in the contact dictionary. If found, it prompts the user to enter a new mobile number, updates the contact, and calls saveContacts() to save the changes.

# If the choice is 5, it prompts the user to enter a name to delete and checks if it exists in the contact dictionary. If found, it asks for confirmation and deletes the contact if confirmed, then calls saveContacts() to save the updated contact book.

# If the choice is any other value, it breaks out of the loop, terminating the program.

Q. WHat we can learn by making this project

# How to read from and write to CSV files using Python's csv module.

# How to use dictionaries to store and manage contact information.

# How to implement a basic command-line interface for a contact management system.

# How to handle file I/O operations and handle potential errors using try-except blocks.

# How to implement functionalities such as adding contacts, searching for contacts, displaying contacts, editing contact information, and deleting contacts.

# How to implement data validation to ensure the correctness of user inputs.

# How to use loops and conditional statements to create a menu-driven program.
