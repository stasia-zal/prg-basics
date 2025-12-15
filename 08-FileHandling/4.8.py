import re

with open('files.txt','r',encoding='utf-8') as file:
    content=file.read()

four_list=re.findall(r'\w+\.\w{4}',content)
print(len(four_list))