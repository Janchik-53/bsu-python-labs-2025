class Library :
    librarycount = 0
    def libraries_quantity(cls) :
        print("Количество созданных библиотек : ",cls.librarycount)


    def __init__(self) :
        self.books = {}
        Library.librarycount += 1


    def add_book(self,title) :
        self.books[title] = 1

    def bring_book(self,title) :
        self.books[title] = 0

    def remove_book(self,title) :
        if title in self.books :
            del self.books[title]

    def find_book(self,title) :
        if title in self.books :
          if self.books[title] == 1 :
            print(f" книга {title} доступна")
          else :
            print("Эта книга недоступна")
        else :
            print("Эта книга не найдена в билиотеке")

    
    def show_all_available_books(self): 
        print("Доступные книги : ")
        for book,status in self.books.items() :
            if status == 1 :
                print(f"-{book}")


def main() :
    library = Library()
    library.libraries_quantity()
    library.add_book("1984")
    library.add_book("Цветы для Элджернона")
    library.find_book("1984")
    library.show_all_available_books()
    library.bring_book("1984")
    library.show_all_available_books()
    library1 = Library()
    library.libraries_quantity()


main()

        
    