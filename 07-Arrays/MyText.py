# To task 3.23


def words(text):
    count=1
    for i in text:
        if i==' ':
            count+=1
    return count

def longword(text):
    return sorted(text,ley=len,reverse=True)

def alpha()