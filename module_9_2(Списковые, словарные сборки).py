from typing import Set, Dict, Any

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [x for x in first_strings if len(x) >= 5]
print(first_result)
second_result = [(first_strings, second_strings) for first in first_result for second in second_strings if len(first) == len(second)]
print(second_result)
third_result = [(string, len(string)) for string in first_strings + second_strings if len(string) % 2 == 0]
print(third_result)