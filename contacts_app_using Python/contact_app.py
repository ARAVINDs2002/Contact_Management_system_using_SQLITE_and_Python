import sqlite3

# Create a SQLite database and table to store contacts
conn = sqlite3.connect('contacts.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS contacts (name TEXT PRIMARY KEY, phone_number TEXT)''')
conn.commit()

def insert_contact(name, phone_number):
    c.execute("INSERT OR REPLACE INTO contacts (name, phone_number) VALUES (?, ?)", (name, phone_number))
    conn.commit()
    print("Contact added successfully.")

def clear_contacts():
    c.execute("DELETE FROM contacts")
    conn.commit()
    print("All contacts cleared.")

def delete_contact(name):
    c.execute("DELETE FROM contacts WHERE name=?", (name,))
    conn.commit()
    print("Contact deleted successfully.")

def add_or_update_contact(name, phone_number):
    insert_contact(name, phone_number)

def display_contacts():
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    print("\nContacts:")
    for contact in contacts:
        print(contact)

def check_contact(name):
    c.execute("SELECT phone_number FROM contacts WHERE name=?", (name,))
    result = c.fetchone()
    if result:
        print(f"phone number found!!!   {name}  : {result[0]}")
    else:
        print(f"No contact found for {name}")

while True:
    print("\n1. Insert contact")
    print("2. Clear all contacts")
    print("3. Delete a contact")
    print("4. Add or update contact details")
    print("5. Display all contacts")
    print("6. Check contact by name")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        insert_contact(name, phone_number)
    elif choice == '2':
        clear_contacts()
    elif choice == '3':
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == '4':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        add_or_update_contact(name, phone_number)
    elif choice == '5':
        display_contacts()
    elif choice == '6':
        name = input("Enter name to check: ")
        check_contact(name)
    elif choice == '7':
        conn.close()
        break
    else:
        print("Invalid choice. Please try again.")
