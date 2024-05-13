class CLI:
    def __init__(self):
        self.products = []  
        self.inventory = []  
    def display_main_menu(self):
        print("1. Product Operations")
        print("2. Inventory Operations")
        print("3. Exit Application")
        return input("Enter your choice: ")

    def display_product_menu(self):
        print("1. Create Product")
        print("2. Delete Product")
        print("3. Display All Products")
        print("4. Find Product by ID")
        return input("Enter your choice: ")

    def display_inventory_menu(self):
        print("1. Create Inventory Item")
        print("2. Delete Inventory Item")
        print("3. Display All Inventory Items")
        print("4. Find Inventory Item by ID")
        return input("Enter your choice: ")

    def get_product_details(self):
        id = input("Enter product ID: ")
        name = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: ")) 
        return id, name, description, price

    def create_product(self):
        id, name, description, price = self.get_product_details()
        new_product = {"id": id, "name": name, "description": description, "price": price}
        self.products.append(new_product)
        print(f"Product '{name}' with ID {id} created successfully!")

    def delete_product(self):
        product_id = input("Enter product ID to delete: ")
        for product in self.products:
            if product["id"] == product_id:
                self.products.remove(product)
                print(f"Product with ID {product_id} deleted successfully!")
                return
        print(f"Product with ID {product_id} not found!")

    def display_all_products(self):
        if not self.products:
            print("There are currently no products in the system.")
            return
        print("-" * 50)
        print(f"| {'Product ID':<15} | {'Product Name':<25} | {'Price':^10} |")  
        print("-" * 50)
        for product in self.products:
            print(f"| {product['id']:<15} | {product['name']:<25} | ${product['price']:.2f} |")  
        print("-" * 50)

    def find_product_by_id(self):
        product_id = input("Enter product ID to find: ")
        for product in self.products:
            if product["id"] == product_id:
                print(f"\nProduct Details:")
                print(f"  ID: {product['id']}")
                print(f"  Name: {product['name']}")
                print(f"  Description: {product['description']}")
                print(f"  Price: ${product['price']:.2f}")
                return
        print(f"Product with ID {product_id} not found!")

    def get_inventory_details(self):
        id = input("Enter inventory item ID: ")
        name = input("Enter inventory item name: ")
        description = input("Enter inventory item description: ")
        quantity = int(input("Enter inventory item quantity: "))
        return id, name, description, quantity

    def create_inventory_item(self):
        id, name, description, quantity = self.get_inventory_details()
        new_item = {"id": id, "name": name, "description": description, "quantity": quantity}
        self.inventory.append(new_item)
        print(f"Inventory item '{name}' with ID {id} created successfully!")

    def delete_inventory_item(self):
        item_id = input("Enter inventory item ID to delete: ")
        for item in self.inventory:
            if item["id"] == item_id:
                self.inventory.remove(item)
                print(f"Inventory item with ID {item_id} deleted successfully!")
                return
        print(f"Inventory item with ID {item_id} not found!")

    def display_all_inventory_items(self):
        if not self.inventory:
            print("There are currently no inventory items in the system.")
            return
        print("-" * 50)
        print(f"| {'Item ID':<15} | {'Item Name':<25} | {'Quantity':^10} |")
        print("-" * 50)
        for item in self.inventory:
            print(f"| {item['id']:<15} | {item['name']:<25} | {item['quantity']:^10} |")
        print("-" * 50)

    def find_inventory_item_by_id(self):
        item_id = input("Enter inventory item ID to find: ")
        for item in self.inventory:
            if item["id"] == item_id:
                print(f"\nInventory Item Details:")
                print(f"  ID: {item['id']}")
                print(f"  Name: {item['name']}")
                print(f"  Description: {item['description']}")
                print(f"  Quantity: {item['quantity']}")
                return
        print(f"Inventory item with ID {item_id} not found!")
