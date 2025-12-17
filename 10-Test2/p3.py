def f(array2D):
    res=False
    count=0
    for array in array2D:
        row=0
        col=0
        for item in array:
            row+=item
        for array in array2D:
            col+=array[count]
        if row==col:
            res=True
        else:
            return False
        count+=1
    return res

print(f([[3,7,2],[4,2,5],[5,2,1]]))
print(f([[3,7,2],[4,2,5],[9,2,1]]))