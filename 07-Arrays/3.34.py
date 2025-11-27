
def idmatrix(n):
    matrix=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    for row in matrix:
        for item in row:
            print(f"{item:1}", end=" ")
        print()
idmatrix(3)
idmatrix(5)
idmatrix(8)