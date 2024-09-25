
class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.orders = []

    def create_order(self, order):
        self.orders.append(order)
        print(f"Order {order.order_id} created for user {self.user_name}")


class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def check_availability(self, requested_quantity):
        return self.quantity >= requested_quantity


class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user
        self.products = []
        self.status = "Pending"

    def add_product(self, product, quantity):
        if product.check_availability(quantity):
            self.products.append((product, quantity))
            product.quantity -= quantity
            print(f"Added {quantity} of {product.product_name} to order {self.order_id}")
        else:
            print(f"Product {product.product_name} is out of stock.")

    def checkout(self):
        if self.products:
            self.status = "Completed"
            print(f"Order {self.order_id} has been completed.")
        else:
            print(f"Order {self.order_id} cannot be checked out with no products.")


# Create users
user1 = User(1, "Bijay")

# Create products
product1 = Product(101, "Nike Air Jordan", 250, 10)
product2 = Product(102, "Nike Air Force 1", 220, 100)

# Create an order for the user
order1 = Order(1001, user1)

# Add products to the order
order1.add_product(product1, 1)
order1.add_product(product2, 2)

# Checkout the order
order1.checkout()

# User creates another order
user1.create_order(order1)
