import math
def triangle_area(a,b,c):
    s=(a+b+c)/2
    u=s*(s-a)*(s-b)*(s-c)
    if a + b <= c or a + c <= b or b + c <= a:
        return "Triangle not possible"
    area=math.sqrt(u)
    return area
print(triangle_area(3,4,5))
print(triangle_area(5,12,30))
print(triangle_area(7,24,25))