def f(sentence):
    vow=['a','e','i','o','u','y']
    sum=0
    for i in sentence:
        for j in vow:
            if i==j:
                sum+=1
    return sum


if __name__=="__main__":
    print(f('book'))
    print(f('water'))
    print(f('hello world'))

