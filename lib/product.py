from database import Database

class Product:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    @staticmethod
    def create(id, name, description, price):
        db = Database('inventory.db')
        db.insert('products', {'id': id, 'name': name, 'description': description, 'price': price})
        db.close()

    @staticmethod
    def delete(id):
        db = Database('inventory.db')
        db.delete('products', f'id = {id}')
        db.close()

    @staticmethod
    def get_all():
        db = Database('inventory.db')
        products = db.select('products')
        db.close()
        return [Product(id=row[0], name=row[1], description=row[2], price=row[3]) for row in products]

    @staticmethod
    def find_by_id(id):
        db = Database('inventory.db')
        product = db.select('products', f'id = {id}')
        db.close()
        if product:
            return Product(id=product[0][0], name=product[0][1], description=product[0][2], price=product[0][3])
        else:
            return None
