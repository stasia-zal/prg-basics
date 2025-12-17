
translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}
word=input('Enter a word in english: ').lower()

if word in translations:
    print('The polish word for it is:', translations[word])
else:
    print("Sorry this word isn't in our translator")
