time=int(input('Enter the number of  hours the car was parked: '))
if time>6:
    print("the fee is  20 PLN")
elif time>=3:
    print("the fee is  15 PLN")
elif time>=1:
    print("the fee is 5 PLN")
else:
    print("the fee is  0 PLN")