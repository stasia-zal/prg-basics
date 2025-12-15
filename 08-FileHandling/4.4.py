file_name='it_company.csv'

with open(file_name,'r') as file:
    content=file.read().splitlines()
i=0
while i<len(content):
    for line in content[i:i+5]:
        print(line)
    i+=5
    input('Press Enter key...')