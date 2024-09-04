class ClothingItem:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"ID: {self.item_id}, Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}")

class ClothingStore:
    def __init__(self):
        self.inventory = []

    def add_item(self):
        item_id = input("Enter item ID: ")
        name = input("Enter item name: ")
        price = float(input("Enter item price: $"))
        quantity = int(input("Enter item quantity: "))
        self.inventory.append(ClothingItem(item_id, name, price, quantity))
        print(f"{name} has been added to inventory.")

    def display_inventory(self):
        if not self.inventory:
            print("No items in inventory.")
        else:
            print("\n=== Inventory ===")
            for item in self.inventory:
                item.display()

    def sell_item(self):
        item_id = input("Enter item ID to sell: ")
        quantity = int(input("Enter quantity to sell: "))
        for item in self.inventory:
            if item.item_id == item_id:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    print(f"Sold {quantity} of {item.name}.")
                else:
                    print(f"Not enough stock for {item.name}.")
                return
        print("Item not found.")

    def menu(self):
        while True:
            print("\n=== Clothing Store Management System ===")
            print("1. Add Item")
            print("2. Display Inventory")
            print("3. Sell Item")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.display_inventory()
            elif choice == '3':
                self.sell_item()
            elif choice == '4':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    store = ClothingStore()
    store.menu()
