#Programmer: Alethea Lo
#Date: 5/1/2025
#Title: Phone Book Database
def display_menu():
    print("\nPhonebook CRUD Application")
    print("1. Add a new contact")
    print("2. Lookup a contact's phone number")
    print("3. Update a contact's phone number")
    print("4. Delete a contact")
    print("5. Exit")


def main():
    create_table()
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            add_contact(name, phone_number)
            print(f"{name} has been added to the phonebook.")

        elif choice == '2':
            name = input("Enter the name of the person to lookup: ")
            lookup_contact(name)

        elif choice == '3':
            name = input("Enter the name of the person to update: ")
            new_phone_number = input("Enter the new phone number: ")
            update_contact(name, new_phone_number)
            print(f"{name}'s phone number has been updated.")

        elif choice == '4':
            name = input("Enter the name of the person to delete: ")
            delete_contact(name)
            print(f"{name} has been deleted from the phonebook.")

        elif choice == '5':
            print("Exiting the phonebook app.")
            break

        else:
            print("Invalid option. Please try again.")



if __name__ == "__main__":
    main()