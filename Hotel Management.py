print("Welcome to our Hotel")

menu = {
    "Pasta": 110,
    "Burger": 70,
    "Pizza": 150,
    "Salad": 50,
    "Coffee": 80
}

print("Pasta: 110")
print("Burger: 70")
print("Pizza: 150")
print("Salad: 50")
print("Coffee: 80")

order_total = 0

item_1 = input("Enter the item which you want to order: ").title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"The order item {item_1} is not available yet")

another_order = input("Do you want to order something else? (Yes/No): ").lower()

if another_order == "yes":
    item_2 = input("Enter the name of second item: ").title()

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"The order item {item_2} is not available yet")

print(f"The total amount to pay is {order_total}")