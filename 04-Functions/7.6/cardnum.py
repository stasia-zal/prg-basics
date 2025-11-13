def hide(card_number):
    num=1
    cardnew=''
    for i in card_number:
        if num==1 or num==2 or num==13 or num==14 or num==15 or num==16:
            cardnew+=i
        else:
            cardnew+='*'
        num+=1
    return cardnew