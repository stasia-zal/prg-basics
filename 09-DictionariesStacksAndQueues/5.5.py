paragraph = "cat dog mouse cat rat cat mouse"

dic={}
words=paragraph.split()
for word in words:
    if word in dic:
        dic[word]+=1
    else:
        dic[word]=1
for words, count in dic.items():
    print(f"The count of {words} is {count}")