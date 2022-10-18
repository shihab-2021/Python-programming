class Phone:
    manufactured = 'china'

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

my_phone = Phone('Oppo', 13000, 'blue')
print(my_phone.brand)
her_phone = Phone('iphone', 89000, 'golden')
print(her_phone.brand)