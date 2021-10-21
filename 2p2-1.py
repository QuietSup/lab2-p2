from tabulate import tabulate


class Product:
    """Contains info about a product (price, description, dimensions)"""
    def __init__(self, price, description, dimensions):
        """Checks if price, description and dimensions aren't empty, as well as whether price has int/float type

        :param price: price of an item
        :type price: int/float
        :param description: short name of an item
        :type description: str
        :param dimensions: length x width x height
        :type dimensions: str
        """
        if not (price and description and dimensions):
            raise ValueError("empty string")

        if not isinstance(price, (int, float)):
            raise TypeError("price is wrong type")

        self.price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def product_info(self):
        """Returns a row with info about product

        :returns: the "row" with info about description, price and dimensions
        :rtype: tuple(str, str, str)
        """
        return self.description, f'${self.price}', self.dimensions


class Customer:
    """Contains info about a customer (first name, last name, patronymic, phone)"""
    def __init__(self, first_name, last_name, patronymic, phone):
        """Checks if first_name, last_name, patronymic and phone aren't empty, as well as they have str type

        :type first_name: str
        :type last_name: str
        :type patronymic: str
        :type phone: str
        """
        if not (first_name and last_name and patronymic and phone):
            raise ValueError("empty string")

        for i in (first_name, last_name, patronymic):
            if not isinstance(i, str):
                raise TypeError(f"{i} isn't string")

        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone = phone

    @property
    def show_customer(self):
        """Returns the table with info about customer"""
        head = ['first name', 'last name', 'patronymic', 'phone']
        return (tabulate([[self.first_name, self.last_name, self.patronymic, self.phone]],
                       headers=head, tablefmt="fancy_grid"))


class Order:
    """Contains info about an order including customer info and all products"""
    def __init__(self, customer, *product):
        """Checks if customer and product are entered in appropriate way

        :param customer: customer's info
        :type customer: class Customer
        :param product: info about each product
        :type product: tuple(class Product)
        """
        if not isinstance(customer, Customer):
            raise TypeError("customer is entered incorrectly")
        for i in product:
            if not isinstance(i, Product):
                raise TypeError("product is entered incorrectly")

        self.customer = customer
        self.product = product

    @property
    def total_price(self):
        """Counts a total cost of order

        :returns: a rounded sum of all products prices
        :rtype: int or float
        """
        total = 0
        for i in self.product:
            total += i.price
        return total

    @property
    def show_order(self):
        """Returns the table with info about all products in order

        :return: the table with description, price and dimensions
        :rtype: str
        """
        head = ["description", "price", "dimensions"]
        rows = []
        for i in self.product:
            rows.append(i.product_info)
        to_show = "\t\t\tORDER\n" + tabulate(rows, headers=head, tablefmt="fancy_grid")
        return to_show


customer1 = Customer("Kendall", "Jenner", "Ivanivna", "+1(001) 00 00 0000")
product1 = Product(3599.99, "Laptop", "0.59 x 11.97 x 8.36")
product2 = Product(179.99, "Case", "0.8 x 13.4 x 9.8")
product3 = Product(79.99, "Mouse", "0.5 x 2.3 x 4.5")

buy = Order(customer1, product1, product2, product3)
print(customer1.show_customer)
print(buy.show_order)
print('TOTAL PRICE:', round(buy.total_price, 2))
