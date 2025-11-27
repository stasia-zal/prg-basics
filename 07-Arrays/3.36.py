a=[[2, 3],
[1 ,5]]
b=[[5, 0, 3 ,7, 5],
[9, 0, 9, 1, 2]]
c=[[2, 1],
[3 ,5],
[7 ,4],
[2, 6]]
def twoDtooneD(arr):
    newarr=[]
    for row in arr:
        for item in row:
                newarr.append(item)
    for a in newarr :
        for item in a:
            print(f"{item:1}", end=" ")  
        print()


twoDtooneD(a)