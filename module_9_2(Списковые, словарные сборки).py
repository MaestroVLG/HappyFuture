from typing import List, Dict, Tuple

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


first_result = [x for x in first_strings if len(x) >= 5]

first_lengths = [len(x) for x in first_result]
print(first_lengths)


second_result = [(first, second) for first in first_result for second in second_strings if len(first) == len(second)]
print(second_result)


combined_strings = first_strings + second_strings
length_dict = {string: len(string) for string in combined_strings}
print(length_dict)
