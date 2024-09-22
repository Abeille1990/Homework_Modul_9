class StepValueError(ValueError):
    pass

class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start # можно приравнять pointer к зачению start сразу в init, а можно позже в iter
        if step == 0:
            raise StepValueError

    def __iter__(self):
        # self.pointer = self.start  # можно приравнять pointer к зачению start сразу в init, а можно позже в iter
        return self

    def __next__(self):
        current = self.pointer  #создаем переменную current чтобы иницировать вызов pointer вначале цикла
        # - чтобы захватить стратовую точку
        if current > self.stop and self.step > 0 or current < self.stop and self.step <0:
            raise StopIteration()
        else:
            self.pointer += self.step
        return current  # возвращаем начальное значение pointer равное старту, после чего проходит итерация цикла,
        # которая увеличивает pointer на шаг и в начале следующего цикла pointer уже новый и выводится из переменной
        # current. то есть не как привычно , что return возвращает, как правило, результат последнего в цикле
        # ,как бы, завершающего выражения, а наоброт берет еще необработанную переменную.

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
        print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

