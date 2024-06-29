class Inventory:
    def __init__(me, name, quantity, price, manufacture_date, color, weight, expiry_date):
        me.name = name
        me.quantity = quantity
        me.price = price
        me.manu_date = manufacture_date
        me.color = color
        me.weight = weight
        me.exp_date = expiry_date

    def display(me):
        print(f"Name of item: {me.name}")
        print(f"How many items do you have?: {me.quantity}")
        print(f"How much does the item cost?: {me.price}")
        print(f"D.O.M: {me.manu_date}")
        print(f"Color of product?: {me.color}")
        print(f"Weight of product: {me.weight}")
        print(f"Date of expiry: {me.exp_date}")

class Items(Inventory):
    pass

print(help(Items))

# speaker = Items(input("Input product name: "), input("Input quantity of items: "), input("Input price of items: "), input("D.O.M: "), input("Input product color: "), input("Input weight of product: "), input("Expiry date of product: "))
# speaker.display() 