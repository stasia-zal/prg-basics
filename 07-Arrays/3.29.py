res=[]
def create_2d_arr(x,y):
    for i in range(y):
        a=[]
        for j in range(x):
            a.append(0)
        res.append(a)
    for row in res:
        for item in row:
            print(f"{item}", end=" ")  # aligned with width 2
        print()
create_2d_arr(3,5)
