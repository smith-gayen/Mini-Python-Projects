#cafe management system.... 

#define the menue of restaurant
menue = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffe': 80,
}

#Greet the customer
print("....Welcome to my restaurant....")
print("Pizza: Rs40.\nPasta: Rs50.\nBurger: Rs60.\nSalad: Rs70.\nCoffe: Rs80.")

#initialize total by 0
order_total = 0

item_1 = input("Entet the neme of the item you want to order: ")
if item_1 in menue:
    order_total += menue[item_1]
    print(f"Your item {item_1} has been added to your order....")
else:
    print(f"Your item {item_1} is not available yet....")

another_order = input("Do you want to add another item? (Yes/no): ")
if another_order == "Yes":
    item_2 = input("Enter the neme of second item: ")
    if item_2 in menue:
        order_total += menue[item_2]
        print(f"Your item {item_2} has been added to your order....")
    else:
        print(f"Your item {item_2} is not available yet....")

print(f"The total amount of item is {order_total}.")
print("....Thank you visit again....")
