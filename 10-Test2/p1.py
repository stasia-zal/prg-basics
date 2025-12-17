# 23:17

def f(player1,player2):
    cards=['T','J','Q','K','A']
    pl1=0
    pl2=0
    for card in player1:
        if card.isdigit():
            pl1+=int(card)
        elif card in cards:
            pl1+=10
    for card in player2:
        if card.isdigit():
            pl2+=int(card)
        elif card in cards:
            pl2+=10
    if pl1>=pl2:
        return True
    else: return False




if __name__ == '__main__':
    print( f('AJ972',"AQT72") ) 
    print( f("9532","K8") ) 