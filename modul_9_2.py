first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) > 5]
print(first_result)

second_result = [f"('{x}','{y}')" for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)

a = first_strings + second_strings
third_result = {x: len(x) for x in a if len(x) % 2 == 0}
print(third_result)
