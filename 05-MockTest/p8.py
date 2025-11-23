def f(palindrome):
    a=True
    for i in range(len(palindrome)//2):
        if palindrome[i]!=palindrome[-i-1]:
            a=False
    return a

if __name__=="__main__":
    print(f('radar'))
    print(f('12-11-21'))
    print(f('book'))
