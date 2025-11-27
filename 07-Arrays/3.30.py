res=[]
def create_2d_arr(x,y):
    x+=1
    y+=1
    for i in range(1,x):
        a=[]
        for j in range(1,y):
            a.append(i*j)
        res.append(a)
    for row in res:
        for item in row:
            print(f"{item:2}", end=" ")  # aligned with width 2
        print()
create_2d_arr(5,5)