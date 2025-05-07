class Dish:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.price}, {self.category}"

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.ordered_dishes = []
        self.status = 'Pending'

    def add_dish(self, dish):
        self.ordered_dishes.append(dish)

    def calculate_total(self):
        total = sum(dish.price for dish in self.ordered_dishes)
        return total

    def view_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print('Ordered dishes: ')
        for dish in self.ordered_dishes:
            print(dish)
        print(f"Total: {self.calculate_total()}")

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.order_history = []

    def place_order(self, restaurant, dishes):
        order_id = len(restaurant.orders) + 1  # Assign order ID based on the existing number of orders
        order = Order(self, order_id)  # Use order_id
        for dish in dishes:
            order.add_dish(dish)
        restaurant.place_order(order)
        self.order_history.append(order)  # Add the order to order_history once
        return order

class Restaurant:
    def __init__(self):
        self.menu = []
        self.orders = []

    def add_dish_to_menu(self, dish):
        self.menu.append(dish)

    def place_order(self, order):
        self.orders.append(order)

    def view_menu(self):
        print('-----Restaurant Menu-----')
        for dish in self.menu:
            print(dish)

    def view_orders(self):
        for order in self.orders:
            order.view_order()

# Create restaurant and dishes
restaurant1 = Restaurant()

dish1 = Dish("Mel", 70, 1)
dish2 = Dish("Lol", 100, 2)
dish3 = Dish("Yogurt", 200, 1)

# Create customer and place an order
customer = Customer("Max", "max123@gmail.com")

# Add dishes to restaurant menu
restaurant1.add_dish_to_menu(dish1)
restaurant1.add_dish_to_menu(dish2)
restaurant1.add_dish_to_menu(dish3)

# View restaurant menu
restaurant1.view_menu()

# Customer places an order
order = customer.place_order(restaurant1, [dish1, dish2])

# View the placed order
order.view_order()

# View all orders in the restaurant
restaurant1.view_orders()