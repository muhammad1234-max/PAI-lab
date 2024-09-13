class restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = {}
        
    def add_item_to_menu(self,item,price):
        self.menu_items[item] = price
        print(f"Item {item} added to menu with price {price}")
        
    def book_tables(self,customer_name, table_number):
        if table_number not in self.book_table:
            self.book_table.append(table_number)
            print(f"table {table_number} has been booked for {customer_name}")
        else:
            print(f"table {table_number} is already bookes")
            
    def customer_order(self,customer_name, items):
        if customer_name not in self.customer_orders:
            self.customer_orders[customer_name]=[] #empty list for as the value of the key which is customer name
        self.customer_orders[customer_name].extend(items) #adding a list of all the items the customer ordered
        print(f"Order for {customer_name} added: {items}")
        
    def print_menu(self):
        print("\n-----Menu-----")
        for item,price in self.menu_items.items(): #only printing the items from the menu_items dictionary
            print(f"{item},{price}")
        print("-----end-----\n")
        
    def print_table_reservations(self):
        print("\n---table reservations---")
        for table in self.book_table:
            print(f"table {table} is reserved")
        print("-----------------------")
    
    def print_customer_order(self):
        print("\n---customer order---")
        for customer, orders in self.customer_orders.items():
            print(f"{customer} ordered: {orders}")
        print("--------------------")
        

burger_boss = restaurant() #instance of the class
#demonstrating some basic functionalities
burger_boss.add_item_to_menu("beef burger",1200)
burger_boss.add_item_to_menu("chicken burger",1100)
burger_boss.add_item_to_menu("loaded fries",600)
burger_boss.add_item_to_menu("gourmet burger",2000)
burger_boss.add_item_to_menu("slushie",400)

burger_boss.book_tables("Muhammad",4)
burger_boss.book_tables("Murtaza",8)
burger_boss.book_tables("Daniyal",2)

burger_boss.customer_order("Muhammad",["beef burger","loaded fries","slushie"])
burger_boss.customer_order("Murtaza",["chicken burger","gourmet burger"])

burger_boss.print_menu()
burger_boss.print_table_reservations()
burger_boss.print_customer_order()
