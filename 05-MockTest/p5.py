def f(binary_number):
    a=True
    for i in str(binary_number):
        if i!='0' and i!='1':
            a=False
    return a

if __name__=="__main__":
    print(f(1101001010))
    print(f(11010586701010))

