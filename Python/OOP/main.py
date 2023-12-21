class Item: 
    # Class attribute
    discount_rate = 0.8

    def __init__(self,name:str, price:float, quantiy=0):

        # Run validations
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantiy >= 0, f"Quantity {quantiy} is not greater than 0"

        # Assign to self object
        print(f"An instance created for {name}")
        self.name = name
        self.price = price
        self.quantity = quantiy


    def caculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.discount_rate



item1 = Item("Phone",100,10)
item1.apply_discount()
print(item1.caculate_total_price())

item2 = Item("Laptop",1000,10)
item2.discount_rate = 0.7
item2.apply_discount()
print(item2.caculate_total_price())

item3 = Item("PC",2000)
print(item3.caculate_total_price())