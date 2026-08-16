class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count +=1

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products in store={cls.count}")

    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (discount*price/100)
        print(f"final_price:{final_price}")


p1= Product("phone",20000)
p2= Product("laptop",50000)
p3= Product("mouse",500)

Product.get_count()
Product.calc_discount(p1.price,10)