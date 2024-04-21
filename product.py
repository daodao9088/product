# product.py

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_product_id(self):
        return self.product_id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity


class InventoryManagementSystem:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                self.products.remove(product)
                break

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def get_all_products(self):
        return self.products


# 创建库存管理系统实例
ims = InventoryManagementSystem()

# 添加产品
product1 = Product(1, "iPhone", 999, 10)
product2 = Product(2, "MacBook Pro", 1999, 5)

ims.add_product(product1)
ims.add_product(product2)

# 获取所有产品
all_products = ims.get_all_products()
for product in all_products:
    print("Product ID:", product.get_product_id())
    print("Name:", product.get_name())
    print("Price:", product.get_price())
    print("Quantity:", product.get_quantity())
    print()

# 更新产品数量
product1.set_quantity(8)
product2.set_quantity(3)

# 再次获取所有产品
all_products = ims.get_all_products()
for product in all_products:
    print("Product ID:", product.get_product_id())
    print("Name:", product.get_name())
    print("Price:", product.get_price())
    print("Quantity:", product.get_quantity())
    print()
