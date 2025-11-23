import random

def rand_elem(array):
    return array[random.randint(0,len(array)-1)]
print(rand_elem([7,9,2,4,5,6]))