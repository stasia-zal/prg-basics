class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
        self.cur_page=0
        self.isopen=False
    def open(self):
        self.isopen=True
    def close(self):
        self.isopen=False
    def status(self):
        print()
        print('Title: ',self.title)
        print('Author: ',self.author)
        print('Ammount of pages: ',self.pages)
        print('Current page: ', self.cur_page)
    def read(self,pages):
        if self.isopen:
            if pages>0 and (self.cur_page+pages)<self.pages:
                self.cur_page+=pages
        else:
            print('ERROR: BOOK IS CLOSED')
