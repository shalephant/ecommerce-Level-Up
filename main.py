import csv
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
           # print(f"Product with id {product_id} was updated")

        else:
            self.products[product_id] = {'name': product_name, 'price': product_price, 'quantity': 0}
           # print(f"Product with id {product_id} was saved")

    """
            purchase_product function purchases an existing product, increasing the product quantity in products
            catalog and adding quantity and price to the purchases dictionary for the history
    """
    def purchase_product(self, product_id, quantity, price):
        if product_id not in self.products:
            print(f"No product with id {product_id} found")
        else:
            self.purchases.setdefault(product_id, []).append((int(quantity), int(price)))
            self.products[product_id]['quantity'] += int(quantity)
           # print(f"{quantity} units of product with id {product_id} was purchased for {price} a unit")


    """
            orders product if quantity specified is lower or equal to quantity in stock it subtracts the amount
            ordered and adds quantity and price to the order history dictionary,
            but if its more it gives a message to the client that there is not enough in stock
    """
    def order_product(self, product_id, quantity):
        if product_id not in self.products:
            print(f"No product with id {product_id} found")
        elif quantity > self.products[product_id]['quantity']:
            print(f"There is not enough of the product with id {product_id} in stock")
        else:
            self.orders.setdefault(product_id, []).append((int(quantity), self.products[product_id]['price']))
            self.products[product_id]['quantity'] -= quantity
           # print(f"{quantity} units of product with the id {product_id} ordered successfully")

    """
            prints the amount of product left in the stock, if there is such product
    """
    def get_quantity_of_product(self, product_id):
        if product_id not in self.products:
            print(f"No product with id {product_id} found")
        else:
           # print(f"There is {self.products[product_id]['quantity']} units in the stock")
            print(self.products[product_id]['quantity'])
            return int(self.products[product_id]['quantity'])

    """
            for each purchase in purchase history we add up prices and quantity of specific product id
             and divide by the quantity of units that was purchased to get an average price
    """
    def get_average_price(self, product_id):
        if product_id not in self.products:
            print(f"No product with id {product_id} found")
        else:
            sum_of_money = 0
            amount_purchased = 0
            for quantity, price in self.purchases[product_id]:
                amount_purchased += quantity
                sum_of_money += price * quantity
            average_price = sum_of_money/amount_purchased
           # print(f"The average price of that product would be {average_price}")
            print(int(average_price))
            return int(average_price)


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
            for quantity, price in self.purchases[product_id]:
                amount_purchased += quantity
                purchase_total_money += price * quantity
            for quantity, price in self.orders[product_id]:
                amount_ordered += quantity
                order_total_money += price * quantity
            order_average = order_total_money/amount_ordered
            purchase_average = purchase_total_money/amount_purchased
            profit_per_unit = order_average - purchase_average
            total_profit = profit_per_unit * amount_ordered
           # print(f"Profit per unit is {profit_per_unit} and total profit from the orders is {total_profit}")
            print(int(total_profit))
            return int(total_profit)

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
       # print(f"Fewest product that is left is {fewest_product} with {min_quantity} units left")
        print(fewest_product)
        return fewest_product

    """
            loops through orders and adds up quantities of orders with same id and puts it to dictionary. 
            Then takes total quantities to list to compare and choose which has maximum amount of orders.
    """
    def get_most_popular_product(self):
        product_orders = {}
        for product in self.orders:
            product_orders.setdefault(product, int())
            for quantity, price in self.orders[product]:
                product_orders[product] += quantity
        order_amount_list = [product_orders[product] for product in product_orders]
        max_order = max(order_amount_list)
        for product in product_orders:
            if product_orders[product] == max_order:
                popular_product = self.products[product]['name']
               # print(f"The most popular product is {popular_product} with {max_order} orders")
        print(popular_product)
        return popular_product


    """
        goes through the each order placed and adds each order's details to list as tuples. purchase price is 
        calculated with average purchase price of product and that is used to calculate Cost Of Goods Sold as well
    """
    def get_orders_report(self):
        orders_report = [("ID", "Name", "Sold Quantity", "Purchase Price", "COGS", "Selling Price")]
        for product in self.orders:
            for quantity, price in self.orders[product]:
                product_id = product
                product_name = self.products[product]['name']
                quantity_sold = quantity

                purchase_sum_of_money = 0
                amount_purchased = 0
                for q, p in self.purchases[product_id]:
                    amount_purchased += quantity
                    purchase_sum_of_money += q * p

                purchase_average_price = int(purchase_sum_of_money / amount_purchased)
                cogs = int(quantity_sold * purchase_average_price)
                selling_price = price
                orders_report.append((product_id, product_name, quantity_sold, purchase_average_price, cogs, selling_price))
        print(orders_report)
        return orders_report


    """
        creates (or adds new orders if file is already created) a csv file and puts orders_report list inside
    """
    def export_orders_report(self, path="reports_order.csv"):
        report = self.get_orders_report()
        with open(path, "w", newline='') as orders_report:
            write = csv.writer(orders_report)
            write.writerows(report)


if __name__ == '__main__':
    ecom = Ecommerce()
    while True:
        command = input("Enter a command:\n")
        part = command.split()
        if part[0] == "save_product":
            ecom.save_product(part[1], part[2], int(part[3]))
        elif part[0] == "purchase_product":
            ecom.purchase_product(part[1], int(part[2]), int(part[3]))
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
        elif part[0] == "get_orders_report":
            ecom.get_orders_report()
        elif part[0] == "export_orders_report":
            ecom.export_orders_report(part[1])
        elif part[0] == "exit":
            break
        else:
            print("Wrong command")


