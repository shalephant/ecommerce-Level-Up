class Ecommerce:
    def __init__(self):
        self.products = {}

    def save_product(self, product_id, product_name, product_price):
        if product_id in self.products:
            self.products[product_id]['name'] = product_name
            self.products[product_id]['price'] = product_price
            print(f"Product with id {product_id} was updated")
        else:
            self.products[product_id] = product_id
            self.products[product_id] = {'name': product_name}
            self.products[product_id] = {'price': product_price}
            print(f"Product with id {product_id} was saved")


if __name__ == '__main__':
    ecom = Ecommerce()
    print(ecom.products)
    while True:
        command = input("Enter a command:\n")
        part = command.split()
        if part[0] == "save_product":
            ecom.save_product(part[1], part[2], float(part[3]))
        elif part[0] == "exit":
            break
        else:
            print("Wrong command")


