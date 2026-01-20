def f(word):
    word=word.lower()
    res=''
    for i in range(len(word)):
        res+=word[:i]+word[i].upper()+word[i+1:]+'-'
    return res[:-1]
print(f('book'))
print(f('water'))
print(f('Ok'))
print(f('A'))
print(f(""))