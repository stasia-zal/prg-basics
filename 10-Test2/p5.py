def f(first,last):
    count=0
    with open('data.txt','r',encoding='utf-8') as file:
        content=file.read()
    content=content.split()
    for word in content:
        if word[0].lower()==first.lower() and word[-1].lower()==last.lower():
            count+=1
    return count

print(f("w","d"))