
def f(arr):
    if arr[0]==arr[1]:
        all=arr[0]
    else:
        all=arr[2]
    for num in arr:
        if num!= all:
            return num
        
if __name__=='__main__':
    print(f([25,25,23]))
    print(f([7,7,7,7,7,5,7,7,7]))