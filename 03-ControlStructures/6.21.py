a=int(input('Enter the amount in PLN: '))
x=a
i=1
five=0
two=0
one=0
while a>=5:
    a=a-5
    five+=1
while a>=2:
    a=a-2
    two+=1
while a>=1:
    a=a-1
    one+=1
print(f'The amount of PLN {x} in coins:')
print(f'5 PLN coins: {five}')
print(f'2 PLN coins: {two}')
print(f'1 PLN coins: {one}')