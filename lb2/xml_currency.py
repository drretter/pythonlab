import xml.dom.minidom as minidom

with open('currency.xml', 'rb') as f:
    raw_data = f.read()

dom = minidom.parseString(raw_data)
dom.normalize()

valutes = dom.getElementsByTagName('Valute')

names = []
values = []

for valute in valutes:
    name_tag = valute.getElementsByTagName('Name')[0]
    name = name_tag.firstChild.data
    names.append(name)

    value_tag = valute.getElementsByTagName('Value')[0]
    value_raw = value_tag.firstChild.data
    value = float(value_raw.replace(',', '.'))
    values.append(value)

print('Всего валют:', len(names))
print()

print('Список названий (Name):')
for name in names:
    print(' ', name)

print()

print('Список курсов (Value):')
for value in values:
    print(' ', value)

# допзадание
all_elements = dom.getElementsByTagName('*')
unique_tags = set()

for elem in all_elements:
    unique_tags.add(elem.tagName)

print('Все уникальные теги в XML:')
for tag in sorted(unique_tags):
    print(' ', tag)