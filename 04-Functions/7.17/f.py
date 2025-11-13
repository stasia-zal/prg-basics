def f(pal):
    tr=True
    for i in range((len(pal))//2):
        if pal[i]!=pal[-(i+1)]:
            tr= False
    return tr
