f=open('abc.txt')
file_content=f.read()
print(file_content)
f.close()


'''

with open('abc.txt','r') as f:
    file_content=f.read()
    print(file_content)
'''