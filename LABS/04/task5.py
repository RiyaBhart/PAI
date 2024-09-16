
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.table_reservations = []
        self.customer_orders = []

    def addtomenu(self, name, price):
        self.menu_items[name] = price
        print(f"{name} has been added to the menu for Rs.{price}")

    def booktable(self, table_number, customer_name):
        reservation = {'Table ': table_number, 'Customer Name': customer_name}
        self.table_reservations.append(reservation)
        print(f"Table {table_number} reserved for {customer_name}")

    def customerorder(self, customer_name, items_ordered):
        order = {'customer name': customer_name, 'items': items_ordered}
        self.customer_orders.append(order)
        print(f"Order Taken From {customer_name}")

    def displaymenu(self):
        if not self.menu_items:
            print("Menu is Empty.")

        else:
            print("Menu: ")
            for item, price in self.menu_items.items():
                print(f"{item}: Rs. {price}")
            print("-------------\n")

    def printtablereservations(self):
        if not self. table_reservations:
            print("No table reservations.")

        else:
            print("Table Reservations: ")
            for reservations in self.table_reservations:
                print(f"Table {reservations['table_number']} reserved by reservations['customer_name']")
            print("-------------\n")
            
    def printcustomersorder(self):
        if not self.customer_orders:
            print("No customer orders.")

        else:
            print("Customer orders: ")
            for order in self.customer_orders:
                for item in order['items']:
                    print(f"  -{item}")
            print("-------------\n")

restaurant = Restaurant()

restaurant.addtomenu('Steak', 3000)
restaurant.addtomenu('Lemonade', 700)
restaurant.addtomenu('Pasta', 1800)

restaurant.booktable(1, "Abiha")
restaurant.booktable(2, "Maya")

restaurant.customerorder('Abiha', ["Steak", "Pasta"])
restaurant.customerorder('Maya', ["Fries", "Lemonade"])

restaurant.displaymenu()

print("-------------\n")

restaurant.printtablereservations

restaurant.printcustomersorder
