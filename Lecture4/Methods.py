#Instance, Class and static methods

class laptop:
    storage_type="ssd"
    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage

    @classmethod
    def get_storage_type(cls):
        print(f"Storage type={cls.storage_type}")

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}" )
    
    @staticmethod
    def calc_discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"Discounted price={final_price}")

    

l1=laptop("16gb","512gb")
'''
l2=laptop("8gb","256gb")
l1.get_info()
''' 
l1.get_storage_type()
l1.calc_discount(40_000,10)

#Instance methods can access class as well as the instance attributes

#Class methods have 'cls' as first parameter and they can access class attributes only
#Decorater:@classmethod

#Static Methods dont have self or cls parameters, they have no compulsory paramaters
#They cannot access instance attributes and class attributes
#@staticmethod is the decorater
#Logically tied up to class


