import json

book={'title': 'Hunger Games',
    'author': 'Suzanne Collins',
    'year':2008,
    'movie':True,
    'series':True
    }

with open('favourite.json','w',encoding='utf-8') as file:
    json.dump(book,file)