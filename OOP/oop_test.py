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