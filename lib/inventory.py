from database import Database
from product import Product

class Inventory:
    def __init__(self, id, product, quantity):
        self.id = id
        self.product = product  
        self.quantity = quantity

    @staticmethod
    def create(id, product_id, quantity):
        db = Database('inventory.db')
        db.insert('inventory', {'id': id, 'product_id': product_id, 'quantity': quantity})
        db.close()

    @staticmethod
    def delete(id):
        db = Database('inventory.db')
        db.delete('inventory', f'id = {id}')
        db.close()

    @staticmethod
    def get_all():
        db = Database('inventory.db')
        inventory_items = db.select('inventory')
        db.close()
        return [Inventory(id=row[0], product=Product.find_by_id(row[1]), quantity=row[2]) for row in inventory_items]

    @staticmethod
    def find_by_id(id):
        db = Database('inventory.db')
        inventory_item = db.select('inventory', f'id = {id}')
        db.close()
        if inventory_item:
            return Inventory(id=inventory_item[0][0], product=Product.find_by_id(inventory_item[0][1]), quantity=inventory_item[0][2])
        else:
            return None
