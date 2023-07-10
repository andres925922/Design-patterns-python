class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls("%s - franchise" % store.name)

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        items = store.items
        sum_of_items_prices = sum(list(map(lambda i: i['price'], items)))

        # It should be in the format 'NAME, total stock price: TOTAL'
        return "%s, total stock price: %s" % (store.name, sum_of_items_prices)
    
store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)
 
print(Store.franchise(store))  # returns a Store with name "Test - franchise"
print(Store.franchise(store2))  # returns a Store with name "Amazon - franchise"
 
print(Store.store_details(store))  # returns "Test, total stock price: 0"
print(Store.store_details(store2))  # returns "Amazon, total stock price: 160"
# Store.store_details(store2)