class Book:

    material_pages = 'paper'
    presence_of_text = True


    def __init__(self,book_title, author, count_of_pages, isbn, reserved):
        self.book_title = book_title
        self.author = author
        self.count_of_pages = count_of_pages
        self.isbn = isbn
        self.reserved = reserved


class School(Book):


    def __init__(self, book_title, author, count_of_pages, isbn, reserved, course, clas, tasks):
        super().__init__(book_title, author, count_of_pages, isbn, reserved)
        self.course = course
        self.clas = clas
        self.tasks = tasks


harry_potter = Book('Harry Potter', 'J. Roulin',
                    435, '743-123-112', False)
animal_farm = Book('Animal Farm', 'J. Oruel',
                   356 , '771-413-312', False)
a_n_w = Book('Amaizing new world', 'O. Haksli',
             402 , '664-451-222', False)
prince = Book('Prince', 'N. Machiavelli',
              213, '888-124-722', True)
the_green_mill = Book('The Green mill','S. King',
                      '315', '415-980-325', False)

history = School('History', 'E. Panosenkop',250, '909-202-400',  False,
              'History of World', '5-7', 'на дом')
algebra = School('Algebra', 'R. Zaitsman', 231, '221-413-304', False,
                 'Algebra', '7', 'на дом')
geografy = School('Geografy', 'F. Konuhov', 180,'180-800-365', True,
                  'Geografy', '5-7', 'на дом')
music = School('Music', 'A.vanBuren', '104' ,'104_015-202' ,False,
               'music_theory', '5-9', 'нет заданий')


books = [harry_potter, animal_farm, a_n_w, prince, the_green_mill, history, algebra, geografy, music]
for x in books:
    if isinstance(x, School):
        if x.reserved == True:
            print(f'Название: {x.book_title}, Автор: {x.author}, Кол.стр: {x.count_of_pages},'
                  f'Материал страниц: {x.material_pages}, is reserved, Предмет: {x.course},'
                  f' Класс: {x.clas}, Задания: {x.tasks}')
        else:
            print(f'Название: {x.book_title}, Автор: {x.author}, Кол.стр: {x.count_of_pages},'
                  f'Материал страниц: {x.material_pages}, Предмет: {x.course},'
                  f' Класс: {x.clas}, Задания: {x.tasks}')
    else:
        if x.reserved == True:
            print(f'Название: {x.book_title}, Автор: {x.author}, Кол.стр: {x.count_of_pages},'
                  f'Материал страниц: {x.material_pages}, is reserved')
        else:
            print(f'Название: {x.book_title}, Автор: {x.author}, Кол.стр: {x.count_of_pages},'
                  f'Материал страниц: {x.material_pages}')
