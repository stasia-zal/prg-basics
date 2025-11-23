def f(card_number):
    res=''
    a=0
    for i in card_number:
        if a<2  or a>11:
            res+=card_number[a]
        else:
            res+='*'
        a+=1
    return res


if __name__=="__main__":
    print(f('1234123412341234'))
