
class Ecommerce:

    def __init__(self):
        self.products = {}
        self.purchases = []

    """
        save_product function adds a new product to the catalog or updates existing products price and name
    """
    def save_product(self, product_id, product_name, product_price):
        if product_id in self.products:
            self.products[product_id]['name'] = product_name
            self.products[product_id]['price'] = product_price
            print(f"Product with id {product_id} was updated")
        else:
            self.products[product_id] = {'name': product_name, 'price': product_price, 'quantity': 0}
            print(f"Product with id {product_id} was saved")

    """
            purchase_product function purchases an existing product, increasing the product quantity in products
            catalog and adding quantity and price to the purchases list for the history
    """
    def purchase_product(self, product_id, quantity, price):
        if product_id not in self.products:
            print(f"No product with id {product_id} found")
        else:
            self.purchases.append((quantity, price))
            self.products[product_id]['quantity'] += int(quantity)
            print(f"{quantity} units of product with id {product_id} was purchased for {price} a unit")



if __name__ == '__main__':
    ecom = Ecommerce()
    print(ecom.products)
    while True:
        command = input("Enter a command:\n")
        part = command.split()
        if part[0] == "save_product":
            ecom.save_product(part[1], part[2], float(part[3]))
        elif part[0] == "purchase_product":
            ecom.purchase_product(part[1], int(part[2]), float(part[3]))
        elif part[0] == "exit":
            break
        else:
            print("Wrong command")


