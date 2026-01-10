def f(word):
    res=''
    letter=0
    for i in word:
        for a in word:
            if a==word[letter]:
                res+=a.upper()
            else:
                res+=a.lower()
        letter+=1
        if letter<len(word):
            res+='-'
    return res


if __name__=='__main__':
    print(f('water'))
    print(f('a'))