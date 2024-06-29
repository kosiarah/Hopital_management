class Inventory:
    def __init__(self, name, quantity, price, manufacture_date, color, weight, expiry_date):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.manu_date = manufacture_date
        self.color = color
        self.weight = weight
        self.exp_date = expiry_date

    def display(self):
        print(f"Name of item: ")
        print(f"How many items do you have?: ")
        print(f"How much does the item cost?: ")
        print(f"D.O.M: ")
        print(f"Color of product?: ")
        print(f"Weight of product: ")
        print(f"Date of expiry: ")

speaker = Inventory("JBL", "100", "300,000", "12/03/23", "BLACK" , "2KG", "NIL")
speaker.display