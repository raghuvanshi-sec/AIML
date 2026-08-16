class Laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"Laptop has {cls.storage_type} storage")


    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @staticmethod
    def calc_final_price(price,discount):
       final_price= price- (discount*price/100)
       print(f"final_price:{final_price}")

L1 = Laptop("16gb","512gb")
L2 = Laptop("8gb","256gb")

Laptop.get_storage_type()

L1.calc_final_price(40_000,10)