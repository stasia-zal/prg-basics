def f(amount_to_pay):
    coins=[5,2,1]
    a=0
    for coin in coins:
        a+=amount_to_pay//coin
        amount_to_pay%=coin
    return a