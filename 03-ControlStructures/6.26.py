import sys

pin='0805'

for i in range(1,4):
    a=input('Enter the PIN code: ')
    if pin==a:
        sys.exit('PIN is correct')
    else:
        print('PIN is incorrect.....')
    
print('Sorry, your payment card has been blocked.')