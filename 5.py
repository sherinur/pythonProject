class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self.__description = description
        self.__units_in_inventory = units_in_inventory
        self.__price = price

    def __str__(self):
        return f"Description: {self.__description}\nUnits in Inventory: {self.__units_in_inventory}\nPrice: ${self.__price:.2f}"

item1 = RetailItem("Jacket", 12, 59.95)
item2 = RetailItem("Designer Jeans", 40, 34.95)
item3 = RetailItem("Shirt", 20, 24.95)

print("Item #1:")
print(item1)
print("\nItem #2:")
print(item2)
print("\nItem #3:")
print(item3)