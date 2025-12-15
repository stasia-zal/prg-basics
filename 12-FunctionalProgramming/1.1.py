###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
    res=(x+y)/2
    return res

# takes two numbers from keyboard
n1 = int(input('Enter first num: '))
n2 = int(input('Enter second num: '))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')