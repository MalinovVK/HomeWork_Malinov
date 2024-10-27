first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


first_result = [len(first_strings[x]) for x in range(len(first_strings)) if len(first_strings[x]) >= 5]
print(first_result)

second_result = [(first_strings[i], second_strings[j]) for i in range(len(first_strings)) for j in range(len(second_strings)) if len(first_strings[i]) == len(second_strings[j])]
print(second_result)

third_result = {x or y: len(x) or len(y) for x in first_strings for y in second_strings if len(x) % 2 or len(y) % 2}
print(third_result)