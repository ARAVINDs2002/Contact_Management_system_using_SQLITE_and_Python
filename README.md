# Please remember that while testing or using any app online use meaningfull data and dont be a fool like m...ahem..certain people i know.

# Contact Management System Documentation

# Overview

This project implements a simple contact management system using SQLite as the backend database. It allows users to perform various operations such as adding new contacts, deleting contacts, updating contact information, and checking if a contact exists by name ,all done with dictionary in python. This system is designed to be simple and make use of command line as UI.


# Database Setup
The project uses a SQLite database named contacts.db to store contact information. The database has a single table named contacts with the following schema:
👉name: The contact's name (Primary Key)

👉phone_number: The contact's phone number

# Features
The following operations are available to manage contacts:

👉Insert Contact
Adds a new contact with a given name and phone number. If a contact with the same name already exists, it is replaced with the new phone number.

👉Clear All Contacts
Deletes all contacts from the database.

👉Delete a Contact
Deletes a contact by name.

👉Add or Update Contact
Adds a new contact or updates the phone number of an existing contact.

👉Display All Contacts
Displays a list of all contacts in the database.

👉Check Contact by Name
Checks if a contact with a given name exists, and if so, displays the phone number.

👉Exit
Closes the database connection and exits the program.

How to Use

# 👉Run the Script
Execute the Python script to start the contact management system.

Select an Option

A menu will appear with different operations. Enter the corresponding number for the desired operation.

# 👉Perform the Operation

Depending on the chosen option, follow the prompts to enter information or confirm actions.

# 👉Exit
To exit the program, select option 7. This will close the database connection safely.


PLEASE UNDERSTAND THAT I HAVNT IMPLEMENTED THIS WITH A REAL WEB BASED UI OR AN APP BECAUSE I FOCUS ON MAKING ANY PROJECT DONE BY ME COMMAND LINE FOR TESTING PURPOSE AT FIRST.I KNOW COMMAND LIKE IS KINDA OLD FASHIONED BUT IT GIVES ALL POSIBLE OPERATIONS AS SAME AS DONE IN A WEB OR APP.THANKYOU FOR YOUR TIME HAVE A GOOD DAY.

