import re

def f(addr):
    key=r'[A-Za-z]{1,2}[\d]{1,4}'
    a=re.fullmatch(key,addr)
    if a==None:
        return False
    else:
        return True


if __name__=='__main__':
    print(f('A4'))
    print(f('a4'))
    print(f('4a'))
    print(f('bC123'))
    print(f('bcd555'))
    print(f('g80915'))
    