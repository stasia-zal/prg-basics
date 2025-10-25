###
# A program to print numerical representations of characters.
#
x = input("Your name:")
c = 0
while c < len(x):
    b = x[c]
    print(f'{b} -> {ord(b)}')
    c = c + 1
