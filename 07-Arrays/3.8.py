arr=[2, 6, 4, 9, 7]
def star(n):
    a=str(n)+': '+'*'*n
    return a
for i in arr:
    print(star(i))