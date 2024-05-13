from product import Product
from inventory import Inventory
from cli import CLI
from database import Database

def main():
    
    db = Database('inventory.db')
    cli = CLI()

   
    db.create_table('products', 'id INTEGER PRIMARY KEY, name TEXT, description TEXT, price REAL')
    db.create_table('inventory', 'id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER')

    
    while True:
        user_choice = cli.display_main_menu()

        if user_choice == '1':  
            product_choice = cli.display_product_menu()

            if product_choice == '1':  
                cli.create_product()
            elif product_choice == '2':  
                Product.delete(input("Enter product ID to delete: "))
            elif product_choice == '3':  
                cli.display_all_products()  
            elif product_choice == '4':  
                cli.find_product_by_id()
            else:
                print("Invalid choice. Please try again.")

        elif user_choice == '2': 
            inventory_choice = cli.display_inventory_menu()

            if inventory_choice == '1': 
                cli.create_inventory_item()
            elif inventory_choice == '2': 
                Inventory.delete(input("Enter inventory item ID to delete: "))
            elif inventory_choice == '3': 
                cli.display_all_inventory_items()  
            elif inventory_choice == '4':  
                cli.find_inventory_item_by_id()
            else:
                print("Invalid choice. Please try again.")

        elif user_choice == '3':  
            print("You are now exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
