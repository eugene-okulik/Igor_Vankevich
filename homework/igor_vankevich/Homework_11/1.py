class Book:
    material = 'бумага'
    text = True

    def __init__(self, book_name, autor, page, isbn, reserved):
        self.book_name = book_name
        self.autor = autor
        self.page = page
        self.isbn = isbn
        self.reserved = reserved
        if reserved:
            self.reserved = ', зарезервированна'
        else:
            self.reserved = ''


class SchoolBook(Book):

    def __init__(self, book_name, autor, page, isbn, reserved, subject, class_num, task):
        super().__init__(book_name, autor, page, isbn, reserved)
        self.subject = subject
        self.class_num = class_num
        self.task = task


book1 = Book('Идиот', 'Достоевский', 312, 4321, True)
book2 = Book('Граф Монте-Кристо', 'Дюма', 213, 1111, False)
book3 = Book('Записки юного врача', 'Булгаков', 111, 4353, False)
book4 = Book('Американская трагедия', 'Драйзер', 3234, 6453, False)
book5 = Book('Отцы и дети', 'Тургенев', 676, 565323, False)
book6 = SchoolBook('Алгебра', 'Иванов', 532, 9393253, True, 'Математика',
                   5, True)
book7 = SchoolBook('Анатомия', 'Васиков', 546, 994332, True, 'Биология',
                   3, False)
book8 = SchoolBook('Я и общество', 'Рюпиков', 332, 23252339, False,
                   'Обществовединие', 11, False)
book9 = SchoolBook('Созвездия', 'Звездочкин', 632, 5765469, False,
                   'Астрономия', 7, True)

print(f'Название: {book1.book_name}, автор: {book1.autor}, страниц: {book1.page}, '
      f'материал: {book1.material}{book1.reserved}')
print(f'Название: {book2.book_name}, автор: {book2.autor}, страниц: {book2.page}, '
      f'материал: {book2.material}{book2.reserved}')
print(f'Название: {book3.book_name}, автор: {book3.autor}, страниц: {book3.page}, '
      f'материал: {book3.material}{book3.reserved}')
print(f'Название: {book4.book_name}, автор: {book4.autor}, страниц: {book4.page}, '
      f'материал: {book5.material}{book5.reserved}')
print(f'Название: {book6.book_name}, автор: {book6.autor}, страниц: {book6.page}, предмет: {book6.subject},'
      f' класс: {book6.class_num}{book6.reserved}')
print(f'Название: {book7.book_name}, автор: {book7.autor}, страниц: {book7.page}, предмет: {book7.subject},'
      f' класс: {book7.class_num}{book7.reserved}')
print(f'Название: {book8.book_name}, автор: {book8.autor}, страниц: {book8.page}, предмет: {book8.subject},'
      f' класс: {book8.class_num}{book8.reserved}')
print(f'Название: {book9.book_name}, автор: {book9.autor}, страниц: {book9.page}, предмет: {book9.subject},'
      f' класс: {book9.class_num}{book9.reserved}')
