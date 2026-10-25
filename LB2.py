from csv import reader
import random


def titles(books):     #функция для 1 задания
    k = 0                       #количество строк с длиной названия больше 30
    for row in books:
        if len(row[1]) > 30:    #проверка длины названия
            k += 1
    print(k)


def search(books):                                             #функция для 2 задания
    searchline = input('Введите Фамилию и Имя автора: ')
    k = 0                                                               #количество подходящих строк
    for row in books:
        if (row[4].find(searchline) != -1) and (float(row[7]) > 150):
            k += 1
            print(row)
    if k > 0:
        print(f'Найдено {k} книг')
    if k == 0:                                                          #если подходящих строк не нашлось
        print('Книги не найдены')


def links(books):                                                       #функция для задания 3
    output = open('links.txt', 'w', encoding='utf-8')                   #создание файла для записи
    books_list = list(books)                                            #перевод файла с книгами в формат списка
    random_books = random.sample(books_list, 20)                     #выбор 20 случайных книг
    for num, row in enumerate(random_books, start=1):                   #перебор случайных книг с нумерованием
        output.write(f'{num}. {row[3]}. {row[1]} - {row[6][6:10]}\n')         #запись книги в файл
    output.close()


with open('books.csv', 'r', encoding='cp1251') as csvfile:
    books = reader(csvfile, delimiter=';')
    titles(books)
    csvfile.seek(0)
    search(books)
    csvfile.seek(0)
    links(books)
    csvfile.close()




#4 задание
import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()
dom = minidom.parseString(xml_data)
dom.normalize()

values = dom.getElementsByTagName('Value')               #поиск элементов с тэгом Value

rate = 0                                                 #итоговый средний Value
k = 0

for value in values:                                     #перебор элементов с тэгом Value
    value_str = value.firstChild.data                    #текущее значение Value
    value_float = float(value_str.replace(',', '.'))
    rate += value_float
    k += 1

xml_file.close()
print("Средний показатель Value: ", rate/k)