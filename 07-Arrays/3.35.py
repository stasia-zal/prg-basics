a=[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
b=[
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 0],
]
c=[[5, 6, 7, 8]]
'''
def transpose_matrix(m):
    for row in range(len(m)):
        for col in range(row+1,len(m[0])):
            m[row][col],m[col][row]=m[col][row],m[row][col]
    for row in m:
        for item in row:
            print(f"{item:1}", end=" ")  
        print()
WORKS ONLY FOR SQUARE MATRICES''' 


def transpose_matrix(m):  #2x3
    new=[]
    for col in range(len(m[0])):  #2
        newrow=[]
        for row in range(len(m)): #1 to 3
            newrow.append(m[row][col])
        new.append(newrow)
    for a in new:
        for item in a:
            print(f"{item:1}", end=" ")  
        print()

transpose_matrix(a)
transpose_matrix(b)
transpose_matrix(c)
