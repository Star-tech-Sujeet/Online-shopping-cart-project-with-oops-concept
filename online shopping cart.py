class Product:
    def __init__(self, product_id, name, price, quantity_available):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity_available = quantity_available

    def display_details(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}, Available: {self.quantity_available}"

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"Item: [{self.product.name}], Qty: {self.quantity}, Price: ${self.product.price:.2f}, Subtotal: ${self.calculate_subtotal():.2f}"

class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.catalog = {}
        self._add_initial_products()

    def _add_initial_products(self):
        self.catalog["P001"] = Product("P001", "Laptop", 1200.00, 100)
        self.catalog["P002"] = Product("P002", "E-book: Python Basics", 25.00, 500)
        self.catalog["P003"] = Product("P003", "Mouse", 15.00, 300)
        self.catalog["P004"] = Product("P004", "TV", 12000.00, 100)
        self.catalog["P005"] = Product("P005", "E-book:  Python Advance", 35.00, 500)
        self.catalog["P006"] = Product("P006", "Keyboard", 15.00, 300)
        self.catalog["P007"] = Product("P007", "phone", 120.00, 100)
        self.catalog["P008"] = Product("P008", "E-book: java Basics", 25.00, 500)
        self.catalog["P009"] = Product("P009", "PlayStation 5", 1500.00, 300)
        self.catalog["P010"] = Product("P010", "Apple AirPods Pro", 199.99, 100)
        self.catalog["P011"] = Product("P011", "Samsung T7 1TB Portable SSD", 89.00, 500)
        self.catalog["P012"] = Product("P012", "Xbox", 1000.00, 300)
        self.catalog["P013"] = Product("P013", "Nike Air Force 1 Sneakers", 120.00, 100)
        self.catalog["P014"] = Product("P014", "LEGO Star Wars ", 169.00, 500)
        self.catalog["P015"] = Product("P015", "Nothing 3a pro ", 150.00, 300)
        self.catalog["P016"] = Product("P016", "Samsung s24 ", 170.00, 100)
        self.catalog["P017"] = Product("P017", "E-bool: c/c++ Basics", 25.00, 500)
        self.catalog["P018"] = Product("P018", "Iphone 16 pro max", 170.00, 300)
        self.catalog["P019"] = Product("P019", "Mac Book M2", 2500.00, 500)
        self.catalog["P020"] = Product("P020", "All collections of Dragon Ball Manga", 17000.00, 300)

    def display_products(self):
        print("\n--- Available Products ---")
        if not self.catalog: 
            print("No products available.")
        for p_id, p in self.catalog.items():
            print(p.display_details())
        print("--------------------------")

    def add_item(self, p_id, qty):
        if not (isinstance(qty, int) and qty > 0): 
            return print("Quantity must be a positive integer.")
        if p_id not in self.catalog: 
            return print(f"Product '{p_id}' not found in catalog.")
        prod = self.catalog[p_id]
        if prod.quantity_available < qty: 
            return print(f"Insufficient stock for {prod.name}. Available: {prod.quantity_available}")

        if p_id in self.items:
            self.items[p_id].quantity += qty
        else:
            self.items[p_id] = CartItem(prod, qty)
        prod.quantity_available -= qty
        print(f"Added/Updated '{prod.name}'. Cart quantity: {self.items[p_id].quantity}")

    def remove_item(self, p_id):
        if p_id not in self.items: 
            return print(f"Product '{p_id}' not found in cart.")
        removed_item = self.items.pop(p_id)
        removed_item.product.quantity_available += removed_item.quantity
        print(f"Removed '{removed_item.product.name}'. Stock returned.")

    def update_quantity(self, p_id, new_qty):
        if not (isinstance(new_qty, int) and new_qty >= 0): 
            return print("New quantity must be a non-negative integer.")
        if p_id not in self.items: 
            return print(f"Product '{p_id}' not found in cart.")
        
        cart_item = self.items[p_id]
        prod = cart_item.product
        old_qty = cart_item.quantity
        
        if new_qty == old_qty: 
            return print(f"Quantity for '{prod.name}' is already {new_qty}. No change needed.")

        stock_diff = new_qty - old_qty
        if stock_diff > 0 and prod.quantity_available < stock_diff:
            return print(f"Insufficient stock for {prod.name}. Need {stock_diff}.")
        
        prod.quantity_available -= stock_diff
        cart_item.quantity = new_qty

        if cart_item.quantity == 0:
            self.items.pop(p_id)
            print(f"Removed '{prod.name}' from cart.")
        else: 
            print(f"Updated '{prod.name}' from {old_qty} to {new_qty}.")

    def display_cart(self):
        print("\n--- Your Shopping Cart ---")
        if not self.items: print("Your cart is empty.")
        total_price = 0.0
        for p_id, item in self.items.items():
            print(item)
            total_price += item.calculate_subtotal()
        print(f"Grand Total: ${total_price:.2f}")
        print("--------------------------")

    def run(self):
        print("\nWelcome to Online Shopping MAll !")
        while True:
            print("\nMenu: 1.View Products \n 2.Add Item \n 3.View Cart \n 4.Update Qty \n 5.Remove Item \n 6.Checkout \n 7.Exit")
            choice = input("Enter choice: ").strip()
            if choice == '1': 
                self.display_products()
            elif choice == '2':
                p_id = input("Product ID: ").strip().upper()
                try: 
                    qty = int(input("Quantity: ").strip())
                except ValueError: 
                    print("Invalid quantity. Enter a number.")
                else: 
                    self.add_item(p_id, qty)
            elif choice == '3': 
                self.display_cart()
            elif choice == '4':
                p_id = input("Product ID to update: ").strip().upper()
                try: 
                    new_qty = int(input("New quantity: ").strip())
                except ValueError: 
                    print("Invalid quantity. Enter a number.")
                else: 
                    self.update_quantity(p_id, new_qty)
            elif choice == '5': 
                self.remove_item(input("Product ID to remove: ").strip().upper())
            elif choice == '6':
                total = sum(item.calculate_subtotal() for item in self.items.values())
                if total > 0: 
                    print(f"\nCheckout. Total: ${total:.2f}. Thank you!")
                    self.items.clear()
                else: 
                    print("Cart empty.")
            elif choice == '7': 
                print("Goodbye!") 
                break
            else: 
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ShoppingCart().run()  
