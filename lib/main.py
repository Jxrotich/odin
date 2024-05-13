from product import Product
from inventory import Inventory
from cli import CLI
from database import Database

def main():
    # Create Database and CLI objects
    db = Database('inventory.db')
    cli = CLI()

    # Create products table
    db.create_table('products', 'id INTEGER PRIMARY KEY, name TEXT, description TEXT, price REAL')

    # Main application loop
    while True:
        user_choice = cli.display_main_menu()

        if user_choice == '1':  
            product_choice = cli.display_product_menu()

            if product_choice == '1':  
                Product.create(*cli.get_product_details())
            elif product_choice == '2':  
                Product.delete(cli.get_product_id())
            elif product_choice == '3':  
                cli.display_all_products()  
            elif product_choice == '4':  
                product = Product.find_by_id(cli.get_product_id())
                cli.display_product(product) if product else print("Product not found.")
            else:
                print("Invalid choice. Please try again.")

        elif user_choice == '2': 
            inventory_choice = cli.display_inventory_menu()

            if inventory_choice == '1': 
                Inventory.create(*cli.get_inventory_details())
            elif inventory_choice == '2': 
                Inventory.delete(cli.get_inventory_item_id())
            elif inventory_choice == '3': 
                cli.display_all_inventory_items()  
            elif inventory_choice == '4':  
                item = Inventory.find_by_id(cli.get_inventory_item_id())
                cli.display_inventory_item(item) if item else print("Inventory item not found.")
            else:
                print("Invalid choice. Please try again.")

        elif user_choice == '3':  
            print("You are now exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
