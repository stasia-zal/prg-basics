def counter(text,letter):
    num=0
    for i in text:
        if i==letter:
            num+=1
    return num