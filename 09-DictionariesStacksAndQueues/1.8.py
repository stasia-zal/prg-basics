price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

total=0

for item,amount in price_list.items():
    print(item,':',amount)
    total+=amount

print(round(total,2))
total=0

for item,amount in price_list.items():
    discounted=round(amount*0.9,2)
    print(f'{item}:{discounted:.2f}')
    total+=discounted

print(f'{total:.2f}')
