num=int(input('Number of products purchased: '))
price=float(input('Product price: '))
if num>2:
    price=price*0.75
print(f"Amount to pay: {price*num}")