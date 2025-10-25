p=int(input("Enter price: "))
d=int(input("Enter discount %: "))
a=p-(p*d/100)
r=p-a
print(f"Price: {p}")
print(f"Discount: {d}%")
print(f"Price with discount: {a}")
print(f"Reduction: {r}")

