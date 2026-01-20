class product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        product.count+=1
    def get_info(self):  #instance method
        print(f"Price of {self.name} is Rs.{self.price}")
    @classmethod
    def get_count(cls):
        print(f"Total products in store is {cls.count}")
    @staticmethod
    def calc_discount(price,discount):
        print(f"Discounted  price={price-price*discount/100}")

p2=product("Laptop",1_00_000)
p3=product("Phone",1000)
p2.get_info()
product.get_count()
p2.calc_discount(p2.price,12)

