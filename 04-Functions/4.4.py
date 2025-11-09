###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    sum=0
    number=str(number)
    for i in number:
        sum=sum+int(i)
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')


'''
def sum(a):
    bla=0
    for i in a:
        bla=int(i)+ bla
    return bla

number=str(abs(int(input("Enter number: "))))
print(sum(number))
'''

