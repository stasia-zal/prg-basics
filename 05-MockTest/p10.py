def f(sentence):
    a=0
    for i in sentence:
        a+=ord(i)
    if a%3==0:
        return True
    else:
        return False
    

if __name__=="__main__":
    print(f('hello world'))
    print(f('university'))
    print(f('student'))


