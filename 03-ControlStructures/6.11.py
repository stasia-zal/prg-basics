

cur=float(input('Current product price: '))
pre=int(input('Previous product price: '))
red_price=(pre-cur)/pre*100
if red_price>10:
    print("Buy the product!!")
    print(f"Product price reduced by {red_price} %")