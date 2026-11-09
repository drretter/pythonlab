import csv
import random


books = []

with open('books-en.csv', 'r', encoding='windows-1251') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        books.append(row)

print('Загружено книг:', len(books))

# задание 1
count = 0

for book in books:
    title = book['Book-Title']
    if len(title) > 30:
        count += 1

print('Книг с названием длиннее 30 символов:', count)

# задание 2
print()
author_query = input('Введите имя автора для поиска: ')

found = []

for book in books:
    author = book['Book-Author']
    year = book['Year-Of-Publication']
    year[1] = 'y'
    if author_query.lower() in author.lower():
        if year == '1991' or year == '1996':
            found.append(book)

if len(found) == 0:
    print('Ничего не найдено.')
else:
    print('Найдено книг:', len(found))
    for book in found:
        print(f"{book['Book-Author']} -- {book['Book-Title']} ({book['Year-Of-Publication']})")


# задание 3
print()
sample = random.sample(books, 20)

with open('result.txt', 'w', encoding='utf-8') as out:
    for i in range(len(sample)):
        book = sample[i]
        author = book['Book-Author']
        title = book['Book-Title']
        year = book['Year-Of-Publication']
        out.write(f"{str(i + 1)}. {author}. {title} - {year}\n")


# допзадание
popular_books = sorted(books, key=lambda book: int(book['Downloads']), reverse=True)

top20 = popular_books[:20]

print('Топ 20 самых скачиваемых книг:')
for i, book in enumerate(top20, start=1):
    print(f"{i}. Скачиваний: {book['Downloads']} | {book['Book-Author']}. \
          {book['Book-Title']} ({book['Year-Of-Publication']})")


publishers = set()
for book in books:
    publisher = book['Publisher'].strip()
    if publisher: 
        publishers.add(publisher)

print(f'Найдено уникальных издательств: {len(publishers)}')
print('Первые 10 издательств:')
for pub in sorted(publishers)[:10]:
    print(' ', pub)