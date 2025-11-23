def occurs(number,array):
    if number in array:
        return True
    else: 
        return False
arr=[15, 38, 7, 23, 14]
a=int(input('Enter number: '))
print('Array: ',*arr)
print(f'Result: number {a} {"is" if occurs(a, arr) else "isn't" } in the array')