###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
a=int(a)
b = input('b=')
b=int(b)
c = input('c=')
c=int(c)
volume=a*b*c
surface_area=2*(a*b+b*c+c*a)
print(f"Volume of a cuboid with sides {a}; {b}; {c} is {volume}. ")
print(f"Surface area of a cuboid with sides {a}; {b}; {c} is {surface_area}. ")
