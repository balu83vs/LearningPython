# Вычисление Фибоначи
####################################################################
"""
from timeit import default_timer

def show_time(func): 
    def wraper(*args):
        start_time = default_timer()
        res = func(*args)
        total_time = default_timer() - start_time
        print('Время выполнения:{:.10f}'.format(total_time))
        print('Результат:{}'.format(res))
        return res
    return wraper    

# вариант Фибоначи 1    
@ show_time
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n not in fib.__dict__.keys():
            fib.__dict__[n] = fib(n-2) + fib(n-1)

        return fib.__dict__[n]

fib(10)

# вариант Фибоначи 2
@ show_time
def fib(step):
    res = [0, 1]
    for i in range(step):
        res.append(res[i] + res[i + 1])
    return res
    
fib(10000)
"""

# разложение матрицы в словарь
"""
from time import perf_counter

def timer(func):                   # декоратор подсчета времени
    def wraper(data):
        time_start = perf_counter()
        res = func(data)
        time_stop = perf_counter()
        time_process = time_stop - time_start
        print('Время выполнения программы: {:.10f}'.format(time_process))
        return res
    return wraper


# через Enumerate
@ timer
def matrix_to_dict_1(matrix: list[list[int|float]]) -> dict[int, list[int|float]]:
    return dict(enumerate(matrix, 1))

# через генератор словаря
@timer
def matrix_to_dict_2(matrix: list[list[int|float]]) -> dict[int, list[int|float]]:
    return {i+1: matrix[i] for i in range(len(matrix))}

matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict_1(matrix))
print()
print(matrix_to_dict_2(matrix))
"""

#
"""
def takes_positive(func):
    def wraper(*args, **kwargs):
        data = set(args)|set(kwargs.values())
        if not all([isinstance(el,int) for el in data]):
            raise TypeError
        else:
            if any([el <= 0 for el in data]):
                raise ValueError
        res = func(*args, **kwargs)
        return res
    return wraper

@takes_positive
def positive_sum(*args):
    return sum(args)
    
try:
    print(positive_sum(10, 20, -10))
except Exception as err:
    print(type(err))
"""

# декораторы с аргументами
"""
import functools as f

def strip_range(start: int, end: int, char: str = '.') -> str:
    def decorator(func):
        @ f.wraps(func)
        def wrapper(*args, **kwargs):
            len_text = len(func(*args, **kwargs))
            if len_text < start and end:
                res = func(*args, **kwargs)
            else:    
                res = f'{func(*args, **kwargs)[:start]}{char*(end-start)}{func(*args, **kwargs)[end:]}'
                if end > len_text:
                    res = res[:len_text]                
            return res
        return wrapper
    return decorator

@strip_range(0, 1)
def beegeek(word, end=" "):
    '''This is... Requiem. What you are seeing is indeed the truth'''
    return word + end

print(beegeek("beegee", end="k"))
print(beegeek.__name__)
print(beegeek.__doc__)
"""

#
"""
import functools as f

def returns(datatype):
    def decorator(func):
        @ f.wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(func(*args, **kwargs), datatype):
                return func(*args, **kwargs)
            else:
                raise TypeError
        return wrapper
    return decorator

@returns(int)
def add(a, b):
    return a + b

try:
    print(add(199, 1))
except TypeError as e:
    print(type(e))
"""

#
"""
import functools as f

def takes(*types):
    def decorator(func):
        @ f.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) == 0:
                if all([isinstance(arg, types) for arg in kwargs.values()]):
                    return func(*args, **kwargs)   
                else:
                    raise TypeError
            elif len(kwargs) == 0:
                if all([isinstance(arg, types) for arg in args]):
                    return func(*args, **kwargs)
                else:
                    raise TypeError
            else:
                if all([isinstance(arg, types) for arg in set(args)|set(kwargs.values())]):
                    return func(*args, **kwargs)
                else:
                    raise TypeError
        return wrapper
    return decorator

@takes(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2], [3, 4]))
except TypeError as e:
    print(type(e))
"""

# добавление аргументов и их значений к декорируемой функции
"""
import functools as f

def add_attrs(**kwargs):
    def decorator(func):
        for kwarg_k, kwargs_v in kwargs.items():
            func.__dict__.setdefault(kwarg_k, kwargs_v)
        @ f.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

@add_attrs(at1=10, at2=20, at3=30, at4=40, atf=50)
def add(a, b):
    '''add docs'''
    return a + b
  
print(add.at1)
print(add.at2)
print(add.at3)
print(add.__name__)
print(add.__doc__)
print(add(1, 2))
print(add(b=12, a=13))
print(add.at4)
print(add.atf)
"""

# обработка исключений из списка
"""
import functools as f

def ignore_exception(*types):
    def decorator(func):
        @ f.wraps(func)
        def wrapper(*args, **kwargs):
            try: 
                res = func(*args, **kwargs)
            except types as err:
                print(f"Исключение {type(err).__name__} обработано")
            else:   
                return res          
        return wrapper
    return decorator

@ignore_exception(ValueError, NameError, ZeroDivisionError, TypeError)
def func(a, b, c):
    '''func docs'''
    raise NameError
 
try:    
    func(1, 2, c=10)
except Exception as e:
    print(type(e))
"""

#
class MaxRetriesException(Exception):
    pass

from functools import wraps

def retry(times):
    def decorator(func):
        @ wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal times
            try:
                res = func(*args, **kwargs)
            except:
                while times != 1:
                    try:
                        res = func(*args, **kwargs)
                    except:
                        times -= 1
                    else:
                        return res                
            else: 
                return res
            finally:
                if times == 1:                   
                    raise MaxRetriesException
        return wrapper
    return decorator