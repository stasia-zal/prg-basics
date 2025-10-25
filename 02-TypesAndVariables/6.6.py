###
# A program to print numerical representations of characters.
#
x = ["a", "b", "z", "A", "B", "Z", "1", "=", "+", "€"]
c = 0

while c < len(x):
    b = x[c]
    print(f'{b} -> {ord(b)}')
    c = c + 1
