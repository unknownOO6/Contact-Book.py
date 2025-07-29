# Task 5 - Contact Book 📒
# CodSoft Internship
# Made by a student who keeps losing friends' phone numbers 😭

import os

filename = "contacts.txt"  # text file to store contacts

def load_contacts():
    contacts = []
    if os.path.exists(filename):
        file = open(filename, "r")
        lines = file.readlines()
        for line in lines:
            contact = line.strip().split("|")
            if len(contact) == 4:
                contacts.append(contact)
        file.close()
    return contacts

def save_contacts(contacts):
    f = open(filename, "w")
    for c in contacts:
        f.write("|".join(c) + "\n")
    f.close()

def show_contacts(contacts):
    if len(contacts) == 0:
        print("\n📭 No contacts saved yet.\n")
    else:
        print("\n=== Contact List ===")
        for i in range(len(contacts)):
            print(str(i+1) + ". Name: " + contacts[i][0])
            print("   Phone: " + contacts[i][1])
            print("   Email: " + contacts[i][2])
            print("   Address: " + contacts[i][3])
            print("----------------------")
        print()

def add_contact(contacts):
    print("\nAdd New Contact 📥")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    contacts.append([name, phone, email, address])
    save_contacts(contacts)
    print("Contact saved! ✅\n")

def delete_contact(contacts):
    show_contacts(contacts)
    try:
        n = int(input("Enter contact number to delete: "))
        if n > 0 and n <= len(contacts):
            deleted = contacts.pop(n - 1)
            save_contacts(contacts)
            print("Deleted contact: " + deleted[0] + " 🗑️\n")
        else:
            print("That number doesn't exist!\n")
    except:
        print("Please enter a valid number 😅\n")

def search_contact(contacts):
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for c in contacts:
        if keyword in c[0].lower() or keyword in c[1]:
            print("Found: " + c[0] + " | " + c[1] + " | " + c[2])
            found = True
    if not found:
        print("No match found 😕\n")

def update_contact(contacts):
    show_contacts(contacts)
    try:
        num = int(input("Which contact number to update? "))
        if num > 0 and num <= len(contacts):
            contact = contacts[num - 1]
            print("Leave blank to keep existing info 👇")
            new_name = input("New Name (" + contact[0] + "): ") or contact[0]
            new_phone = input("New Phone (" + contact[1] + "): ") or contact[1]
            new_email = input("New Email (" + contact[2] + "): ") or contact[2]
            new_address = input("New Address (" + contact[3] + "): ") or contact[3]
            contacts[num - 1] = [new_name, new_phone, new_email, new_address]
            save_contacts(contacts)
            print("Contact updated 👍\n")
        else:
            print("That contact number doesn't exist!\n")
    except:
        print("Invalid input... try a number 🙃\n")

def main():
    print("📒 Welcome to My Contact Book 📱")
    contacts = load_contacts()

    while True:
        print("\n==== MENU ====")
        print("1. Show Contacts")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            update_contact(contacts)
        elif choice == "6":
            print("Goodbye! 👋 Stay in touch!")
            break
        else:
            print("That's not even an option 😐\n")

if __name__ == "__main__":
    main()
