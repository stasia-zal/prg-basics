from e_book import Book 


def main():
    book=Book('Hunger Games','Suzanne Collins',374)
    book.open()
    book.status()
    book.read(15)
    book.status()
    book.close()
    book.read(45)
    book.status()

if __name__=='__main__':
    main()
