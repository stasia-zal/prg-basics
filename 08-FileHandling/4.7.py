import re

text=input('Enter text: \n')

def vowels():
    vow_list=re.findall(r'[aeiouAEIOU]' ,text)
    return len(vow_list)

print('Number of vowels: ',vowels())