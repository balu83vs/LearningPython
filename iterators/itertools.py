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

# Функция roundrobin
from itertools import cycle

def roundrobin(*args):
    iter_list = []
    final_round = len(max(args, key = lambda x: len(x)))
    for el in args:
        iter_list.append(iter(el))

    res_iter = cycle(iter_list)

    for res in res_iter:
        try:
            yield next(res)
        except StopIteration:
            final_round -= 1
            if final_round == 0:
                break


#roundrobin('abc', 'd', 'ef')
#print(*roundrobin('abc', 'd', 'ef'))
