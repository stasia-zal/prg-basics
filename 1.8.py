price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
    }
for item,price in price_list.items():
    print(item,':',price)
total=0
for price in price_list.values():
    total+=price
print(round(total,2))
for item,price in price_list.items():
    price_list[item]=round(price,2)
for item,price in price_list.items():
    print(item,':',price)
for item,price in price_list.items():
    price_list[item]=price*0.9
for item,price in price_list.items():
    price_list[item]=round(price,1)
for item,price in price_list.items():
    print(item,':',price)
total=0
for price in price_list.values():
    total+=price
print(round(total,2))
