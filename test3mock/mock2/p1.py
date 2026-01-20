def f(n):
    st=str(n)
    collection=set()
    for dig in st:
        if int(dig)%2!=0:
            collection.add(int(dig))
    if not collection: return -1
    res=int(max(collection))-int(min(collection))
    if res!=0:
        return res
    else: return -1

print(f(10852))
print(f(723597))
print(f(4388))
print(f(846206))