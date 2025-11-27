# To task 3.23


def words(t):
    text=t.split()
    count=1
    for i in text:
        if i==' ':
            count+=1
    return count

def longword(t):
    text=t.split()
    return sorted(text,key=len,reverse=True)

def alpha(t):
    text=t.split()
    return sorted(text, reverse=False)