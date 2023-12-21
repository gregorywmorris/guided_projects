class Item: 
    def __init__(self,name:str, price:float, quantiy=0):
        # run validations
        assert price >= 0
        assert quantiy >= 0

        # Assign to self object
        print(f"An instance created for {name}")
        self.name = name
        self.price = price
        self.quantity = quantiy


    def caculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone",100,5)
print(item1.caculate_total_price())

item2 = Item("Laptop",1000,5)
print(item2.caculate_total_price())

item3 = Item("PC",2000)
print(item3.caculate_total_price())