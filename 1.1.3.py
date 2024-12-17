class Product():
    def __init__(self, product, category, price, availability):
        self.product = product
        self.category = category
        self.price = price
        self.availability = availability

    def products(self):
        return f'{self.product} {self.category} {self.price} {self.availability}'


class Order():
    def __init__(self, price, discount, tax):
        self.price = price
        self.discount = discount
        self.tax = tax

    def process_buying(self):
        return f'{self.price} {self.discount} {self.tax}'


class Customer():
    def __init__(self, user_inf, order_history):
        self.order_history = order_history
        self.user_inf = user_inf

    def custom(self):
        return f'{self.order_history} {self.user_inf}'


class ShoppingCart():
    def __init__(self, dell, to_add, all_product):
        self.dell = dell
        self.to_add = to_add
        self.all_product = all_product

    def shop_cart(self):
        return f'{self.dell} {self.to_add} {self.all_product}'


product = Product('лодка','рыбалка','20 рублей','есть в наличии')
print(product.products())

order = Order('20 рублей', '15%', '13%')
print(order.process_buying())

customer = Customer('рыбалов', 'лодка, удочка, сеть')
print(customer.custom())

shop = ShoppingCart('удалить лодка', 'добавить сети', 'лодка, удочка, сеть')
print(shop.shop_cart())
