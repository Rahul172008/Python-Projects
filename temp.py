import pymongo
client=pymongo.MongoClient('mongodb://localhost:27017')
db=client["tbRecordSystem"]
collection=db["tbStudent"]

i=1
while(i):
    print("Press 1: for insert student record=")
    print("Press 2: for delete student record=")
    print("Press 3: for search student record=")
    print("Press 4: for display student record=")
    print("Press 5: for update student record=")
     

    choice=int(input("Enter your choice="))

    if choice == 1:
        name=input("Enter the name=")
        phone=input("Enter the phone")
        address=input("Enter the address")

        dict1={
            "Name":name,
            "Phone":phone,
            "Address":address
        }

        collection.insert_one(dict1)
        print("Record inserted sucessfully.")

    elif choice ==2:
        name=input("Enter the name= ")

        collection.delete_one({"Name":name})
        print("Record deleted sucessfully")

    elif choice ==3:
        name=input("Enter the name")
        result=collection.find_one({"Name":name})
        print(result)

    elif choice ==4:
        result=collection.find()
        for data in result:
            print(data)

    elif choice==5:
            name=input("Enter the name=")
            phone=input("Enter the phone=")
            collection.update_one({"Name":name},{"$set":{"Phone":phone}})
            print("Record has been updated")
    else:
        print("Invalid Choice")

    i=int(input("Press 1: for more loop , press 0: for exit="))