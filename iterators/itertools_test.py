# Функция tabulate()
"""
from itertools import count

def tabulate(func):
    return map(func, count(1,1))

func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))    
"""

# Функция factorials()
"""
from itertools import accumulate
import operator

def factorials(n):
    return accumulate((el for el in range(1,n+1)), operator.mul)

numbers = factorials(6)
print(*numbers)    
"""

# Функция alnum_sequence()
"""
from itertools import cycle, starmap
import string

# красивое попарное представление (цифра+буква...)
def alnum_sequence():
    alphabet = string.ascii_uppercase
    iterable = starmap(lambda x, y: f'{x} {y}', enumerate(alphabet, 1))
    return cycle(iterable)

# поэлементное представление (цифра, буква, цифра, буква ...)
def alnum_sequence():
    alphabet = string.ascii_uppercase
    for i in cycle(enumerate(alphabet, 1)):
        yield from i

alnum = alnum_sequence()
print(*(next(alnum) for _ in range(55)))
"""

# Функция roundrobin (задача решена очень спорным НЕ оптимальным методом!)
"""
from itertools import cycle

def roundrobin(*args):
    iter_list = []
    for el in args:
        iter_list.append(iter(el))
    final_round = len(iter_list)*5
    res_iter = cycle(iter_list)

    for res in res_iter:
        try:
            temp_res = next(res)
            yield temp_res
        except StopIteration:
            final_round -= 1
            if final_round == 0:
                break

#roundrobin('abc', 'd', 'ef')
#print(*roundrobin('abc', 'd', 'ef'))

numbers = [1, 2, 3]
letters = iter('betgrsk')

print(*roundrobin(numbers, letters))
"""

# Функция drop_while_negative()
"""
from itertools import dropwhile, filterfalse

def drop_while_negative(iterable):
    #return dropwhile(lambda x: x < 0, iterable)
    return filterfalse(lambda x: x<=0, iterable)

numbers = [-3, -2, -1, 0, 1, 2, 3]
print(*drop_while_negative(numbers))    
"""

# Функция first_largest()
# через распаковку в списки и dropwhile
"""
from itertools import dropwhile

def first_largest(iterable, n):
    start_count = 0
    final_count = 0
    temp = list(iter(iterable))
    if not list(filter(lambda x: x > n, temp)):
        return -1
    temp_iter = iter(temp)
    while True:
        try:
            next(temp_iter)
            start_count +=1
        except StopIteration:
            break  
    res = dropwhile(lambda x: x < n, iter(temp))
    while True:
        try:
            next(res)
            final_count +=1
        except StopIteration:
            break         
    return start_count - final_count
"""
# через итератор
"""
def first_largest(iterable, n):
    res_index = -1
    temp_index = 0
    data = iter(iterable)
    while True:
        try:
            res = next(data)
            if res > n:
                 res_index = temp_index
                 break
            temp_index +=1
        except StopIteration:
            break
    return res_index        

iterator = iter([9, 8, 18, 21, 14, 72, 73, 18, 20])
print(first_largest(iterator, 10))

numbers = [10, 2, 14, 7, 7, 18, 20]
print(first_largest(numbers, 11))

iterator = iter([-1, -2, -3, -4, -5])
print(first_largest(iterator, 10))

iterator = iter([18, 21, 14, 72, 73, 18, 20])
print(first_largest(iterator, 10))

iterator = iter([4, 100, 102, 334, 5])
print(first_largest(iterator, 101))
"""

# Функция sum_of_digits()
"""
from itertools import chain
from functools import reduce

def sum_of_digits(data):
    data = list(map(str, data))
    res = reduce(lambda x,y: int(x)+int(y), chain.from_iterable(data))
    return res

print(sum_of_digits([13, 20, 41, 2, 2, 5]))
"""

# Функция is_rising()
"""
from itertools import pairwise

def is_rising(data: iter) -> bool:
    return all(map(lambda x: x[0] < x[1], pairwise(data)))

print(is_rising([1, 2, 3, 4, 5]))    
"""

# Функция max_pair()
"""
from itertools import pairwise

def max_pair(data: iter) -> int:
    return max(map(lambda x: sum(x), pairwise(data)))

print(max_pair([1, 8, 2, 4, 3]))
"""

# Функция ncycles()
"""
from itertools import tee, chain

def ncycles(data: iter, times: int) -> iter:
    return chain.from_iterable(tee(data, times))
        
print(*ncycles([1, 2, 3, 4], 3))
"""

# Функция grouper()
"""
from itertools import islice, zip_longest, tee
from math import ceil

def grouper(data: any, times: int) -> iter:
    data1, data2 = tee(data, 2)
    len_data = len(list(data1))
    data = iter(data2)
    temp_list = (islice(data,0,ceil(len_data / times)) for _ in range(times))
    return zip_longest(*temp_list)

#numbers = [1, 2, 3, 4, 5, 6, 7]
#print(*grouper(numbers, 3))
"""

#
"""
from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

sort_per = sorted(persons, key = lambda x: x.height)
res = groupby(sort_per, key = lambda x: x.height)

for key, per in res:
    print(f'{key}: {", ".join([el.name for el in sorted(per, key = lambda x: x.name)])}')
"""

#
"""
from collections import namedtuple
from itertools import groupby

Student = namedtuple('Student', ['surname', 'name', 'grade'])

students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
            Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
            Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
            Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
            Student('Елькина', 'Мария', 11),Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
            Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
            Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
            Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
            Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]

students = sorted(students, key = lambda x: x.name)
res = groupby(students, key = lambda x: x.name)
res_list = max(sorted([(key, len(list(name))) for key, name in res]), key = lambda x: x[1])
print(res_list[0])
"""

# Группы слов
"""
from itertools import groupby

def group(text):
    text = sorted(text.split(), key = lambda x: len(x))
    res_text = groupby(text, key = lambda x: len(x))
    return res_text

res = group(input())

for key, value in res:
    print(f'{key} -> {", ".join(sorted(value))}') 

# hi never here my blueS
"""

# Нет дел
"""
from itertools import groupby

tasks = [('Отдых', 'поспать днем', 3),
        ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
        ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
        ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
        ('Отдых', 'погулять вечером', 4),
        ('Курс по ооп', 'обсудить темы', 1),
        ('Урок по groupby', 'добавить задачи на программирование', 3),
        ('Урок по groupby', 'написать конспект', 1),
        ('Отдых', 'погулять днем', 2),
        ('Урок по groupby', 'добавить тестовые задачи', 2),
        ('Уборка', 'убраться в ванной', 2),
        ('Уборка', 'убраться в комнате', 1),
        ('Уборка', 'убраться на кухне', 3),
        ('Отдых', 'погулять утром', 1),
        ('Курс по ооп', 'обсудить задачи', 2)]

tasks = sorted(tasks, key = lambda x: x[0])
res_tasks = groupby(tasks, key = lambda x: x[0])

for key, value in res_tasks:
    print(key, end=':\n')
    for el in list(sorted(value, key = lambda x: x[2])):
        print(f'    {el[2]}. {el[1]}')
    print()
"""

# Функция group_anagrams()
"""
from itertools import groupby

def group_anagrams(words: list) -> list[tuple]:
    words = sorted(words, key = lambda x: sorted(x))
    res = groupby(words, key = lambda x: sorted(x))
    res_list = [tuple(value) for key, value in res]
    return res_list

groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
print(*groups)

#groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])
#print(*groups)
"""

# Функция ranges()
"""
def ranges(numbers: list) -> list[tuple]:
    temp_list = []
    res_list = []
    for el in numbers:
        if len(temp_list) == 0:
            temp_list.append(el)    
        elif el - temp_list[-1] == 1:
            temp_list.append(el)
        else:
            res_list.append((temp_list[0], temp_list[-1]))
            temp_list = []  
            temp_list.append(el)  
    if len(temp_list) == 1:
        res_list.append((temp_list[0], temp_list[0]))
    else:    
        res_list.append((temp_list[0], temp_list[-1]))        
    return res_list

numbers = [1, 3, 5, 7]
print(ranges(numbers))
"""
 
######################################### комбинаторика #######################################
# поиск возможных сочетаний из четырех
"""
from itertools import permutations

number = [1,2,3,4]
print(len(list(permutations(number))))
"""
# поиск возможных сочетаний двух объектов из 26
"""
from itertools import combinations

number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
print(len(list(combinations(number, r=2))))
"""

# Перестановки
"""
from itertools import permutations

res = sorted(set(''.join(el) for el in permutations([el for el in input()])))
print(*res, sep = '\n')
"""

# книжный магазин
"""
from itertools import combinations

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
res_list = []
for r in range(1, len(wallet)):
    res = set(filter(lambda x: sum(x) == 100, combinations(wallet, r = r)))
    if len(res) != 0:
        res_list.append(len(res))
print(sum(res_list))
"""

# книжный магазин 2
"""
from itertools import combinations_with_replacement

count = 0
wallet = [100, 50, 20, 10, 5]
for r in range(1, 21):
    res = list(filter(lambda x: sum(x) == 100, set((combinations_with_replacement(wallet, r = r)))))
    if len(res) != 0:
        count += len(res)
print(count)        
"""

# Задача о рюкзаке
"""
from collections import namedtuple
import itertools

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

total_mass = int(input())

def bag(total_mass, items):
    optim_mass = []
    temp_list = []
    res_list = []
    total_res_list = []    
    pre_dict = {}  
    pre_string = []

    total_price = 0

    mass_list = [el.mass for el in items]
    for r in range(1, 11):
        optim_mass.extend(
                          list(map(lambda x: list(x), filter(lambda x: sum(x) <= total_mass, itertools.combinations(mass_list, r = r))))
                          )
    if len(optim_mass) == 0:
        print ('Рюкзак собрать не удастся')
        return
        
    for el in optim_mass: 
        for el in map(lambda x: list(filter(lambda y: y['mass'] == x, [el._asdict() for el in items])), el):
            temp_list.append((el[0]['name'], el[0]['price']))
        res_list.append(temp_list)
        temp_list = []
      
    for res in res_list:
        for el in res:
            pre_string.append(el[0])
            total_price += el[1]
        pre_dict.setdefault(', '.join(pre_string), total_price)  
        total_res_list.append(pre_dict)
        total_price = 0
        pre_string = []
        pre_dict = dict()
    for key, value in sorted(total_res_list, key = lambda x: int(*map(int, x.values())), reverse=True)[0].items():
        print(*sorted(key.split(', ')), sep = '\n')

bag(total_mass, items)       
"""
# комбинатор различных систем счисления
"""
from itertools import product

symbol_list = [el for el in range(10)] + [el for el in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
n = int(input())
m = int(input())

for el in product(symbol_list[:n], repeat = m):
    print(*el, sep = '', end = ' ') 
"""    