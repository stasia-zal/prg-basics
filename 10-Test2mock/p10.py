def f(arr):
    alls=[]
    for row in arr:
        for item in row:
            alls.append(item)
    m=min(alls)
    row_c=0
    for row in arr:
        if m in row:
            col=0
            for item in row:    
                if item==m:
                    if row_c==col:
                        return True
                    else:
                        return False
                col+=1
        row_c+=1
    


print(f([[7,8],[5,3],[9,4]]))
print(f([[7,8,5,3],[9,4,2,6]]))