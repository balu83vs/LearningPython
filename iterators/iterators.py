################################ ИТЕРАТОРЫ и ГЕНЕРАТОРЫ ##########################

# обратный Filter
"""
def filterfalse(predicate, iterable):
    return list(filter(lambda x: not predicate(x), iterable))

numbers = [1, 2, 3, 4, 5]

print(*filterfalse(lambda x: x >= 3, numbers))
"""

# Функция transpose()
"""
def transpose(matrix):
    return list(map(list, zip(*matrix)))

matrix = [['1', '2'],
          ['4', '5'],
          ['7', '8'],
          ['3', 4],
          [True, None],
          [9, 80],
          [1, -1]]

print(transpose(matrix))
"""

# Функция get_min_max()
"""
def get_min_max(data):
    if len(data) == 0:
        return None
    else:
        min_index = list(filter(lambda x: x if x[1] == min(data) else None, enumerate(data)))[0]
        max_index = list(filter(lambda x: x if x[1] == max(data) else None, enumerate(data)))[0]
        return (min_index[0], max_index[0])

data = [1, 1, 2, 3, 8, 8]

print(get_min_max(data))
"""

# Функция get_min_max()
"""
import copy

def get_min_max(iterable):
    if str(type(iterable)) == "<class 'range_iterator'>":
            iterable = iter(iterable)
            iterable2 = copy.deepcopy(iterable)
            return (min(iterable), max(iterable2))
    min_max = {}
    iterable = iter(iterable)
    try:
        el = next(iterable)
    except StopIteration:
        return None
    else:
        min_max['min'] = el
        min_max['max'] = el
        while True:
            try:
                el = next(iterable)
                if el < min_max.get('min'):
                    min_max['min'] = el
                if el > min_max.get('max'):
                    min_max['max'] = el
            except StopIteration:
                return (min_max.get('min'), min_max.get('max'))            
            
data = iter(range(100_000_000))
print(get_min_max(data))
"""

# Функция starmap()
"""
def starmap(func, iterable):
    return [func(*el) for el in iterable]

pairs = [(1, 3), (2, 5), (6, 4)]
print(*starmap(lambda a, b: a + b, pairs))    
"""

####################### Создание собственных итераторов ###########################
##
"""
from random import choice

class random_numbers:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def __iter__(self):
        return self
                          
    def __next__(self):
        if self.left == self.right:
            return self.left
        else:
            self.res = choice(list(range(self.left, self.right)))
            return self.res
        
iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))        
"""

# Итератор Fibonacci
"""
class Fibonacci:
    def __init__(self) -> None:
        self.start = 0
        self.index_1 = 0
        self.index_2 = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start == 0:
            self.start += 1
            return 1
        else:
            res = self.index_1 + self.index_2
            self.index_1 = self.index_2
            self.index_2 = res
            return res
        
fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))        
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci)) 
print(next(fibonacci))
"""

# Итератор PowerOf

"""
class PowerOf:
    def __init__(self, number):
        self.number = number
        self.pow = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = self.number ** self.pow
        self.pow += 1
        return res
    
power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))    
"""

# Итератор DictItemsIterator
"""
class DictItemsIterator:
    def __init__(self, data) -> None:
        self.data = data
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        dict_len = len(self.data)
        if self.index < dict_len:
            self.index +=1
            key_list = list(self.data)
            return (key_list[self.index-1], self.data.get(key_list[self.index-1]))
        else:
            raise StopIteration
    
pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
print(*pairs)    
"""

# Итератор CardDeck
"""
class CardDeck:
    def __init__(self) -> None:
        self.mast = ['пик', 'треф', 'бубен', 'червей']
        self.nom = ['2','3','4','5','6','7','8','9','10','валет','дама','король','туз']
        self.deck = [f'{n} {m}' for m in self.mast for n in self.nom]
        self.len_deck = len(self.deck)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.index < self.len_deck
            return self.deck[self.index]
        except:
            raise StopIteration
        finally:
            self.index += 1

#cards = list(CardDeck())

#print(cards[9])
#print(cards[23])
#print(cards[37])
#print(cards[51])        
"""

# Итератор Cycle
"""
class Cycle:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.data_iter = iter(self.iterable)

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            res = next(self.data_iter)
            return res
        except StopIteration:
            self.data_iter = iter(self.iterable)
            res = next(self.data_iter)
            return res
  
cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
"""

# Итератор RandomNumbers
"""
from random import choices

class RandomNumbers:
    def __init__(self, left, right, number) -> None:
        self.left = left
        self.right = right + 1
        self.number = number
        self.res = iter(choices(range(self.left, self.right), k=self.number))

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.res)    
    
#iterator = RandomNumbers(1, 1, 3)

#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
"""

# Итератор Alphabet
"""
class  Alphabet:
    def __init__(self, language):
        self.language = language
        self.lang_dict = {'ru_start': ord('а'), 'ru_end': ord('я'), 'en_start': ord('a'), 'en_end': ord('z')}
        self.index = self.lang_dict.get(f'{self.language}_start')

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            if self.index <= self.lang_dict.get(f'{self.language}_end'):
                return chr(self.index)
            else:
                raise StopIteration
        except StopIteration:
            self.index = self.lang_dict.get(f'{self.language}_start')            
            return chr(self.index)
        finally:
            self.index +=1
    
ru_alpha = Alphabet('en')

for _ in range(40):
    print(next(ru_alpha))
#print(next(ru_alpha))
#print(next(ru_alpha))
"""

# Итератор Xrange
"""
class Xrange:
    def __init__(self, start, end, step = 1):
        self.start = start
        self.base_start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        try: 
            if self.base_start < self.end:
                if self.start < self.end:
                    return self.start
                else: 
                    raise StopIteration
            else:
                if self.start > self.end:
                    return self.start
                else: 
                    raise StopIteration         
        finally:
            self.start += self.step

#xrange = Xrange(-20, 13, 4)
#print(*xrange)

#xrange = Xrange(10, -21, -6)
#print(list(xrange))


#xrange = Xrange(0, 3, 0.5)
#print(*xrange, sep='; ')    
"""

########################## Генераторы ##############################

# Функция alternating_sequence()
"""
def alternating_sequence(count = None):
    i = 0
    while abs(i) != count:   
        i += 1
        if i%2 != 0:
            yield i
        else:
            yield i * -1
    return StopIteration

generator = alternating_sequence()

for _ in range(10_124_421):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
"""

# Функция primes()
"""
def primes(left, right):
    for i in range(left, right + 1):
        if i != 1 and all([1 if i%j != 0 or j == i or j == 1 else 0 for j in range(1, i+1)]):
                yield i

generator = primes(1, 15)
print(*generator)            
"""

# Функция reverse()
"""
def reverse(sequence):
    for el in sequence[::-1]:
        yield el

generator = reverse('beegeek')

print(type(generator))
print(*generator)       
"""

# Функция dates()
"""
from datetime import date, timedelta

def dates(start, count = None):
    delta = timedelta(days=1)
    try:
        if not count: 
            while True:
                yield start
                start += delta
        else:
            for _ in range(count):
                yield start
                start += delta  
    except Exception as err:
        return err

generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print('Error')
"""

# Функция card_deck()
"""
def card_deck(suit):
    masty = ('пик', 'треф', 'бубен', 'червей')
    numbers = ('2','3','4','5','6','7','8','9','10','валет','дама','король','туз')
    new_masty = tuple(filter(lambda x: x!= suit, masty))
    while True:
        for mast in new_masty:
            for num in numbers:
                yield f'{num} {mast}'            

    
generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)
"""


# Функция matrix_by_elem()
"""
def matrix_by_elem(matrix):
    print(sum(matrix, []))
    yield from sum(matrix, [])

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(*matrix_by_elem(matrix))  
"""

# Функция palindromes()
"""
def test():
    i = 1
    while True:
        if str(i) == str(i)[::-1]:
            yield i
        i+=1    

def palindromes():
    yield from test() 


generator = palindromes()
numbers = [next(generator) for _ in range(30)]
print(*numbers)
"""

# Функция flatten()
"""
def flatten(nested_list):
    for el in nested_list:
        if isinstance(el, (int, float)):
            yield el          
        else:
            yield from flatten(el)

generator = flatten([[1, 2], [[3]], [[4], 5]])
print(*generator)
"""

###################### Генераторные выражения #####################

# Функция cubes_of_odds()
"""
def cubes_of_odds(iterable):
    return (number ** 3 for number in iterable if number% 2 != 0) 

print(*cubes_of_odds([1, 2, 3, 4, 5]))
"""

# Функция is_prime()
"""
def is_prime(number):
     if number != 1:
        return all(number%i for i in range(2, number))
     else: 
        return False

print(is_prime(1))
"""

# Функция interleave()
"""
def interleave(*args):
    return (i[j] for j in range(len(args[0])) for i in args) 
   
numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]

print(*interleave(numbers, squares, qubes))
"""

########################## Конвейеры генераторов ########################

# 
from collections import namedtuple

Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
           Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
           Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
           Person('Genevieve Asse', 'French', 'female', 1949, 0),
           Person('Irene Adler', 'Swedish', 'female', 2005, 0),
           Person('Sergio Asti', 'Italian', 'male', 1926, 0),
           Person('Olof Backman', 'Swedish', 'male', 1994, 0),
           Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
           Person('Dana Atchley', 'American', 'female', 1941, 2000),
           Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
           Person('Shura_Stone', 'Russian', 'male', 2000, 0),
           Person('Jon Bale', 'Swedish', 'male', 2000, 0)]

# через генераторные функции
"""
def country(persons):
    for person in persons:
        if person.nationality == 'Swedish':
            yield person 

def male(persons):
    for person in persons:
        if person.sex == 'male':
            yield person            

def life(persons):
    for person in persons:
        if person.death == 0:
            yield person

def youngest(persons):
    yield max(persons, key=lambda x: x.birth).name

print(*youngest(life(male(country(persons)))))
"""

# через генераторные выражения
"""
country = (el for el in persons if el.nationality == 'Swedish')
male = (el for el in country if el.sex == 'male')
life = (el for el in male if el.death == 0)

def youngest(persons):
    yield max(persons, key=lambda x: x.birth).name

print(*youngest(life))
"""


# Функция parse_ranges()
"""
def parse_ranges(ranges):   
    for inter in ranges.split(','):
        a,b = inter.split('-')
        interval = (el for el in range(int(a),int(b)+1))
        yield from interval

print(*parse_ranges('1-2,4-4,8-10'))
"""

# Функция filter_names()
"""
def filter_names(names, ignore_char, max_names):
    res_gen = (name for name in names if name[0].lower() != ignore_char and name.isalpha())
    for _ in range(max_names):
        try:
            yield next(res_gen)
        except StopIteration:
            pass

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 'D', 3))    
"""

# Инвестиции
"""
with open('D:\py_learning\py_programs\data.csv', 'r', encoding='utf-8') as data_file:
    file_lines = (line.strip('\n').split(',') for line in data_file)
    values = next(file_lines)
    dict_lines = (dict(zip(values, el)) for el in file_lines)
    res = sum(int(el.get('raisedAmt')) for el in dict_lines if el.get('round') == 'a')
    print(res)
"""

# Функция years_days()
"""
from datetime import date, timedelta

def years_days(year):
    start = date(year=year, month=1, day=1)
    stop = date(year=year+1, month=1, day=1)
    delta = timedelta(days=1)
    while start != stop:
        yield start
        start+=delta 

dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))
"""

# Функция txt_to_dict()  
"""
def txt_to_dict():
    temp_dict = {}
    with open('D:\py_learning\py_programs\planets.txt', 'r', encoding='utf-8') as data_file:
        lines = (line for line in data_file)
        for line in lines:
            line = line.strip('\n')
            if len(line) > 1:
                temp_dict.setdefault(line.split(' = ')[0], line.split(' = ')[1])
            else:
                yield temp_dict
                temp_dict = dict()
        yield temp_dict


planets = txt_to_dict()
print(*planets)
"""

# Функция unique()
"""
def unique(iterable):
    double = list()
    for el in iterable:
        if el not in double:
            yield el
            double.append(el)

numbers = [1, 2, 2, 3, 4, 5, 5, 5]
print(*unique(numbers))

#iterator = iter('111222333')
#uniques = unique(iterator)

#print(next(uniques))
#print(next(uniques))
#print(next(uniques)) 
"""

# Функция stop_on()
"""
def stop_on(iterable, obj):
    try:
        for el in iterable:
            if el != obj:
                yield el
            else:
                raise StopIteration
    except StopIteration:
        pass        

numbers = [1, 2, 3, 4, 5]
print(*stop_on(numbers, 4))

#iterator = iter('beegeek')
#print(*stop_on(iterator, 'a'))            
"""

# Функция with_previous()
"""
def with_previous(iterable):
    temp = None
    for el in iterable:
        yield (el, temp)
        temp = el    
        
numbers = [1, 2, 3, 4, 5]
print(*with_previous(numbers))
"""

# Функция pairwise()
"""
def pairwise(iterable):
    temp = iter(iterable)
    try:
        now = next(temp)
    except StopIteration:
        return []
    else:    
        while True:
            try:      
                future = next(temp)
            except StopIteration:
                yield now, None  
                break  
            else:    
                yield now, future
                now = future
                
numbers = [1, 2, 3, 4, 5]
print(*pairwise(numbers))

#print(list(pairwise([])))
"""

# Функция around()
"""
def around(iterable):
    temp = iter(iterable)
    prev = None
    try:
        now = next(temp)
    except StopIteration:
        return []
    else:    
        while True:
            try:
                future = next(temp)
            except StopIteration:
                yield prev, now, None
                break
            else:
                yield prev, now, future
                prev = now
                now = future

numbers = [1, 2, 3, 4, 5]
print(*around(numbers))
"""