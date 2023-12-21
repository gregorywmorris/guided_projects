class Item: 
    # Class attribute
    discount_rate = 0.8
    all = []

    def __init__(self,name:str, price:float, quantiy=0) -> None:

        # Run validations
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantiy >= 0, f"Quantity {quantiy} is not greater than 0"

        # Instance attributes
        print(f"An instance created for {name}")
        self.name = name
        self.price = price
        self.quantity = quantiy
        
        # actions to exicute
        Item.all.append(self)


    def caculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.discount_rate
    
    def __repr__(self) -> str:
        return f"Item('{self.name}',{self.price},{self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
