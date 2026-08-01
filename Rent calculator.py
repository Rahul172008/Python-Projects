print("Welcome To Rent Calculator")
rent =int(input("Enter House Rent:"))
food =int(input("Enter Food Expense:"))
electricity=int(input("Enter Electericity Bill:"))
water = int(input("Enter  Water Bill :"))
wifi = int(input("Enter  Wifi Bill:"))
gas = int(input("Enter  Gas Bill:"))

persons= int(input("Enter The Number Of Person:"))

total = rent + food + electricity + water + gas 

if persons > 0:
    per_person=round(total/persons)
    print("\n=====BILL SUMMARY=====")
    print("House Rent: $",rent)
    print("Food Expense: $",food)
    print("Electricity Bill: $",electricity)
    print("Water Bill: $",water)
    print("Wifi Bill: $",wifi)
    print("Gas Bill: $",gas)
    print("--------------------------")
    print("Total Expense: $",total)
    print("Per Person Pay: $",per_person)
else:
    print("Number Of Persons Must Be Greater Than 0.")
