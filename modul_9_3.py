
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x)-len(y)) for x,y in zip(first, second) if len(x) != len(y))
second_result = ((abs(len(first[x]))==len(second[x])) for x in range(max(len(first), len(second))))


print(list(first_result))
print(list(second_result))