name=input('Enter First Name: ')
secn=input('Enter Second Name: ')
initials= lambda name,secn: name[0]+secn[0]
print(initials(name,secn))