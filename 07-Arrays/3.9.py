def compare(array1,array2):
    if array1==array2:
        print(f'Array1: {array1}')
        print(f'Array2: {array2}')
        print(f'Comparison: True')
        print()
    else:
        print(f'Array1: {array1}')
        print(f'Array2: {array2}')
        print(f'Comparison: False')
        print()

compare(["water","book","sky"],["water","book","sky"])
compare([True,False],[True,False,True])
compare([5,3,1], [5,3,1])
compare([3,2,1],[3,2])