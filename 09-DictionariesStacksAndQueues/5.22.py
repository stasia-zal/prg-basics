import json

product = {}

# read product data from keyboard
product['Name']=input('Name: ')
product['Price']=float(input('Price: '))
product['paid']=bool(input('Paid(y/n): ').lower()=='y')
# save product data to json file
with open('product.json','w',encoding='utf-8') as file:
    json.dump(product,file)