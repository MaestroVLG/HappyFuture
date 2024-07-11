import io
from pprint import pprint

file = open('byron.txt', 'r')
with open('byron.txt') as file:
    text = file.read()
    print(text)


