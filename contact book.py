contact = {}

while True:
    print("\n===== CONTACT BOOK ======")
    print("Press 1 : For Add Contact")
    print("Press 2 : For View Contact")
    print("Press 3 : For Search Contact")
    print("Press 4 : For Update Contact")
    print("Press 5 : For Delete Contact")
    print("Press 6 : For Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        name = input("Enter Your Name : ").lower()
        number = input("Enter Your Number : ")
        contact[name] = number
        print("Contact Added Successfully!")

    elif choice == "2":
        if contact:
            print("\n===== Contact List =====")
            for name, number in contact.items():
                print("Name :", name)
                print("Number :", number)
                print("----------------------")
        else:
            print("No Contact Found!")

    elif choice == "3":
        name = input("Enter Name To Search : ").lower()

        if name in contact:
            print("Name :", name)
            print("Number :", contact[name])
        else:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter Name To Update : ").lower()

        if name in contact:
            new_number = input("Enter New Number : ")
            contact[name] = new_number
            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "5":
        name = input("Enter The Name To Delete : ").lower()

        if name in contact:
            del contact[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "6":
        print("Thank You For Using Contact Book!")
        break

    else:
        print("Invalid Choice! Please Try Again.")