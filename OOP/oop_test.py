# Не доделал!!!
"""
import functools

def recviz(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not func.__dict__:
            func.__dict__.setdefault('level', 0)
        res = func(*args, **kwargs)
        func.level +=1
        print(' ' * func.level, '<-', res, sep = ' ')
        print(repr(func))
        return res
    return wrapper

@recviz
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
        
fact(5)
"""

# Декоратор @recviz
# процедурное решение
"""
def recviz(func): 
    if recviz.__dict__.get('count') is None:
            recviz.__dict__.setdefault('count', -1)    
    def wraper(*args, **kwargs):
        text = []
        if args:
            text.append(''.join(list(map(str,repr(*args)))))
        if kwargs:
            for key, value in kwargs.items():
                text.append("{0}={1}".format(key, repr(value)))
        text = ', '.join(text)
        recviz.__dict__['count'] += 1
        count = recviz.__dict__.get('count')
        print(f"{'    '*count}-> {func.__name__}({text})")
        res = func(*args, **kwargs)
        recviz.__dict__['count'] -= 1
        print(f"{'    '*count}<- {repr(res)}") 
        return res
    return wraper
"""
# ООП решение
"""
class recviz:
    def __init__(self, func):
        self.func = func
        if self.__dict__.get('count') is None:
            self.__dict__.setdefault('count', -1)
    
    def __call__(self, *args, **kwargs):
        text = []
        if args:
            text.append(''.join(list(map(str,repr(*args)))))
        if kwargs:
            for key, value in kwargs.items():
                text.append("{0}={1}".format(key, repr(value)))
        text = ', '.join(text)    
        self.__dict__['count'] += 1
        step = self.__dict__.get('count')
        print(f"{'    '*step}-> {self.func.__name__}({text})")
        res = self.func(*args, **kwargs)
        self.__dict__['count'] -= 1
        print(f"{'    '*step}<- {repr(res)}")  
        return res

@recviz
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
fib(7)        
        
@recviz
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
        
fib(4)
"""  

# Scales
"""
class Scales:
    def __init__(self, right_weight = 0, left_weight = 0):
        self.right_weight = right_weight
        self.left_weight = left_weight
        
    def add_right(self, weight):
        self.right_weight += weight
    
    def add_left(self, weight):
        self.left_weight += weight
    
    def get_result(self):
        if self.right_weight < self.left_weight:
            return 'Левая чаша тяжелее'
        elif self.right_weight > self.left_weight:
            return 'Правая чаша тяжелее'
        else:
            return 'Весы в равновесии'

scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)

print(scales.get_result()) 
"""

#
"""
from math import sqrt

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def abs(self):
        return sqrt(self.x**2 + self.y**2)

vector = Vector(3, 4)

print(vector.x, vector.y)
print(vector.abs())    
"""

# ежедневник
"""
class Todo:
    def __init__(self):
        self.things = []
        self.max_priority = 0
        self.min_priority = 100
        
    def add(self, name: str, priority: int) -> None:
        self.things.append((name, priority))
        if priority > self.max_priority:
            self.max_priority = priority
        if priority < self.min_priority:   
            self.min_priority = priority
        
        
    def get_by_priority(self, n: int) -> list:
        return [el[0] for el in list(filter(lambda x: x[1] == n, self.things))]
    
    def get_low_priority(self):
        return [el[0] for el in list(filter(lambda x: x[1] == self.min_priority, self.things))]
    
    def get_high_priority(self):
        return [el[0] for el in list(filter(lambda x: x[1] == self.max_priority, self.things))] 
    
todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))
"""

# Почтальон
"""
class Postman:
    def __init__(self):
        self.delivery_data = []
        
    def add_delivery(self, street, build, app):
        self.delivery_data.append((street, build, app))
    
    def get_houses_for_street(self, street):
        temp_list = [el[1] for el in list(filter(lambda x: x[0] == street, self.delivery_data))]
        res_dict = {el: None for el in temp_list}
        return list(res_dict.keys())
    
    def get_flats_for_house(self, street, build):
        temp_list = [el[2] for el in list(filter(lambda x: x[0] == street and x[1] == build, self.delivery_data))]
        res_dict = {el: None for el in temp_list}
        return list(res_dict.keys())

postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
"""

#
"""
from re import sub

class Wordplay:
    def __init__(self, words = []):
        self.words = words.copy() # делаем поверхностную копию входного списка, чтобы изолировать его от дальнейших изменений 
        
    def add_word(self, word: str) -> None:
        if word not in self.words:
            self.words.append(word)
    
    def words_with_length(self, n: int) -> list:
        return list(filter(lambda x: len(x) == n, self.words))
    
    def only(self, *args: str) -> list:
        temp_list = []
        text = ''.join([el for el in args])
        return [word for word in self.words if len(sub(fr'[{text}]','',word)) == 0]          
    
    def avoid(self, *args: str) -> list:
        temp_list = []
        text = ''.join([el for el in args])
        return [word for word in self.words if len(sub(fr'[{text}]','',word)) == len(word)]
    
words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)
"""    

# шахматы
"""
class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.horizontal_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    
    def get_char(self):
        return 'N'
    
    def can_move(self, x, y):
        var_list = [(2,1), (-2,1), (2,-1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]
        res = any([(self.horizontal_dict.get(x), y) == (self.horizontal_dict.get(self.horizontal) + i[0], self.vertical + i[1]) for i in var_list])
        return res
            
    def move_to(self, x, y):
        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y
              
    def draw_board(self):
        temp_list = []
        for i in range(8,0,-1):
            for j in 'abcdefgh':
                if i == self.vertical and j == self.horizontal:
                    temp_list.append(self.get_char())
                elif self.can_move(j,i):
                    temp_list.append('*')
                else:
                    temp_list.append('.')
            print(*temp_list, sep = '')        
            temp_list = []

knight = Knight('a', 1, 'white')

knight.draw_board()
knight.move_to('e', 8)
print()
knight.draw_board()
"""

#
"""
class BankAccount:
    def __init__(self, balance = 0):
        self._balance = balance
        
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            raise ValueError ('На счете недостаточно средств')
    
    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount) 

account1 = BankAccount(balance=100)
account2 = BankAccount(balance=0)
account1.transfer(account2, 20)
print(account1.get_balance())
print(account2.get_balance())
"""

# 
"""
class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def set_name(self, name):
        if isinstance(name, str):
            if len(name) != 0 and name.isalpha():
                self._name = name
            else:
                raise ValueError('Некорректное имя')    
        else:
            raise ValueError('Некорректное имя')
            
    def set_age(self, age):
        if age in range(0,111) and isinstance(age, int):
            self._age = age
        else:
            raise ValueError('Некорректный возраст') 
        
user = User('Гвидо', 67)

user.set_name('Тимур')
user.set_age(30)

print(user.get_name())
print(user.get_age())
"""       

# login password
"""
def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10**9

class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password
    
    @property
    def login(self):
        return self._login 
    @login.setter
    def login(self, login):
        raise AttributeError('Изменение логина невозможно')
    
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = hash_function(password)

account = Account('timyr-guev', 'lovebeegeek')

print(account.password)
account.login = 'verylovebeegeek'
account.password = 'verylovebeegeek'
print(account.password)
"""

# многочлен
"""
from math import sqrt

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    @property
    def x1(self):
        if self.b**2 - 4*self.a*self.c >= 0:
            return (-self.b - sqrt(self.b**2 - 4*self.a*self.c))/(2*self.a)
        else:
            return None
        
    @property
    def x2(self):
        if self.b**2 - 4*self.a*self.c >= 0:
            return (-self.b + sqrt(self.b**2 - 4*self.a*self.c))/(2*self.a)
        else:
            return None
    
    @property
    def view(self):
        temp1 = ''
        temp2 = '+'
        temp3 = '+'
        if self.a < 0:
            temp1 = '-'
        if self.b < 0:
            temp2 = '-'
        if self.c < 0:
            temp3 = '-'        
        return f'{temp1}{abs(self.a)}x^2 {temp2} {abs(self.b)}x {temp3} {abs(self.c)}'
    
    @property
    def coefficients(self):
        return (self.a, self.b, self.c)
    
    @coefficients.setter
    def coefficients(self, coefficients):
        self.a = coefficients[0]
        self.b = coefficients[1]
        self.c = coefficients[2]

polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)
print(polynom.b)
print(polynom.c)        


polynom = QuadraticPolynomial(-1, -2, 3)
print(polynom.view)
print(polynom.coefficients)        

polynom = QuadraticPolynomial(1, 2, -3)
polynom.coefficients = (1, -5, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)
"""

# color
"""
from re import findall

class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode
        
    @property
    def hexcode(self):
        return self._hexcode
    
    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode
        color_hex = findall(r'[A-Z0-9]{2}', self._hexcode)
        self.r = int(color_hex[0], 16)
        self.g = int(color_hex[1], 16)
        self.b = int(color_hex[2], 16)

color = Color('0000FF')
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)       

color = Color('0000FF')
color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

#________________________
color = Color('0000FF')
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

print()

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

#_____________________
hexcodes = ['FC5A5E', '13AABE', '851149', 'AAAAAA', 'FFFFFF', 'B6A1D8', 'ABCDEF', 'FEDCBA', '123456', '999999']
count = 1
for hc in hexcodes:
    color = Color(hc)
    print(f'Цвет № {count}')
    print(color.hexcode)
    print(color.r, color.g, color.b, sep='\n')
    print()
    count += 1
"""    

# различные варианты внесения данных в класс
"""
class QuadraticPolynomial:
    def __init__(self, *args):
        self.a, self.b, self.c = args
    
    @classmethod
    def from_iterable(cls, args):
        return cls(*args)
    
    @classmethod
    def from_str(cls, args):
        return cls(*map(float, args.split(' ')))
    
polynom = QuadraticPolynomial(1, -5, 6)
print(polynom.a)
print(polynom.b)
print(polynom.c)

polynom = QuadraticPolynomial.from_iterable([2, 13, -1])
print(polynom.a)
print(polynom.b)
print(polynom.c)

polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')
print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)
"""

#
"""
class Pet:
    pets_list = []

    def __init__(self, name):
        self.name = name
        self.pets_list.append(self)    

    @classmethod
    def first_pet(cls):  
        if cls.pets_list:
            return cls.pets_list[0]
        
    @classmethod
    def last_pet(cls):
        if cls.pets_list:
            return cls.pets_list[-1]
        
    @classmethod
    def num_of_pets(cls):
        return len(cls.pets_list)
        

print(Pet.first_pet())
print(Pet.last_pet())
print(Pet.num_of_pets())

       
pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())


pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')
pet4 = Pet('Ratchet')
pet5 = Pet('Ratchet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())
"""

#
"""
from re import sub, IGNORECASE

class StrExtension:
    
    def __init__(self):
        pass
    
    @staticmethod
    def remove_vowels(string):
        string = sub(r'[aeiouy]', '', string, flags= IGNORECASE)
        return string
    
    @staticmethod
    def leave_alpha(string):
        string = sub(r'[^a-z]', '', string, flags= IGNORECASE)
        return string
    
    @staticmethod
    def replace_all(string,chars,char):
        string = sub(fr'[{chars}]', char, string)
        return string

print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))    

print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))

print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
"""

#
"""
from re import findall

class CaseHelper:
    @staticmethod
    def is_snake(string):
        if ' ' not in string and string[0].isalpha() and string[-1].isalpha() and string == string.lower():
            return True
        else:
            return False
    
    @staticmethod
    def is_upper_camel(string):
        if string.isalpha() and string[0] == string[0].upper() and string[-1] == string[-1].lower():
            return True
        else:
            return False
    
    @staticmethod
    def to_snake(string):
        if __class__.is_snake(string) == False:
            return '_'.join(findall(r'[A-Z][a-z]*', string)).lower()
        return string
    
    @staticmethod
    def to_upper_camel(string):
        if __class__.is_upper_camel(string) == False:
            return ''.join(list(map(lambda x: x.capitalize(), string.split('_'))))        
        return string    

    
print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))

print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))

print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))
#beegeek
#bee_geek

print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))
#Beegeek
#BeeGeek

cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup']
for case in cases:
    print(CaseHelper.is_snake(case))
# TrueTrueFalseFalseFalseFalseTrueTrueTrue
    
cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup', 'AssertEqual', 'SetUp']
for case in cases:
    print(CaseHelper.is_upper_camel(case))  
#      

cases = ['AssertEqual', 'SetUp', 'TearDown', 'AddModuleCleanup', 'AssertRaisesRegex', 'AssertAlmostEqual', 'AssertNotAlmostEqual']
for case in cases:
    print(CaseHelper.to_snake(case)) 
# assert_equal set_up tear_down add_module_cleanup assert_raises_regex assert_almost_equal assert_not_almost_equal       

cases = ['assert_equal', 'tear_down', 'assert_raises_regex', 'assert_almost_equal', 'assert_not_almost_equal', 'beegeek']
for case in cases:
    print(CaseHelper.to_upper_camel(case))
# AssertEqual TearDown AssertRaisesRegex AssertAlmostEqual AssertNotAlmostEqual Beegeek   
    """    

#
"""
from functools import singledispatchmethod

class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @format.register(int)
    def f_is_int(data):
        print(f'Целое число: {data}')
    
    @format.register(float)
    def f_is_float(data):
        print(f'Вещественное число: {data}')
    
    @format.register(list)
    @format.register(tuple)
    def f_is_list(data):
        if isinstance(data, list):
            print('Элементы списка:', end = ' ')
        else:
            print('Элементы кортежа:', end = ' ')
        print(*data, sep = ', ')
    
    @format.register(dict)
    def f_is_dict(data):
        print('Пары словаря:', end = ' ')
        print(*data.items(), sep = ', ')

Formatter.format(1337)
Formatter.format(20.77)
#Целое число: 1337
#Вещественное число: 20.77

Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))
#Элементы списка: 10, 20, 30, 40, 50
#Элементы кортежа: [1, 3], [2, 4, 6]

Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})
#Пары словаря: ('Cuphead', 1), ('Mugman', 3)
#Пары словаря: (1, 'one'), (2, 'two')
#Пары словаря: (1, True), (0, False)

try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)
#Аргумент переданного типа не поддерживается

not_supported = [str, type, bool, dict, tuple, list]
for item in not_supported:
    try:
        Formatter.format(item)
    except TypeError as e:
        print(e)
#Аргумент переданного типа не поддерживается
#Аргумент переданного типа не поддерживается
#Аргумент переданного типа не поддерживается
#Аргумент переданного типа не поддерживается
#Аргумент переданного типа не поддерживается
#Аргумент переданного типа не поддерживается        
"""

#
"""
from datetime import date, timedelta
from functools import singledispatchmethod

class BirthInfo:

    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(str)
    def is_str(self, birth_date):
        birth_date = list(map(int, birth_date.split('-')))
        self.birth_date = date(*birth_date)
        
    @__init__.register(date)
    def is_iso(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(list)
    @__init__.register(tuple)
    def is_list_tuple(self, birth_date):
        self.birth_date = date(*birth_date) 
   
    
    @property
    def age(self):
        count = 0
        today = date.today()
        delta_year = timedelta(days = 365)
        for year in range(self.birth_date.year+1, today.year):
            if year%4 == 0:
                count+=1      
        add_days = timedelta(days = count)
        res = (today - self.birth_date - add_days) // delta_year
        return res

birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])
print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)
# 2020-09-18
# 2010-10-10
# 2016-01-01

birthday = date(2020, 9, 18)
birthinfo = BirthInfo(birthday)
print(birthinfo.age)
# 2

birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(type(birthinfo1.birth_date))
print(type(birthinfo2.birth_date))
print(type(birthinfo3.birth_date))    
#<class 'datetime.date'>
#<class 'datetime.date'>
#<class 'datetime.date'>   
    

errors = [20200918, True, {1: 'one'}, {1, 2, 3}, 100.9]

for obj in errors:
    try:
        BirthInfo(obj)
    except TypeError as e:
        print(e)    
#Аргумент переданного типа не поддерживается
#Аргумент переданного типа не поддерживается
#Аргумент переданного типа не поддерживается
#Аргумент переданного типа не поддерживается
#Аргумент переданного типа не поддерживается        
"""     


############### Строковое представление объектов (методы __str__, __repr__)
#
"""
from functools import singledispatchmethod

class IPAddress:

    @singledispatchmethod
    def __init__(self, ip):
        self.ip = ip
    
    @__init__.register(list)
    @__init__.register(tuple)
    def from_list_or_tuple(self, ip):
        self.ip = '.'.join(list(map(str, ip)))
    
    def __repr__(self):
        return f"IPAddress('{self.ip}')"
    
    def __str__(self):
        return self.ip

ip = IPAddress('8.8.1.1')
print(str(ip))
print(repr(ip))        
"""

#
"""
class AnyClass:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            #self.__dict__[key] = self.__dict__.get(key, value)
            #setattr(self, key, value)
            self.__dict__.update(kwargs)
        res = []
        for key, value in self.__dict__.items():
            if type(value) is str:
                res.append(f"{key}: '{value}'")  
            else:
                res.append(f"{key}: {value}")      
        self.res = ', '.join(res)      

    def __str__(self):      
        return f"{__class__.__name__}: {self.res}"
    
    def __repr__(self):
        return f"{__class__.__name__}({self.res})"        

any = AnyClass()
print(str(any))
print(repr(any))

obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)
print(str(obj))
print(repr(obj))

attrs = {
    'name': 'Guido van Rossum',
    'birth_date': '31.01.1956',
    'age': 67,
    'career': 'python guru'
}
obj = AnyClass(**attrs)
print(obj.name)
print(obj.birth_date)
print(obj.age)
print(obj.career)
"""

############################## Сравнение объектов (методы __eq__, __ne__)
#
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"{__class__.__name__}({self.x}, {self.y})"
    
    def __eq__(self, other):
        if isinstance(other, tuple):
            if self.x == other[0] and self.y == other[1] and len(other) == 2:
                return True
        else:
            try:
                if self.x == other.x and self.y == other.y:
                    return True
            except:
                return NotImplemented        
        return NotImplemented
    
a = Vector(1, 2)
b = Vector(1, 2)
print(a == b)
print(a != b)   

a = Vector(1, 2)
b = Vector(3, 4)
c = Vector(5, 6)
vectors = [a, b, c]
print(vectors)

a = Vector(0, 1)
not_supported = [[1, 2], True, (1, 2, 3, 4), 'beegeek', {'name': 'Grace Hopper'}, {18, 22}]
for item in not_supported:
    print(a == item)
"""

######################### методы __lt__, __gt__, __le__, __ge__, @total_ordering
#
"""
from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, word):
        self.word = word
        
    def __str__(self):
        return self.word.lower().capitalize()
    
    def __repr__(self):
        return f"{__class__.__name__}('{self.word}')"
    
    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented

print(Word('bee') == Word('hey'))
print(Word('bee') < Word('geek'))
print(Word('bee') > Word('geek'))
print(Word('bee') <= Word('geek'))
print(Word('bee') >= Word('gee'))
"""    

#
"""
from functools import total_ordering

@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        
    def __str__(self):
        return f"{self.year}-{self.month}"
    
    def __repr__(self):
        return f"{__class__.__name__}({self.year}, {self.month})"
    
    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        if isinstance(other, tuple) and len(other) == 2:
            return self.year == other[0] and self.month == other[1]      
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Month):
            return (self.year == other.year and self.month < other.month) or (self.year < other.year)
        if isinstance(other, tuple) and len(other) == 2:
            return (self.year == other[0] and self.month < other[1]) or (self.year < other[0])  
        return NotImplemented

print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))

months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]
print(sorted(months))
print(min(months))
print(max(months))
"""
#
"""
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version):      
        self.version = __class__._transform(version)
    
    def __str__(self):
        return '.'.join(self.version)  
    
    def __repr__(self):
        return f"{__class__.__name__}('{'.'.join(self.version)}')"
    
    def __eq__(self, other):
        if isinstance(other, Version):
            return list(map(int, self.version)) == list(map(int, other.version))
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Version):
            return list(map(int, self.version)) < list(map(int, other.version))
        return NotImplemented
    
    @staticmethod
    def _transform(version):
        version_list = version.split('.')
        for _ in range(3-len(version_list)):
            version_list.append('0')
        return version_list 

print(Version('3.0.3') == Version('1.11.28'))
print(Version('3.0.3') < Version('1.11.28'))
print(Version('3.0.3') > Version('1.11.28'))
print(Version('3.0.3') <= Version('1.11.28'))
print(Version('3.0.3') >= Version('1.11.28'))

print(Version('3') == Version('3.0'))
print(Version('3') == Version('3.0.0'))
print(Version('3.0') == Version('3.0.0'))

versions = [Version('162.5'), Version('68.3'), Version('173.8'), Version('108.9'), Version('159.6'), Version('145.7'),
            Version('187.6'), Version('137.7'), Version('33.7'), Version('22.4'), Version('199.4'), Version('122.1'),
            Version('47.4'), Version('10.2'), Version('164.9'), Version('191.6'), Version('139.9'), Version('184.4'),
            Version('94.9'), Version('188.6'), Version('56.8'), Version('138.7'), Version('83.2'), Version('59.4'),
            Version('189.7'), Version('128.5')]
print(sorted(versions))
print(min(versions))
print(max(versions))
"""


################# Унарные операции (__pos__, __neg__, __invert__)
#
"""
class ColoredPoint:
    def __init__(self, x, y, color = (0,0,0)):
        self.x, self.y, self.color = x, y, color
        self.new_color = [0,0,0]
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return f"{__class__.__name__}({self.x}, {self.y}, {self.color})"
    
    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)
    def __neg__(self):
        return ColoredPoint(-self.x, -self.y, self.color)
    def __invert__(self):
        self.new_color[0], self.new_color[1], self.new_color[2] = 255 - self.color[0], 255 - self.color[1], 255 - self.color[2]
        return ColoredPoint(self.y, self.x, tuple(self.new_color))

point = ColoredPoint(2, -3)
print(+point)
print(-point)
print(~point)

point1 = ColoredPoint(1, 2, (100, 150, 200))
point2 = ~point1
print(repr(point1))
print(repr(point2))
"""

#
"""
class Matrix:
    def __init__(self, rows, cols, value = 0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = __class__.create_matrix(self.rows, self.cols, self.value)
        
    def __str__(self):
        str_matrix = [' '.join(list(map(str, el))) for el in self.matrix]
        return '\n'.join(str_matrix)
    def __repr__(self):
        return f"{__class__.__name__}({self.rows}, {self.cols})"
    
    def __pos__(self):
        other = Matrix(self.rows, self.cols, self.value)
        other.matrix = self.matrix
        return other
    
    def __neg__(self):
        other = Matrix(self.rows, self.cols, self.value)
        for i in range(self.rows):
            for j in range(self.cols):
                other.matrix[i][j] = -self.matrix[i][j]
        return other
    
    def __invert__(self):
        other = Matrix(self.cols, self.rows, self.value)
        for i in range(self.cols):
            for j in range(self.rows):
                other.matrix[i][j] = self.matrix[j][i]
        return other
    def __round__(self, n = 0):
        other = Matrix(self.rows, self.cols, self.value)
        for i in range(self.rows):
            for j in range(self.cols):
                if n != 0:
                    other.matrix[i][j] = round(self.matrix[i][j], n)
                else:
                    other.matrix[i][j] = round(self.matrix[i][j])        
        return other
    
    def get_value(self, row, col):
        return self.matrix[row][col]
    def set_value(self, row, col, value):
        self.matrix[row][col] = value
 
    @staticmethod
    def create_matrix(rows, cols, value):
        matrix = []
        temp_list = []
        for _ in range(rows):
            for _ in range(cols):
                temp_list.append(value)
            matrix.append(temp_list) 
            temp_list = []
        return matrix 
    
print(Matrix(2, 3))

matrix = Matrix(2, 3, 1)
print(+matrix)
print()
print(-matrix)

matrix = Matrix(2, 3, 1)
print(matrix)
print()
print(~matrix)

matrix = Matrix(2, 3)
print(matrix.get_value(0, 0))
print(matrix.get_value(1, 1))
matrix.set_value(0, 0, 100)
matrix.set_value(1, 1, 200)
print(matrix.get_value(0, 0))
print(matrix.get_value(1, 1))

matrix = Matrix(4, 2)
counter = 1
for row in range(4):
    for col in range(2):
        matrix.set_value(row, col, counter)
        counter += 1
print(matrix)
print()
print(~matrix)
"""

## ###################### Арифметические операции __add__, __mul__, __truediv__, __floordiv__
"""
#
class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins, self.fats, self.carbohydrates = proteins, fats, carbohydrates
        
    def __repr__(self):
        return f"{__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})"
    
    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(
                self.proteins+other.proteins, 
                self.fats+other.fats, 
                self.carbohydrates+other.carbohydrates
            )
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(self.proteins / other, self.fats / other, self.carbohydrates / other)
        return NotImplemented
    
    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(self.proteins // other, self.fats // other, self.carbohydrates // other)
        return NotImplemented
    
food1 = FoodInfo(10, 20, 30)
food2 = FoodInfo(10, 10, 20)
print(food1 + food2)
print(food1 * 2)
print(food1 / 2)
print(food1 // 2)    

food1 = FoodInfo(10, 20, 30)
try:
    food2 = (5, 10, 15) + food1
except TypeError:
    print('Некорректный тип данных')
"""

#
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"{__class__.__name__}({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented
    
    def __rmul__(self, other): # отражение операции *
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        return NotImplemented
    
    def __rtruediv__(self, other): # отражение операции /
        return self.__truediv__(other)
    
a = Vector(1, 2)
b = Vector(3, 4)
print(a + b)
print(a - b)
print(b + a)
print(b - a)    

a = Vector(3, 4)
print(a * 2)
print(2 * a)
print(a / 2)
"""

#
"""
class SuperString:
    def __init__(self, string):
        self.string = string
        
    def __str__(self):
        return self.string
    
    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented
        
    def __mul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[:int(len(self.string)/other)])
        return NotImplemented
    
    def __lshift__(self, other):
        if isinstance(other, int):
            if len(self.string) > other:
                return SuperString(self.string[:len(self.string) - other])
            return SuperString('')           
        return NotImplemented    
    
    def __rshift__(self, other):
        if isinstance(other, int):
            if len(self.string) > other:
                return SuperString(self.string[other:])
            return SuperString('')            
        return NotImplemented
    
s1 = SuperString('bee')
s2 = SuperString('geek')
print(s1 + s2)
print(s2 + s1)    

s = SuperString('beegeek')
print(s * 2)
print(3 * s)
print(s / 3)

s = SuperString('beegeek')
print(s << 4)
print(s >> 3)
"""

#
"""
from datetime import time
class Time:
    def __init__(self, hours, minutes):
        self.hours, self.minutes = __class__.time_format(hours, minutes)
        
    def __str__(self):
        return time.strftime(time(hour=self.hours, minute=self.minutes), "%H:%M")
    
    def __add__(self, other):
        if isinstance(other, Time):
            return Time(*__class__.time_format(self.hours + other.hours, self.minutes + other.minutes))
        return NotImplemented
        
    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours += other.hours
            self.minutes += other.minutes
            self.hours, self.minutes = __class__.time_format(self.hours, self.minutes)
            return self
        else:
            return NotImplemented      
        
    @staticmethod
    def time_format(hours, minutes):
        if minutes >= 60:
            add_hours = minutes // 60
            minutes = minutes % 60
            hours = hours + add_hours
        if hours >= 24:    
            hours = hours % 24
        return hours, minutes
    
time1 = Time(2, 30)
time2 = Time(3, 10)
print(time1 + time2)
print(time2 + time1)

time1 = Time(2, 30)
time2 = Time(3, 10)
time1 += time2
print(time1)
print(time2)

time1 = Time(25, 20)
time2 = Time(10, 130)
print(time1)
print(time2)
"""

#
"""
class Queue:
    def __init__(self, *args):
        self.args = list(args)
        
    def __str__(self):
        return ' -> '.join(list(map(str, self.args)))
    
    def __eq__(self, other):
        if isinstance(other, Queue):
            if len(self.args) != len(other.args):
                return False
            else:
                for i in range(len(self.args)):
                    if self.args[i] != other.args[i]:
                        return False
                return True    
        return NotImplemented    
    
    def __add__(self, other):
        if isinstance(other, Queue):
            self.args.extend(other.args)
            return Queue(*self.args)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, Queue):
            if isinstance(other, Queue):
                self.args.extend(other.args)
            return self
        if isinstance(other, tuple):
            for el in other:
                self.args.append(el)
            return self
        return NotImplemented
    
    def __rshift__(self, other):
        if isinstance(other, int):
            if len(self.args) > other:
                return Queue(*self.args[other:])
            return Queue('')            
        return NotImplemented
    
    def add(self, *args):
        return __class__.__iadd__(self, args)
    
    def pop(self):
        if len(self.args) == 0:
            return None
        return self.args.pop(0)
    
queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)
queue1 += queue2
print(queue1)

queue = Queue(1, 2)
queue.add(3)
queue.add(4, 5)
print(queue)
print(queue.pop())
print(queue)

queue = Queue(*'beegeek')
for i in range(9):
    print(f'Queue >> {i} =', queue >> i)    
"""    

#######################  Вызываемые объекты метод __call__

# Фибоначи
"""
class CachedFunction:
    def __init__(self, func):
        self.func = func
        if self.__dict__.get('cache_dict') is None:
            self.cache_dict = dict()
    
    def __call__(self, *args):
        if self.cache_dict.get(args) is None:
            self.cache_dict.setdefault(args, self.func(*args))
        return self.cache_dict.get(args)
    
    @property
    def cache(self):
        return self.cache_dict
    
@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
    
print(slow_fibonacci(100))
print(slow_fibonacci.cache)    
"""

# сортировка по любому количеству атрибутов экземпляра класса
"""
class SortKey:
    def __init__(self, *args):
        self.args = args
        
    def __call__(self, *args):
        return [getattr(*args, el, None) for el in self.args]  
    
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]
print(sorted(users, key=SortKey('name')))
print(sorted(users, key=SortKey('name', 'age')))
print(sorted(users, key=SortKey('age')))
print(sorted(users, key=SortKey('age', 'name')))
"""

## Преобразования типов __bool__, __int__, __float__, __complex__, __oct__, __hex__
# градусник
"""
class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature
        
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        return cls((fahrenheit-32)*5/9)
    
    def to_fahrenheit(self):
        return (self.temperature * (9/5)) + 32
    
    def __str__(self):
        return f"{round(self.temperature, 2)}°C"
    
    def __bool__(self):
        if self.temperature > 0:
            return True
        else:
            return False
    
    def __int__(self):
        return int(self.temperature)
    
    def __float__(self):
        return float(self.temperature)

t = Temperature(5.5)
print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())      

t1 = Temperature(1)
t2 = Temperature(0)
t3 = Temperature(-1)
print(bool(t1))
print(bool(t2))
print(bool(t3))

t = Temperature.from_fahrenheit(41)
print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())
"""

# Сравнение римских чисел RomanNumeral
"""
from functools import total_ordering

@total_ordering
class RomanNumeral:
    def __init__(self, roman_number: str) -> None:
        self.roman_number = roman_number
        
    def __str__(self):
        return self.roman_number
    
    def __int__(self):
        arab_number = 0
        figure_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if len(self.roman_number) == 1:
            arab_number = figure_dict.get(self.roman_number)
        else:
            temp_count = 0
            for el in [figure_dict.get(self.roman_number[i]) for i in range(len(self.roman_number))]:
                if el <= temp_count:
                    arab_number += el
                else: 
                    arab_number += (el - temp_count) - temp_count
                temp_count = el 
        return arab_number
    
    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.__int__() == other.__int__()        
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.__int__() < other.__int__()
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            arab_number = self.__int__() + other.__int__()  
            return RomanNumeral(self.over_int(arab_number))
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            arab_number = self.__int__() - other.__int__()  
            return RomanNumeral(self.over_int(arab_number))
        return NotImplemented
    
    @staticmethod
    def over_int(arab_number):
        string_number = str(arab_number)
        figure_dict = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        res_list = []
        for figure in [int(string_number[i])*10**(len(string_number)-1-i) for i in range(len(string_number)) if int(string_number[i]) > 0]:
            res_string = figure_dict.get(figure)
            if res_string is None:
                res_string = ''
                for el in sorted(figure_dict, reverse = True):
                    if figure/el >= 1:
                        res_string += figure_dict[el]*(figure//el)
                        figure -= el*(figure//el)
            res_list.append(res_string)     
        return ''.join(res_list)

a = RomanNumeral('X')
b = RomanNumeral('X')
print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

number = RomanNumeral('MXL') + RomanNumeral('MCDVIII') - RomanNumeral('I')
print(number)
print(int(number))

roman = RomanNumeral('L')
print(roman.__eq__(1))
print(roman.__ne__(1.1))
print(roman.__gt__(range(5)))
print(roman.__lt__([1, 2, 3]))
print(roman.__ge__({4, 5, 6}))
print(roman.__le__({1: 'one'}))
"""

## Работа с атрибутами __getatribute__, __getattr__, __setattr__, __delattr__

# Защита от изменения и удаления атрибутов
"""
class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def __setattr__(self, key, value):
        if self.__dict__.get(key) == None:
            self.__dict__[key] = value
        else:    
            raise AttributeError ('Изменение значения атрибута невозможно')
        
    def __delattr__(self, attr):    
        raise AttributeError ('Удаление атрибута невозможно')
    
videogame = Const(name='Cuphead')
videogame.developer = 'Studio MDHR'
print(videogame.name)
print(videogame.developer)

videogame = Const(name='Dicso Elysium')
try:
    videogame.name = 'Half-Life: Alyx'
except AttributeError as e:
    print(e)  

videogame = Const(name='The Last of Us')
try:
    del videogame.name
except AttributeError as e:
    print(e)    
"""    

# Защита от удаления атрибутов _ и __
"""
class ProtectedObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)
        
    def __getattribute__(self, attr):
        return object.__getattr__(self, attr)
        
    def __getattr__(self, attr):
        if attr[0]!='_':
            return object.__getattribute__(self, attr)
        else:
            raise AttributeError ('Доступ к защищенному атрибуту невозможен')
            
    def __setattr__(self, key, value):
        if key[0] == '_':
            raise AttributeError ('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, key, value)
        
    def __delattr__(self, attr):
        if attr[0] == '_':
            raise AttributeError ('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, attr) 

user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')
try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)

user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')
del user.login
print('Успешное удаление атрибута')    

user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')
del user.login
try:
    print(user.login)
except AttributeError:
    print('Атрибут отсутствует')
"""