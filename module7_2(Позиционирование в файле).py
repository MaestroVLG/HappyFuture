file_name = 'text.txt'

strings = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as fs:
        for el in range(len(strings)):
            pos = fs.tell()
            fs.write(strings[el] + '\n')
            strings_positions[el + 1, pos] = strings[el]

    return strings_positions


res = custom_write(file_name, strings)
for i in res.items():
    print(i)