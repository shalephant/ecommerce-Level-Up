
class Ecommerce:

    def __init__(self):
        self.products = {}
        self.purchases = {}
        self.orders = {}

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
            self.purchases.setdefault(product_id, []).append((int(quantity), self.products[product_id]['price']))
            self.products[product_id]['quantity'] += int(quantity)
            print(f"{quantity} units of product with id {product_id} was purchased for {price} a unit")


    """
            order_product function if quantity specified is lower or equal to quantity in stock it subtracts the amount
            ordered, but if its more it gives a message to the client that there is not enough in stock
    """
    def order_product(self, product_id, quantity):
        if product_id not in self.products:
            print(f"No product with id {product_id} found")
        elif quantity > self.products[product_id]['quantity']:
            print(f"There is not enough of the product with id {product_id} in stock")
        else:
            self.orders.setdefault(product_id, []).append((int(quantity), self.products[product_id]['price']))
            self.products[product_id]['quantity'] -= quantity

            print(f"{quantity} units of product with the id {product_id} ordered successfully")
            print(self.orders)


    """
            prints the amount of product left in the stock, if there is such product
    """
    def get_quantity_of_product(self, product_id):
        if product_id not in self.products:
            print(f"No product with id {product_id} found")
        else:
            print(f"There is {self.products[product_id]['quantity']} units in the stock")


    """
            for each purchase in purchase history we add up prices and quantity for those prices and divide
            by the quantity of units that was purchased to get an average price
    """
    def get_average_price(self, product_id):
        if product_id not in self.products:
            print(f"No product with id {product_id} found")
        else:
            sum_of_money = 0
            amount_purchased = 0
            for purchase in self.purchases:
                amount_purchased += purchase[0]
                sum_of_money += purchase[1] * purchase[0]
            average_price = sum_of_money/amount_purchased
            print(f"The average price of that product would be {average_price}")


    """
            We find average price of ordered products subtract average price of purchased products from it to
            find average profit per unit. We do the same thing with total prices to find total profit
    """
    def get_product_profit(self, product_id):
        if product_id not in self.products:
            print(f"No product with id {product_id} found")
        else:
            order_total_money = 0
            purchase_total_money =0
            amount_ordered = 0
            amount_purchased = 0
            for purchase in self.purchases:
                amount_purchased += purchase[0]
                purchase_total_money += purchase[1] * purchase[0]
            for order in self.orders:
                amount_ordered += order[0]
                order_total_money += order[1] * order[0]
            order_average = order_total_money/amount_ordered
            purchase_average = purchase_total_money/amount_purchased
            profit_per_unit = order_average - purchase_average
            total_profit = profit_per_unit * amount_ordered
            print(f"Profit per unit is {profit_per_unit} and total profit from the orders is {total_profit}")


    """
            loop through products dictionary to and add quantities to list to find minimum quantity
            and take the name from the list that has minimum quantity left
    """
    def get_fewest_product(self):
        prod_quantities = [self.products[product]['quantity'] for product in self.products]
        min_quantity = min(prod_quantities)
        for product in self.products:
            if self.products[product]['quantity'] == min_quantity:
                fewest_product = self.products[product]['name']
        print(f"Fewest product that is left is {fewest_product} with {min_quantity} units left")





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
        elif part[0] == "order_product":
            ecom.order_product(part[1], int(part[2]))
        elif part[0] == "get_quantity_of_product":
            ecom.get_quantity_of_product(part[1])
        elif part[0] == "get_average_price":
            ecom.get_average_price(part[1])
        elif part[0] == "get_product_profit":
            ecom.get_product_profit(part[1])
        elif part[0] == "get_fewest_product":
            ecom.get_fewest_product()
        elif part[0] == "get_most_popular_product":
            ecom.get_most_popular_product()
        elif part[0] == "exit":
            break
        else:
            print("Wrong command")


