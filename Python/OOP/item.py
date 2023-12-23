import csv

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('./Python/OOP/items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            print(items)
            
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __repr__(self) -> str:
        return f"Item('{self.name}',{self.price},{self.quantity})"

class Phone(Item):
    pass

Item.instantiate_from_csv

print(Item.all)

phone1 = Item("jscPhoneC10",500,5)
phone2 = Item("jscPhoneC20",700,5)

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

