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