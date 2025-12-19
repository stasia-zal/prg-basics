
def f(c):
    game='AKQJT98765432'
    a=[]
    for carr in game:
        a.append(carr)
    for card in c:
        if card in a:
            a.remove(card)
        else:
            return card
    for res in a:
        return res



if __name__=='__main__':
    print(f("AKQJT8765432"))
    print(f('4765329AKQJT'))