######################################################## Не доделал!!! ########################################################
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


######################################################## Декоратор @recviz ########################################################
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


######################################################## Scales ########################################################
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


########################################################          ########################################################
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


######################################################## ежедневник ########################################################
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


######################################################## Почтальон ########################################################
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


########################################################             ########################################################
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


######################################################## шахматы ########################################################
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


########################################################              ########################################################
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


########################################################                 ######################################################## 
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


######################################################## login password ########################################################
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


######################################################## многочлен ########################################################
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


######################################################## color ########################################################
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


######################################################## различные варианты внесения данных в класс ###############################################
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


########################################################                      ########################################################
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


########################################################                     ########################################################
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


########################################################                ########################################################
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


########################################################                 ########################################################
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


########################################################                  ########################################################
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


######################################################## Строковое представление объектов (методы __str__, __repr__) ##############################
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


######################################################## Сравнение объектов (методы __eq__, __ne__) ###############################################
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


######################################################## методы __lt__, __gt__, __le__, __ge__, @total_ordering ###################################
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


######################################################## Унарные операции (__pos__, __neg__, __invert__) ########################################
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


######################################################## Арифметические операции __add__, __mul__, __truediv__, __floordiv__ ######################
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


########################################################  Вызываемые объекты метод __call__ ########################################################
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


######################################################## Преобразования типов __bool__, __int__, __float__, __complex__, __oct__, __hex__
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


######################################################## Работа с атрибутами __getatribute__, __getattr__, __setattr__, __delattr__

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


######################################################## Hash функции ########################################################
#
"""
def limited_hash(left, right, hash_function = hash):
    def new_hash(arg):
        hash_value = hash_function(arg)
        while hash_value not in [el for el in range(left,right+1)]:
            if hash_value > right:
                hash_value = left + ((hash_value - right)-1)
            elif hash_value < left:
                hash_value = right - ((left - hash_value)-1)
        return hash_value         
    return new_hash

hash_function = limited_hash(10, 15)
print(hash_function(16))
print(hash_function(17))
print(hash_function(21))
print(hash_function(22))
print(hash_function(23))

hash_function = limited_hash(10, 15)
print(hash_function(9))
print(hash_function(8))
print(hash_function(4))
print(hash_function(3))
print(hash_function(2))

hash_function = limited_hash(2, 3, hash_function=lambda obj: len(str(obj)))
print(hash_function('a'))
print(hash_function('ab'))
print(hash_function('abc'))
print(hash_function('abcd'))
print(hash_function('abcde'))
print(hash_function('abcdef'))
print(hash_function('abcdefg'))

def hash_function(obj):
    return sum(index * ord(character) for index, character in enumerate(str(obj), start=1))
hash_function = limited_hash(10, 15, hash_function)
array = [1366, -5502567186.7395, 'zZQyrjYzdgcabTZPATPl', False, {'монета': -671699723096.267, 'лететь': 5151},
         (False, True, 897, -844416.51017117, 1101),
         [True, 171664.794743347, True, False, 'UypAaBSjBWYWBYbmRTdN', 4044844490314.56]]
for item in array:
    print(hash_function(item))
"""


#
"""
class Row:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        
    def __repr__(self):
        res_list = [
            f"{key}='{value}'" if isinstance(value, str) 
            else f"{key}={value}" 
            for key, value in self.__dict__.items()
                   ] 
        return f"{__class__.__name__}({', '.join(res_list)})"
    
    def __getattribute__(self, attr):
        return object.__getattr__(self, attr)
    
    def __getattr__(self, attr):
        return object.__getattribute__(self, attr)
    
    def __setattr__(self, key, value):
        if self.__dict__.get(key) is None:
            raise AttributeError ('Установка нового атрибута невозможна')
        else:
            raise AttributeError ('Изменение значения атрибута невозможно')
    
    def __delattr__(self, attr):
        raise AttributeError ('Удаление атрибута невозможно')
        
    def __eq__(self, other):
        if isinstance(other, Row):
            return list(self.__dict__.items()) == list(other.__dict__.items())
        return NotImplemented
    
    def __hash__(self):
        keys = [ord(key) if isinstance(key, str) else key for key in self.__dict__.keys()]
        values = [ord(value) if isinstance(value, str) else value for value in self.__dict__.values()]
        return sum([(i+1)*keys[i]*values[-i+1] for i in range(len(keys))]) % 1200 
    
row = Row(a='A', b='B', c='C')
print(row)
print(row.a, row.b, row.c)    

row1 = Row(a=1, b=2, c=3)
row2 = Row(a=1, b=2, c=3)
row3 = Row(b=2, c=3, a=1)
print(row1 == row2)
print(hash(row1) == hash(row2))
print(row1 == row3)
print(hash(row1) == hash(row3))

row = Row(a=1, b=2, c=3)
try:
    row.d = 4
except AttributeError as e:
    print(e)
"""    


#
"""
class SkipIterator:

    def __init__(self, iterable, n):
        self.iterable, self.n = iterable, n
        self.index = -1
        
    def __iter__(self):
        if not isinstance(self.iterable, (list,str,tuple,dict,set)):
            res_list = []
            while True:
                try:
                    if self.index == -1 or self.n == 0:
                        self.index += 1
                        res_list.append(next(self.iterable))
                    else:
                        self.index += self.n + 1 
                        for _ in range(self.n):
                            next(self.iterable)   
                        res_list.append(next(self.iterable))                        
                except StopIteration:
                    return iter(res_list)
        else:
            return self
    
    def __next__(self):   
            if self.index == -1 or self.n == 0:
                self.index += 1
            else:
                self.index += self.n + 1  
            try:
                return self.iterable[self.index]
            except:
                raise StopIteration

skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)   # пропускаем по два элемента
print(*skipiterator)

data = ['к', 'б', 'ш', 'к', 'к', 'о', 'т', 'г', 'о', 'д', 'р', 'в', 'с', 'с', 'и', 'о', 'в', 'п', 'у', 'с', 'л', 'т',
        'г', 'т', 'з', 'ь', 'о', 'п', 'н', 'в', 'и', 'н', 'с', 'п', 'р', 'ш', 'е', 'к', 'н', 'с', 'у', 'в', 'п', 'т',
        'х', 'т', 'с', 'с', 'л', 'с']
skipiterator = SkipIterator(iter(data), 4)
print(*skipiterator)
"""


#
"""
class LoopTracker:

    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.index = 0
        self.empty_index = 0
        if self.iterable:
            self.first_el = self.iterable[0]
        else:
            self.first_el = None  
        self.last_el = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.iterable:
            self.index += 1
            self.last_el = self.iterable.pop(0)
            return self.last_el
        self.empty_index += 1
        raise StopIteration
        
    @property
    def accesses(self):
        return self.index
    
    @property
    def empty_accesses(self):
        return self.empty_index
    
    @property
    def first(self):
        if self.first_el != None:
            return self.first_el
        raise AttributeError ('Исходный итерируемый объект пуст')
    
    @property
    def last(self):
        if self.last_el:
            return self.last_el
        raise AttributeError ('Последнего элемента нет')
    
    def is_empty(self):
        if self.iterable:
            return False
        return True
    
loop_tracker = LoopTracker(dict.fromkeys(range(100)))

print(next(loop_tracker))
print(next(loop_tracker))
print(next(loop_tracker))
print(loop_tracker.accesses)
print(loop_tracker.first)
print(loop_tracker.last)
print(loop_tracker.is_empty())
"""    


#
"""
from copy import deepcopy
import itertools

class SequenceZip:

    def __init__(self, *args):
        self.args = deepcopy(args)
        if self.args:
            if isinstance(self.args[0], dict):
                temp_list = []
                for el in self.args:
                    temp_list.append(list(el.keys()))
                self.args = temp_list    
            self.min_len = min([len(list(el)) for el in self.args])
            self.args = self.transform(self.args)
              
    def __len__(self):
        return len(list(self.args))
       
    def __getitem__(self, key): 
        for _ in range(key):
            next(self.args)
        return next(self.args)    
        #return self.args[key]
    
    def transform(self, data):
        temp_gen = (el[i] for i in range(self.min_len) for el in data)
        res = (tuple(itertools.islice(temp_gen, 0, len(data))) for _ in range(self.min_len))
        return res
    
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])
print(list(sequencezip))
print(tuple(sequencezip))

sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])
print(len(sequencezip))
print(sequencezip[1])
print(sequencezip[2])

many_large_sequences = [range(100000) for _ in range(100)]
sequencezip = SequenceZip(*many_large_sequences)
print(sequencezip[99999])  

data = {'bee': 'bee', 'geek': 'geek'}
sequencezip = SequenceZip(data)
data['python'] = 'python'
print(data)
print(len(sequencezip))
print(list(sequencezip))

data = {'bee': 'bee', 'geek': 'geek'}
sequencezip = SequenceZip(data)
print(sequencezip[0])
print(list(sequencezip))
"""


#
"""
class OrderedSet:

    def __init__(self, iterable = []):
        self.iterable = iterable.copy()   
        self.iterable = list({el: self.iterable.count(el) for el in self.iterable}.keys())
        
    def __getitem__(self, key):
        self.iterable = list({el: self.iterable.count(el) for el in self.iterable}.keys())
        return self.iterable[key]
    
    def __len__(self):
        return len(self.iterable)
    
    def __contains__(self, item):
        return item in self.iterable
    
    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return (
                {el: self.iterable.index(el) for el in self.iterable} 
                == 
                {el: other.iterable.index(el) for el in other.iterable}
            )
        if isinstance(other, set):
            return sorted(self.iterable) == sorted(other)
        return NotImplemented
    
    def add(self, element):
        self.iterable.append(element)
        
    def discard(self, element):
        try:
            self.iterable.remove(element)
        except ValueError:
            pass

orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])
print(*orderedset)
print(len(orderedset))

orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])
print('python' in orderedset)
print('C++' in orderedset)

orderedset = OrderedSet()
orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)    

data = ['Ada Lovelace'] * 1000
orderedset = OrderedSet(data)
print(len(orderedset))

orderedset = OrderedSet([1, 2, 3, 4])
not_supported = [120, {1: 'one'}, True, 'pi = 3', 17.9]
for item in not_supported:
    print(item != orderedset)
"""


#
"""
import copy

class AttrDict:

    def __init__(self, data = {}):
        self.data = copy.deepcopy(data) 
        
    def __len__(self):
        return len(self.data)
        
    def __iter__(self):
        yield from self.data.keys()
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr)
    
    def __getattr__(self, attr):
        return self.data[attr]

    def __setattr__(self, attr, value):
        if self.__dict__.get(attr) != None:
            raise AttributeError ('Изменение атрибута запрещено')
        object.__setattr__(self, attr, value)   
        
    def __delattr__(self, attr):
        raise AttributeError ('Удаление атрибута запрещено') 
    
attrdict = AttrDict({'name': 'X Æ A-12', 'father': 'Elon Musk'})
print(attrdict['name'])
print(attrdict.father)
print(len(attrdict))    

attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})
attrdict['city'] = 'Dubai'
attrdict['age'] = 31
print(attrdict.city)
print(attrdict.age)

attrdict = AttrDict()
attrdict['school_name'] = 'BEEGEEK'
print(attrdict['school_name'])
print(attrdict.school_name)
"""


#
"""
import copy

class PermaDict:

    def __init__(self, data = {}):
        self.data = copy.deepcopy(data)
        
    def keys(self):
        return self.data.keys()
    
    def values(self):
        return self.data.values()
    
    def items(self):
        return self.data.items()
    
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        yield from self.keys()
        
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        if self.data.get(key) == None:
            self.data[key] = value
        else:
            raise KeyError ('Изменение значения по ключу невозможно')
    
    def __delitem__(self, key):
        del self.data[key]

permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})
print(permadict['name'])
print(len(permadict))

permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})
print(*permadict)
print(*permadict.keys())
print(*permadict.values())
print(*permadict.items())

permadict = PermaDict()
permadict['name'] = 'Timur'
permadict['age'] = 30
del permadict['name']
print(permadict['age'])
print(len(permadict))

permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})
try:
    permadict['name'] = 'Arthur'
except KeyError as e:
    print(e)
"""


#
"""
import copy

class HistoryDict:

    def __init__(self, data = {}):
        self.data = copy.deepcopy(data)
        self.memo_dict = {}
        for key, value in self.data.items():
            self.__setitem__(key, value)
            
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        yield from self.data
        
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        if self.memo_dict.get(key) == None:
            self.memo_dict[key] = []
        self.memo_dict[key].append(value)  
        self.data[key] = value
        
    def __delitem__(self, key):
        del self.data[key]
        del self.memo_dict[key]
        
    def keys(self):
        return self.data.keys()
    
    def values(self):
        return self.data.values()
    
    def items(self):
        return self.data.items()
    
    def history(self, key):
        if self.memo_dict.get(key) == None:
            return []
        return self.memo_dict[key]   
    
    def all_history(self):
        return self.memo_dict
    
historydict = HistoryDict({'ducks': 99, 'cats': 1})
print(historydict['ducks'])
print(historydict['cats'])
print(len(historydict))    

historydict = HistoryDict({'ducks': 99, 'cats': 1})
print(*historydict)
print(*historydict.keys())
print(*historydict.values())
print(*historydict.items())

historydict = HistoryDict({'ducks': 99, 'cats': 1})
historydict['ducks'] = 100
print(historydict.history('ducks'))
print(historydict.history('cats'))
print(historydict.history('dogs'))

historydict = HistoryDict({'ducks': 99, 'cats': 1})
print(historydict.all_history())
historydict['ducks'] = 100
historydict['ducks'] = 101
historydict['cats'] = 2
print(historydict.all_history())

historydict = HistoryDict({'ducks': 99, 'cats': 1})
historydict['dogs'] = 1
print(len(historydict))
del historydict['ducks']
del historydict['cats']
print(len(historydict))
"""


#
"""
class MutableString:

    def __init__(self, string = ''):
        self.string = string
        
    def __repr__(self):
        return f"{__class__.__name__}('{self.string}')"
    
    def __str__(self):
        return self.string
    
    def __len__(self):
        return len(self.string)
    
    def lower(self):
        self.string = self.string.lower()
        return self.string
    
    def upper(self):
        self.string = self.string.upper()
        return self.string
    
    def __iter__(self):
        return iter(self.string)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return MutableString(self.string[index])
        return self.string[index]
    
    def __setitem__(self, index, value):
        self.string = [el for el in self.string]
        self.string[index] = value
        self.string = ''.join(self.string)
    
    def __delitem__(self, index):
        self.string = [el for el in self.string]
        del self.string[index]
        self.string = ''.join(self.string)
        
    def __add__(self, other):
        if isinstance(other, MutableString):
            return self.string + other.string

            
mutablestring = MutableString('beegeek')
print(*mutablestring)
print(str(mutablestring))
print(repr(mutablestring))            

mutablestring = MutableString('Beegeek')
mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
            
mutablestring1 = MutableString('bee')
mutablestring2 = MutableString('geek')
print(mutablestring1 + mutablestring2)
print(mutablestring2 + mutablestring1)

mutablestring = MutableString('beegeek')
print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)
"""


#
"""
class Grouper:

    def __init__(self, iterable, key):
        self.key = key
        self.iterable = iterable.copy()
        self.res_dict = dict()
        for el in self.iterable:
            self.add(el)    
            
    def __iter__(self):
        yield from self.res_dict.items()
    
    def __getitem__(self, index):
        return self.res_dict.get(index)
    
    def __contains__(self, item):
        return item in self.res_dict.keys()
    
    def group_for(self, iterable):
        return self.key(iterable)
    
    def add(self, iterable):
        group = self.group_for(iterable)
        value = self.res_dict.get(group)
        if value: 
            self.res_dict.setdefault(group, value.append(iterable))
        else:
            self.res_dict.setdefault(group, [iterable])

grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)
print(grouper[2])
print(grouper[3])
print(grouper[4])          

grouper = Grouper(['hi'], key=lambda s: s[0])
grouper.add('hello')
grouper.add('bee')
grouper.add('big')
grouper.add('geek')
print(grouper['h'])
print(grouper['b'])
print(grouper['g'])

grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)
print(3 in grouper)
print('bee' in grouper)

from collections import namedtuple
Person = namedtuple('Person', ['name', 'age', 'height'])
persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

grouper = Grouper(persons, key=lambda x: x.height)
print(sorted(grouper))
"""


#
"""
import sys

class UpperPrint:

    def __enter__(self):
        self.standart_stdout = sys.stdout.write
        sys.stdout.write = self.temp_func
    
    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.standart_stdout
        
    def temp_func(self, data):
        self.standart_stdout(data.upper()) 

        
print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')
with UpperPrint():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')
print('Требуйте встречи с менеджером, отвечающим за жизнь!')        
"""


#
"""
class WriteSpy:

    def __init__(self, file1, file2, to_close = False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close      
    
    def __enter__(self):
        return self 
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.to_close:
            self.file1.close()
            self.file2.close()    
            
    def write(self, text):
        if self.writable():
            self.file1.write(text)
            self.file2.write(text)
        else:
            raise ValueError ('Файл закрыт или недоступен для записи')         
                 
    def close(self):
        self.file1.close()
        self.file2.close()
        
    def writable(self):
        if not self.file1.closed and not self.file2.closed:
            if self.file1.writable() and self.file2.writable():
                return True
        return False
    
    def closed(self):
        if self.file1.closed and self.file2.closed:
            return True
        return False        
    
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
with WriteSpy(f1, f2, to_close=True) as combined:
    combined.write('You shall seal the blinding light that plagues their dreams\n')
    combined.write('You are the Vessel\n')
    combined.write('You are the Hollow Knight')
print(f1.closed, f2.closed)
with open('file1.txt') as file1, open('file2.txt') as file2:
    print(file1.read())
    print(file2.read())    

f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.closed())
    f1.close()
    print(combined.closed())
    f2.close()
    print(combined.closed())    
"""


#
"""
from copy import deepcopy

class Atomic:

    def __init__(self, data, deep = False):
        self.data = data 
        if deep:    
            self.backup = deepcopy(data)  
        else:
            self.backup = data.copy()
        
    def __enter__(self):
        return self.data
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.data.clear()
            if isinstance(self.data, list):
                self.data.extend(self.backup) 
            if isinstance(self.data, (set, dict)):
                self.data.update(self.backup)
        return True

matrix = [[1, 2], [3, 4]]
with Atomic(matrix) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу
print(matrix)        

matrix = [[1, 2], [3, 4]]
with Atomic(matrix, True) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу
print(matrix)

data = {'firstname': 'Alyson', 'lastname': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}
with Atomic(data, True) as atomic:          # deep = True
    atomic['birthday']['month'] = 'April'   # изменение вложенной структуры
    print(atomic['name'])                   # обращение по несуществующему ключу
print(data)
with Atomic(data) as atomic:                # deep = False
    atomic['birthday']['month'] = 'April'   # изменение вложенной структуры
    print(atomic['name'])                   # обращение по несуществующему ключу
print(data)
"""


# Timer
"""
import time

class AdvancedTimer:

    def __init__(self):
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None
        
    def __enter__(self):
        self.last_run = time.perf_counter()
        return self
    
    def __exit__(self, *args, **kwargs):
        stop = time.perf_counter()
        self.last_run = stop - self.last_run
        self.runs.append(self.last_run)
        self.min = min(self.runs)
        self.max = max(self.runs)

from time import sleep
timer = AdvancedTimer()
with timer:
    sleep(1.5)
with timer:
    sleep(0.7)
with timer:
    sleep(1)
print([round(runtime, 1) for runtime in timer.runs])
print(round(timer.min, 1))
print(round(timer.max, 1))        
"""


# HTMLTags
"""
class HtmlTag:

    step = 0
    temp = False

    def __init__(self, tag, inline = False):
        self.tag = tag
        self.inline = inline
                         
    def __enter__(self):
        if HtmlTag.temp: 
            HtmlTag.step += 1   
        HtmlTag.temp = True    
        if not self.inline:
            print(f"{'  ' * (HtmlTag.step)}<{self.tag}>")
        return self
        
    def __exit__(self, exc_type, ec_value, traceback):
        HtmlTag.step -= 1
        HtmlTag.temp = False
        if not self.inline:
            print(f"{'  ' * (HtmlTag.step)}</{self.tag}>")       
        
    def print(self, text):
        if HtmlTag.temp: 
            HtmlTag.step += 1
        if self.inline:
            print(f'{"  " * (HtmlTag.step-1)}<{self.tag}>{text}</{self.tag}>')
        else:    
            print('  ' * (HtmlTag.step) + text)

with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Поколение Python')
    with HtmlTag('p', True) as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')
"""  


######################################################## contextmanager ########################################################

# защита файлов от внесения информации с ошибками
"""
from contextlib import contextmanager

@contextmanager
def safe_write(file):
    backup = open('backup.txt', 'w', encoding = 'utf-8')
    try:
        yield backup
    except Exception as error:
        print('Во время записи в файл было возбуждено исключение', type(error).__name__)
    else:
        backup.close()
        backup = open('backup.txt', 'r', encoding = 'utf-8')
        file_input = open(file, 'w', encoding = 'utf-8')
        file_input.write(backup.read().strip())
        file_input.close()
    finally:
        backup.close()

with safe_write('undertale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')   
with safe_write('undertale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
    raise ValueError
with open('undertale.txt') as file:
    print(file.read())        
    
with safe_write('poem.txt') as file:
    print('''Я кашлянул в звенящей тишине,
            И от шального эха стало жутко…, 
            Расскажет ли утятам обо мне,
            под утро мной испуганная утка?''', file=file)
with safe_write('poem.txt') as file:
    file.insert('Стихотворение про утку')       # неверный метод для записи в файл
with open('poem.txt') as file:
    print(file.read())    
"""   


# контроль открываемого файла
"""
from contextlib import contextmanager

@contextmanager
def safe_open(filename, mode = 'r'):
    try:
        file = open(filename, mode)
        
    except Exception as err:
        yield (None, err)
    else:
        yield (file, None)
        file.close()

with open('Ellies_jokes.txt', 'w') as file:
    file.write('Знаешь, кто не прав? Лев\n')
    file.write('Что треугольник сказал кругу? Катись отсюда')   
with safe_open('Ellies_jokes.txt') as file:
    file, error = file
    print(error)
    print(file.read())

with safe_open('Ellies_jokes_2.txt') as file:
    file, error = file
    print(file)
    print(error)
"""    


######################################################## Дискрипторы ########################################################

#
"""
class NonNegativeInteger:

    def __init__(self, name, default = None):
        self.name = name
        self.default = default
        
    def __get__(self, obj, cls):
        if self.name in obj.__dict__:
            return obj.__dict__[self.name]
        else:
            if self.default != None:
                return self.default
            raise AttributeError('Атрибут не найден')    
     
    def __set__(self, obj, value):
        if isinstance(value, int):
            if value >= 0: 
                obj.__dict__[self.name] = value
            else: 
                raise ValueError('Некорректное значение')    
        else:
            raise ValueError('Некорректное значение')
        
class Student:
    score = NonNegativeInteger('score')
student = Student()
student.score = 90
print(student.score) 

class Student:
    score = NonNegativeInteger('score', 0)
student = Student()
print(student.score)
student.score = 0
print(student.score)
"""


#
"""
class MaxCallsException(Exception):
    pass

class LimitedTakes:
    # закрепляем дескриптор за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор
    def __set_name__(self, cls, attr): 
        self._attr = attr
        
    def __init__(self, times):
        self.times = times
        
    def __get__(self, obj, cls):
        if self.times > 0:
            if self._attr in obj.__dict__:
                self.times -= 1
                return obj.__dict__[self._attr]
            else:
                raise AttributeError('Атрибут не найден')      
        else:
            raise MaxCallsException('Превышено количество доступных обращений')
    
    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value

class Student:
    name = LimitedTakes(3)
student = Student()
student.name = 'Gwen'
print(student.name)
print(student.name)
print(student.name)
try:
    print(student.name)
except MaxCallsException as e:
    print(e)    
"""


#
"""
import random

class RandomNumber:
    
    def __set_name__(self, cls, attr):
        self._attr = attr
    
    def __init__(self, start, end, cache = False):
        self.start = start
        self.end = end
        self.cache = cache
        self.memo = None
        
    def __get__(self, obj, cls):
        if not self.cache:
            return random.randrange(self.start, self.end)
        else:
            if self.memo == None:
                self.memo = random.randrange(self.start, self.end)
            return self.memo    
        
    def __set__(self, obj, value):
        raise AttributeError('Изменение невозможно')
    
class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)
magicpoint = MagicPoint()
print(magicpoint.x in [1, 2, 3, 4, 5])
print(magicpoint.y in [1, 2, 3, 4, 5])
print(magicpoint.z in [1, 2, 3, 4, 5])  

class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)
magicpoint = MagicPoint()
print(magicpoint.x in [6, 7, 8, 9, 10])
print(magicpoint.y in [6, 7, 8, 9, 10])
print(magicpoint.z in [6, 7, 8, 9, 10])

class MagicPoint:
    x = RandomNumber(0, 5)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)
magicpoint = MagicPoint()
try:
    magicpoint.x = 10
except AttributeError as e:
    print(e)
""" 


#
"""
class Versioned:

    def __set_name__(self, obj, attr):
        self._attr = attr
        
    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return Versioned.get_version(self, obj)
        raise AttributeError('Атрибут не найден')
    
    def __set__(self, obj, value):
        try:
            getattr(obj, self._attr)
        except:
            obj.__dict__[self._attr] = [value]
        else:
            obj.__dict__[self._attr].append(value)

    def get_version(self, obj, n=0):
        return obj.__dict__[self._attr][n-1]
    
    def set_version(self, obj, n):
        obj.__dict__[self._attr][-1] = Versioned.get_version(self, obj, n)

class Student:
    age = Versioned()
student = Student()
student.age = 18
student.age = 19
student.age = 20
print(student.age)
print(Student.age.get_version(student, 1))
print(Student.age.get_version(student, 2))
print(Student.age.get_version(student, 3))        

class Student:
    name = Versioned()
student = Student()
try:
    print(student.name)
except AttributeError as e:
    print(e)
"""


######################################################## Наследование ########################################################

#
"""
class FieldTracker:

    changed_dict = {}
    
    def __getattribute__(self, attr):
        res = object.__getattribute__(self, attr)
        if type(res) == list:
            return res[-1]
        return res
    
    def __setattr__(self, attr, value):
        if attr in self.__dict__.keys():
            if self.__dict__[attr][-1] != value:
                self.__dict__[attr].append(value)
                if len(self.__dict__[attr]) == 2:
                    FieldTracker.changed_dict.setdefault(attr, self.__dict__[attr][0])
        else:
            self.__dict__[attr] = [value]      
    
    def base(self, attr):
        return self.__dict__[attr][0]
    
    def has_changed(self, attr):
        return len(self.__dict__[attr])>1
    
    def changed(self):
        return FieldTracker.changed_dict
    
    def save(self):
        for key in FieldTracker.changed_dict.keys():
            self.__dict__[key] = [self.__dict__[key][-1]]  
        FieldTracker.changed_dict = {}

class Point(FieldTracker):
    fields = ('x', 'y', 'z')
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()
point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.save()
print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())
"""


######################################################## переопределение __new__ и наследование базовых классов типов данных
"""
class LowerString(str):

    def __new__(cls, obj = ''):
        if isinstance(obj, str):
            obj = obj.lower()
        if isinstance(obj, list):
            obj = list(map(lambda x: x.lower(),obj))
        if isinstance(obj, dict):
            obj = {key.lower(): obj.get(key) for key in obj.keys()}    
            
        instance = super().__new__(cls, obj)
        return instance

s1 = LowerString('BEEGEEK')
s2 = LowerString('BeeGeek')
print(s1)
print(s2)
print(s1 == s2)
print(issubclass(LowerString, str))    

print(LowerString(['Bee', 'Geek']))
print(LowerString({'A': 1, 'B': 2, 'C': 3}))
"""


# сравнение без учета регистра
"""
class FuzzyString(str):

    def __new__(cls, obj):
        obj = obj.lower()
        return super().__new__(cls, obj)
           
    def __eq__(self, other):
        if isinstance(other, FuzzyString):
            return self.__str__() == other.__str__()
        if isinstance(other, str):
            return self.__str__() == other.lower()
        return NotImplemented
        
    def __ne__(self, other):
        if isinstance(other, FuzzyString):
            return self.__str__() != other.__str__()
        if isinstance(other, str):
            return self.__str__() != other.lower()
        return NotImplemented
  
    def __lt__(self, other):
        if isinstance(other, FuzzyString):
            return self.__str__() < other.__str__()
        if isinstance(other, str):
            return self.__str__() < other.lower()
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, FuzzyString):
            return self.__str__() > other.__str__()
        if isinstance(other, str):
            return self.__str__() > other.lower()
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, FuzzyString):
            return self.__str__() <= other.__str__()
        if isinstance(other, str):
            return self.__str__() <= other.lower()
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, FuzzyString):
            return self.__str__() >= other.__str__()
        if isinstance(other, str):
            return self.__str__() >= other.lower()
        return NotImplemented
    
    def __contains(self, other):
        if isinstance(other, FuzzyString):
            return other.__str__() in self.__str__()
        if isinstance(other, str):
            return other.lower() in self.__str__()  
        return NotImplemented
    
s1 = FuzzyString('BeeGeek')
s2 = FuzzyString('beegeek')
print(s1 == s2)
print(s1 in s2)
print(s2 in s1)
print(s2 not in s1)
print(s2 not in s1)    

s = FuzzyString('BeeGeek')
print(s != 'BEEGEEK')
print(s == 'BEEGEEK')
print(s != 'beegeek')
print(s == 'beegeek')
print(s >= 'BEEGEEK')
print(s <= 'BEEGEEK')
print(s > 'BEEGEEK')
print(s < 'BEEGEEK')
"""


#
"""
class SuperInt(int):

    def __init__(self, digit):
        self.digit = digit  
        self.index = -1    

    def repeat(self, n=2):
        int_digit = super().__int__()
        if int_digit < 0:
            self.__init__(int(f'-{str(abs(int_digit))*n}'))
        else:
            self.__init__(int(str(int_digit)*n))
        return SuperInt(self.digit)
    
    def to_bin(self):
        return format(super().__int__(), 'b')

    def next(self):
        return SuperInt(super().__int__()+1)

    def prev(self):
        return SuperInt(super().__int__()-1)
    
    def __next__(self):
        temp_list = [int(el) for el in str(super().__int__()) if el.isdigit()]
        self.index += 1
        try:
            return SuperInt(temp_list[self.index])
        except:
            raise StopIteration        
         
    def __iter__(self):
        return self

superint1 = SuperInt(17)
superint2 = SuperInt(-17)
print(superint1.repeat())
print(superint2.repeat(3)) 

superint1 = SuperInt(1337)
superint2 = SuperInt(-2077)
print(*superint1)
print(*superint2)    

superint1 = SuperInt(2023)
for item in superint1:
    print(item, type(item))

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
superint = SuperInt(30)
for n in digits:
    print(superint.repeat(n))    
"""


#
"""
class AdvancedTuple(tuple):
    
    def __init__(self, data):
        self.data = data
    
    def __add__(self, other):
        return AdvancedTuple(self.data + list(AdvancedTuple.check(self, other)))
        
    def __iadd__(self, other):    
       self.data = list(AdvancedTuple.check(self, other))
       self = AdvancedTuple(list(self)+self.data)
       return self
    
    def __radd__(self, other):
        return AdvancedTuple(list(AdvancedTuple.check(self, other)) + self.data)
    
    def check(self, other):
        if not isinstance(other, (list, tuple)):
            if '__iter__' in other.__dir__():
                other = [el for el in other]
            else:
                other = [el for el in other.keys()]
        return other  

advancedtuple = AdvancedTuple([1, 2, 3])
print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({'a': 1, 'b': 2} + advancedtuple)

advancedtuple = AdvancedTuple([1, 2, 3])
advancedtuple += [4, 5]
advancedtuple += iter([6, 7, 8])
print(advancedtuple)
print(type(advancedtuple))    
"""


######################################################## Абстрактные классы ########################################################
"""
#
from abc import ABC, abstractmethod

class Middle(ABC):

    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes                   # пользовательские оценки
        self.expert_votes = expert_votes               # оценки критиков
    
    @abstractmethod
    def get_correct_user_votes(self):
        #Возвращает нормализованный список пользовательских оценок
        #без слишком низких и слишком высоких значений
        return [vote for vote in self.user_votes if 10 < vote < 90]

    @abstractmethod
    def get_correct_expert_votes(self):
        #Возвращает нормализованный список оценок критиков
        #без слишком низких и слишком высоких значений
        return [vote for vote in self.expert_votes if 5 < vote < 95]

    @abstractmethod
    def get_average(self, users):
        if users:
            votes = self.get_correct_user_votes()
        else:
            votes = self.get_correct_expert_votes()
        return votes    


class Average(Middle):
    def __init__(self, user_votes, expert_votes):
        super().__init__(user_votes, expert_votes)

    def get_correct_user_votes(self):
        return super().get_correct_user_votes()

    def get_correct_expert_votes(self):
        return super().get_correct_expert_votes()

    def get_average(self, users=True):
        #Возвращает среднее арифметическое пользовательских оценок или
        #оценок критиков в зависимости от значения параметра users
        votes = super().get_average(users)
        return sum(votes) / len(votes)

class Median(Middle):
    def __init__(self, user_votes, expert_votes):
        super().__init__(user_votes, expert_votes)

    def get_correct_user_votes(self):
        return super().get_correct_user_votes()

    def get_correct_expert_votes(self):
        return super().get_correct_expert_votes()

    def get_average(self, users=True):
        #Возвращает медиану пользовательских оценок или
        #оценок критиков в зависимости от значения параметра users
        if users:
            votes = sorted(self.get_correct_user_votes())
        else:
            votes = sorted(self.get_correct_expert_votes())
        return votes[len(votes) // 2]

class Harmonic(Middle):
    def __init__(self, user_votes, expert_votes):
        super().__init__(user_votes, expert_votes)

    def get_correct_user_votes(self):
        return super().get_correct_user_votes()

    def get_correct_expert_votes(self):
        return super().get_correct_expert_votes()

    def get_average(self, users=True):
        #Возвращает среднее гармоническое пользовательских оценок или
        #оценок критиков в зависимости от значения параметра users
        votes = super().get_average(users)
        return len(votes) / sum(map(lambda vote: 1 / vote, votes))
    

user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
average = Average(user_votes, expert_votes)
print(average.get_correct_user_votes())
print(average.get_correct_expert_votes())
print(average.get_average())
print(average.get_average(False))   

user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
median = Median(user_votes, expert_votes)
print(median.get_correct_user_votes())
print(median.get_correct_expert_votes())
print(median.get_average())
print(median.get_average(False))

user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
harmonic = Harmonic(user_votes, expert_votes)
print(harmonic.get_correct_user_votes())
print(harmonic.get_correct_expert_votes())
print(round(harmonic.get_average(), 2))
print(round(harmonic.get_average(False), 2))
"""


######################################################## Полиморфизм ########################################################
#
""""
from abc import ABC, abstractmethod

class StringCreator(ABC):

    def __init__(self, length):
        self.length = length
        self.res_list = []
        self.temp_str = ''

    def add(self, words):
        for el in words.split(' '):
            if len(self.temp_str) + len(el) <= self.length:
                self.temp_str += (el + ' ')
            else:
                self.res_list.append(self.temp_str.strip())
                self.temp_str = ''   
                self.temp_str += (el + ' ')

    @abstractmethod
    def end(self):
        pass

class LeftParagraph(StringCreator):
    def end(self):
        self.res_list.append(self.temp_str.strip())
        for string in self.res_list:
            print(string)
        self.res_list = []  
        self.temp_str = ''  

class RightParagraph(StringCreator):
    def end(self):
        self.res_list.append(self.temp_str.strip())
        for string in self.res_list:
            print(string.rjust(self.length, " "))
        self.res_list = []  
        self.temp_str = ''  

leftparagraph = LeftParagraph(10)
leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()            
print()
rightparagraph = RightParagraph(10)
rightparagraph.add('death')
rightparagraph.add('can have me')
rightparagraph.add('when it earns me')
rightparagraph.end()
print()
leftparagraph = LeftParagraph(23)
leftparagraph.add('Multiply noise and joy')
leftparagraph.add('Sing songs in a good hour')
leftparagraph.add('Friendship grace and youth')
leftparagraph.add('Our birthday girls')
leftparagraph.end()
leftparagraph.add('Meanwhile the winged child')
leftparagraph.add('friends greeting you')
leftparagraph.add('Secretly thinks sometime')
leftparagraph.add('I will be the birthday boy')
leftparagraph.end()
print()
rightparagraph = RightParagraph(28)
rightparagraph.add('I will not regret the roses')
rightparagraph.add('Withered with a light spring')
rightparagraph.add('I love the grapes on the vines')
rightparagraph.add('Ripened in the hands under the mountain')
rightparagraph.end()
rightparagraph.add('The beauty of my green valley')
rightparagraph.add('Golden joy of autumn')
rightparagraph.add('oblong and transparent')
rightparagraph.add('Like the fingers of a young maiden')
rightparagraph.end()
"""


######################################################## Композиция ########################################################

# Колода карт (через product)
"""
from itertools import product
from random import shuffle

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f'{self.suit}{self.rank}'

        
class Deck:

    suits = ['♣', '♢', '♡', '♠']
    ranks = [str(rank) for rank in range(2, 11)] + ['J', 'Q', 'K', 'A']

    def __init__(self):
        self.deck = list(product(self.suits, self.ranks))
        
    def shuffle(self):
        if len(self.deck) == 52:
            shuffle(self.deck)
            return self.deck
        else:
            raise ValueError('Перемешивать можно только полную колоду')
    
    def deal(self):
        try:
            card = self.deck.pop()
            return f'{card[0]+card[1]}'
        except IndexError:
            raise ValueError('Все карты разыграны')

    def __str__(self):
        return f'Карт в колоде: {len(self.deck)}'
""" 


# Колода карт (через композицию)
"""
from random import shuffle

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f'{self.suit}{self.rank}'

        
class Deck:
    
    def __init__(self):
        self.suits = ['♣', '♢', '♡', '♠']
        self.ranks = [str(rank) for rank in range(2, 11)] + ['J', 'Q', 'K', 'A']
        self.deck = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        if len(self.deck) == 52:
            shuffle(self.deck)
            return self.deck
        else:
            raise ValueError('Перемешивать можно только полную колоду')
    
    def deal(self):
        try:
            card = self.deck.pop()
            return f'{card.suit + card.rank}'
        except IndexError:
            raise ValueError('Все карты разыграны')

    def __str__(self):
        return f'Карт в колоде: {len(self.deck)}'

deck = Deck()
print(deck)
print(deck.deal())
print(deck.deal())
print(deck.deal())
print(deck)
"""


# OrderedDict через композицию
"""
class View:

    def __init__(self, element):
        self.element = element  
        self.key, self.value = self.element

        
class Queue:

    def __init__(self, pairs = []):
        if isinstance(pairs, dict):
            self.pairs = [View(item) for item in pairs.items()]
        if isinstance(pairs, list):
            self.pairs = [View(item) for item in pairs]
        
    def add(self, pair):
        try:
            index = [pair.key for pair in self.pairs].index(View(pair).key)
            self.pairs.pop(index).element
        except ValueError:
            pass
        finally:    
            self.pairs.append(View(pair))    
    
    def pop(self):
        try:
            deleted_element = self.pairs.pop(0)
            return (deleted_element.key, deleted_element.value)
        except IndexError:
            raise KeyError('Очередь пуста')
            
    def __repr__(self):
        res_str = ''
        for item in self.pairs:
            res_str += f'{item.element}, '
        res_str = res_str.strip(', ')        
        return f'{type(self).__name__}([{res_str}])'
    
    def __len__(self):
        return len(self.pairs)
    
queue = Queue([('one', 1)])
queue.add(('two', 2))
print(queue.pop())
print(queue.pop())
print(queue)
"""


#
"""
from datetime import datetime

def hours_to_minutes(hours):
    return hours.hour * 60 + hours.minute

def minutes_to_hours(minutes):
    hours = minutes // 60
    minutes = minutes - (hours*60)
    return datetime(year = 1900, month = 1, day = 1, hour = hours, minute = minutes).strftime('%H:%M')

    
class Lecture:

    def __init__(self, topic, start_time, duration):
        self.topic = topic 
        self.start_time = datetime.strptime(start_time, '%H:%M')
        self.duration = datetime.strptime(duration, '%H:%M')
        self.end_time = hours_to_minutes(self.start_time) + hours_to_minutes(self.duration)
        

class Conference:

    def __init__(self, schedule = [], pause = []):
        self.schedule = schedule
        self.pause = pause
        
    def add(self, lecture):
        if self.schedule:
            for el in self.schedule:
                if (
                    (hours_to_minutes(el.start_time) <= hours_to_minutes(lecture.start_time) < el.end_time or hours_to_minutes(el.start_time) < lecture.end_time <= el.end_time)
                    or
                    (hours_to_minutes(lecture.start_time) <= hours_to_minutes(el.start_time) < lecture.end_time or hours_to_minutes(lecture.start_time) < el.end_time <= lecture.end_time)
                ):
                    raise ValueError('Провести выступление в это время невозможно')
        self.schedule.append(lecture)
        self.schedule = sorted(self.schedule, key = lambda x: x.start_time)
    
    def total(self):
        total_lecture_time = sum([hours_to_minutes(lecture.duration) for lecture in self.schedule])
        return minutes_to_hours(total_lecture_time)
    
    def longest_lecture(self):
        longest_lecture_time = max([hours_to_minutes(lecture.duration) for lecture in self.schedule])
        return minutes_to_hours(longest_lecture_time)
    
    def longest_break(self):
        try:
            self.pause = [(hours_to_minutes(self.schedule[i].start_time) 
                           - self.schedule[i-1].end_time) for i in range(1, len(self.schedule))]
            longest_break_time = max(self.pause)
            return minutes_to_hours(longest_break_time)
        except (IndexError, ValueError):
            return '00:00'
        
conference = Conference()

conference.add(Lecture('Простые числа', '08:00', '01:30'))
conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))
conference.add(Lecture('Муравьиный алгоритм', '13:30', '01:50'))
print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())        
"""


######################################################## __slots__ ########################################################

#
"""
from functools import total_ordering

@total_ordering
class Shape:

    __slots__ = ('name', 'color', 'area')
    
    def __init__(self, name, color, area):
        self.name, self.color, self.area = name, color, area
        
    def __repr__(self):
        return f'{self.color} {self.name} ({self.area})'
    
    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.area == other.area
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Shape):
            return self.area < other.area
        return NotImplemented
    
shape = Shape('triangle', 'red', 12)

print(shape.name)
print(shape.color)
print(shape.area)
"""

### Enum (не решена!!!)
"""
from datetime import timedelta, date
from enum import Enum

Weekday = Enum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start = 0)
    
class NextDate:

    def __init__(self, today, weekday, after_today = False):
        self.today, self.weekday, self.after_today = today, weekday, after_today
        self.weekday_today = self.today.weekday() + 1
        
    def date(self):
        delta = timedelta(days = 1)
        "метод, возвращающий дату следующего дня недели в виде экземпляра класса date"
        self.today = self.today + delta * type(self).days_until(self)
        return self.today 
    
    def days_until(self):
        "метод, возвращающий количество дней до даты следующего дня недели"
        if not self.after_today:
            return (self.weekday.value + self.weekday_today)-7*((self.weekday.value + self.weekday_today)//8)
        return (self.weekday.value + self.weekday_today)-7*((self.weekday.value + self.weekday_today)//7)

from datetime import date
today = date(2023, 4, 17)                                   # понедельник
next_friday = NextDate(today, Weekday.FRIDAY)               # следующая пятница
print(next_friday.date())
print(next_friday.days_until())   

from datetime import date
today = date(2023, 4, 17)                                   # понедельник
next_monday = NextDate(today, Weekday.MONDAY)               # следующий понедельник без учета текущего
print(next_monday.date())
print(next_monday.days_until())

from datetime import date
today = date(2023, 4, 17)                                   # понедельник
next_monday = NextDate(today, Weekday.MONDAY, True)         # следующий понедельник с учетом текущего
print(next_monday.date())
print(next_monday.days_until())

from datetime import date
for weekday in Weekday:
    today = date(2023, 4, 27)                               # четверг
    next_date = NextDate(today, weekday)
    print(next_date.date())
    print(next_date.days_until())
"""


######################################################## Декораторы в виде класса ########################################################

#
"""
import functools

class reverse_args:

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        
    def __call__(self, *args, **kwargs):
        args = reversed(args)
        return self.func(*args, **kwargs)

@reverse_args
def concat(a, b, c):
    return a + b + c
    
print(concat('apple', 'cherry', 'melon'))
""" 


#
"""
import functools

class MaxCallsException(Exception):
    pass

    
class limited_calls:

    def __init__(self, n):
        self.n = n
        self.i = 0
        
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.i < self.n:
                res = func(*args, **kwargs)
                self.i+=1
                return res   
            else:
                raise MaxCallsException('Превышено допустимое количество вызовов')
        return wrapper
    
@limited_calls(3)
def add(a, b):
    return a + b
print(add(1, 2))
print(add(3, 4))
print(add(5, 6))
try:
    print(add())
except MaxCallsException as e:
    print(e)    
"""


#
"""
import functools

class takes_numbers:

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        
    def __call__(self, *args, **kwargs):
        if all([isinstance(arg, (int, float)) for arg in args]) and all([isinstance(arg, (int, float)) for arg in kwargs.values()]):
            res = self.func(*args, **kwargs)
            return res
        raise TypeError('Аргументы должны принадлежать типам int или float')
    
@takes_numbers
def mul(a, b):
    return a * b
    
try:
    print(mul(1, '2'))
except TypeError as error:
    print(error)
"""    


#
"""
import functools

class returns:

    def __init__(self, datatype):
        self.datatype = datatype
        
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if not isinstance(res,self.datatype):
                return TypeError
            return res
        return wrapper

@returns(int)
def add(a, b):
    return a + b
try:
    print(add('1', '2'))
except Exception as error:
    print(type(error))
"""


#
"""
import functools

class exception_decorator:

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        
    def __call__(self, *args, **kwargs):
        try:
            res = self.func(*args, **kwargs)
        except Exception as err:
            return (None, type(err))
        else:
            return (res, None)
        
@exception_decorator
def func(x):
    return 2*x + 1
print(func(1))
print(func('bee')) 
"""

#
"""
import functools

class ignore_exception:

    def __init__(self, *errors):
        self.errors = errors
        
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwrags):
            try:
                res = func(*args, **kwrags)
            except Exception as error:
                if type(error) in self.errors:
                    print(f'Исключение {type(error).__name__} обработано')
                    return True
                raise error
            else:
                return res
        return wrapper

@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def func(x):
    return 1 / x
func(0)

min = ignore_exception(ZeroDivisionError)(min)
try:
    print(min(1, '2', 3, [4, 5]))
except Exception as error:
    print(type(error))    
"""    


#
"""
import functools

class type_check:

    def __init__(self, types):
        self.types = types
        
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if all([True if self.types[i] == type(args[i]) else False for i in range(min(len(self.types), len(args)))]):
                res = func(*args, **kwargs)
                return res
            raise TypeError
        return wrapper

@type_check([int, int])
def add(a, b):
    return a + b
print(add(1, 2))

@type_check([int, int])
def add(a, b):
    return a + b
try:
    print(add(1, '2'))
except Exception as error:
    print(type(error))        
"""    


#
"""
import functools
from re import fullmatch, split

def snake_case(attrs = False):
    def wrapper(cls):
        old_init = cls.__init__
        
        for old_name in dir(cls):
            if fullmatch(r'__\w+__', old_name) == None:
                backup = cls.__dict__[old_name] 
                if isinstance(backup, (int, float, str)):
                    if attrs:
                        new_name = transformation(old_name)     
                        setattr(cls, new_name, backup)
                        delattr(cls, old_name)
     
        @functools.wraps(old_init)
        def new_init(self, *args, **kwargs):
            old_init(self, *args, **kwargs)
            for old_name in dir(cls):
                if fullmatch(r'__\w+__', old_name) == None:
                    backup = cls.__dict__[old_name]
                    if isinstance(backup, (int, float, str)):
                        if attrs:
                            new_name = transformation(old_name)     
                            setattr(cls, new_name, backup)
                            delattr(cls, old_name)
                    else:
                        new_name = transformation(backup.__name__)
                        setattr(cls, new_name, backup)
                        delattr(cls, old_name)               
        cls.__init__ = new_init
        return cls
    return wrapper

def transformation(string):
    if string[0] != '_':       
        temp_list = list(filter(lambda x: len(x)>0, split(r'(^[a-z]{1}[a-z]*[^A-Z]|[A-Z]{1}[a-z]*[^A-Z])', string)))
        res_string = '_'.join(temp_list).lower()
    else:
        string = string[1::]
        temp_list = list(filter(lambda x: len(x)>0, split(r'(^[a-z]{1}[a-z]*[^A-Z]|[A-Z]{1}[a-z]*[^A-Z])', string)))
        res_string = '_'.join(temp_list).lower()
        res_string = '_'+res_string
    return res_string

@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1
    
    def superSecondMethod(self):
        return 2
obj = MyClass()
print(obj.first_method())
print(obj.super_second_method())

@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2
print(MyClass.first_attr)
print(MyClass.super_second_attr)
"""


# декоратор для __repr__
"""
def auto_repr(args, kwargs):
    def wrapper(cls):
        def new_repr(self):
            attr_list = []
            for arg in args:
                if arg in self.__dict__:
                    attr_list.append(repr(self.__dict__[arg]))
            for kwarg in kwargs:
                if kwarg in self.__dict__:
                    attr_list.append('='.join([kwarg, repr(self.__dict__[kwarg])]))               
            return f'{type(self).__name__}({", ".join(attr_list)})'         
        cls.__repr__ = new_repr
        return cls
    return wrapper

@auto_repr(args=['x', 'y'], kwargs=['color'])
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

point = Point(1, 2, color='green')
print(point)
point.x = 10
point.y = 20
print(point)

@auto_repr(args=['name', 'surname'], kwargs=[])
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
person = Person('Gvido', 'van Rossum')
print(person)
"""


# декоратор для ограничения количества новых экземпляров класса
"""
def limiter(limit, unique, lookup):
    def decorator(cls):
        cls.instance_list = []
        cls._instance = None
        cls.ID_list = []
        def wraper(*args, **kwargs):
            cls._instance = cls(*args, **kwargs)
            if len(cls.instance_list)<limit:
                cls.ID_list.append(getattr(cls._instance, unique))    
                cls.instance_list.append(cls._instance)
            else:
                if getattr(cls._instance, unique) in cls.ID_list:
                    cls._instance = cls.instance_list[cls.ID_list.index(getattr(cls._instance, unique))]
                else:    
                    if lookup == 'FIRST':
                        cls._instance = cls.instance_list[0] 
                    else:
                        cls._instance = cls.instance_list[-1]
            return cls._instance  
        return wraper
    return decorator

@limiter(2, 'ID', 'FIRST')
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value

obj1 = MyClass(1, 5)          # создается экземпляр класса с идентификатором 1
obj2 = MyClass(2, 8)          # создается экземпляр класса с идентификатором 2
obj3 = MyClass(1, 20)         # возвращается obj1, так как экземпляр с идентификатором 1 уже есть
obj4 = MyClass(3, 0)          # превышено ограничение limit, возвращается первый созданный экземпляр

print(obj3.value)
print(obj4.value)
"""


######################################################## dataclasses ########################################################
"""
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(init = False)    
        
    def __post_init__(self):
        if self.x == 0 or self.y == 0:
            self.quadrant = 0
        elif self.x > 0 and self.y > 0:  
            self.quadrant = 1
        elif self.x < 0 and self.y > 0:  
            self.quadrant = 2 
        elif self.x < 0 and self.y < 0:  
            self.quadrant = 3
        else:
            self.quadrant = 4
            
    def symmetric_x(self):
        return type(self)(self.x, -self.y)
    
    def symmetric_y(self):
        return type(self)(-self.x, self.y) 
    
point = Point()

print(point)
print(point.x)
print(point.y)
print(point.quadrant)

point = Point(1.0, 2.0)

print(point.symmetric_x())
print(point.symmetric_y())
"""


#
"""
from dataclasses import dataclass, field

@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare = False)
    surname: str = field(compare = False)
    value: int = field(repr = False)    

@dataclass
class FootballTeam:
    name: str
    players: list = field(default_factory=list, repr = False, compare = False)  
    
    def add_players(self, *players):
        for player in players:
            self.players.append(player)

player = FootballPlayer('Kylian', 'Mbappe', 180000000)
print(player)
print(player.name)
print(player.surname)
print(player.value)

team = FootballTeam('PSG')
print(team)
print(team.name)
print(team.players)
team.add_players(FootballPlayer('Kylian', 'Mbappe', 180000000))
print(team.players)
"""


######################################################## Final exersices ########################################################

# 2
"""
import math

class Vector:

    def __init__(self, *args):
        self.args = args
        
    def __add__(self, other):
        if len(self.args) == len(other.args):
            return type(self)(*[self.args[i] + other.args[i] for i in range(len(self.args))])
        raise ValueError('Векторы должны иметь равную длину')
    
    def __sub__(self, other):
        if len(self.args) == len(other.args):
            return type(self)(*[self.args[i] - other.args[i] for i in range(len(self.args))])
        raise ValueError('Векторы должны иметь равную длину')
    
    def __mul__(self, other):
        if len(self.args) == len(other.args):
            return sum([self.args[i] * other.args[i] for i in range(len(self.args))])
        raise ValueError('Векторы должны иметь равную длину')
    
    def norm(self):
        return math.sqrt(sum([self.args[i] ** 2  for i in range(len(self.args))]))
    
    def __str__(self):
        return f"{self.__dict__['args']}"
    
    def __eq__(self, other):
        if isinstance(other, type(self)):
            if len(self.args) == len(other.__dict__['args']):
                return self.args == other.__dict__['args']
            else:
                raise ValueError('Векторы должны иметь равную длину')
        return NotImplemented
    
a = Vector(1, 2, 3)
b = Vector(3, 4, 5)
c = Vector(5, 6, 7, 8)

print(a)                       # (1, 2, 3)
print(b)                       # (3, 4, 5)
print(c)                       # (5, 6, 7, 8)

print(a + b)                   # (4, 6, 8)
print(a - b)                   # (-2, -2, -2)
print(a * b)                   # 1*3 + 2*4 + 3*5 = 26
print(c.norm())                # sqrt(5**2 + 6**2 + 7**2 + 8**2) = sqrt(174) = 13.19090595827292

print(a == Vector(1, 2, 3))    # True
print(a == Vector(4, 5, 6))    # False

vector1 = Vector(1, 2, 3)
vector2 = Vector(5, 6, 7, 8)
try:
    print(vector1 == vector2)
except ValueError as e:
    print(e)

vector1 = Vector(1, 2)
vector2 = Vector(3, 4)
vector3 = vector1 + vector2
vector4 = vector1 - vector2
print(type(vector3))
print(type(vector4)) 
"""


# 3 Не доделана!!!!!
"""
class CaesarCipher:
    
    def __init__(self, step):
        self.step = step

    def encode(self, text):
        res_string = ''
        for el in text:
            figure = ord(el)+self.step
            if type(self).check_abc(self, el):
                if figure > 122:
                    figure = (figure - 122) + 97
                if figure < 97:
                    figure = 122 - (97 - figure)  
                res_string += chr(figure)    
            elif type(self).check_ABC(self, el):
                if figure > 90:
                    figure = (figure - 90) + 65
                if figure < 65:
                    figure = 90 - (65 - figure)
                res_string += chr(figure)       
            else:
                res_string += el      
        return res_string    
        
    def decode(self, text):
        self.step = -self.step
        res = type(self).encode(self, text)
        self.step = -self.step
        return res

    def check_abc(self, el):
        if el in [chr(i) for i in range(ord('a'), ord('z')+1)]:
            return True
        return False
    
    def check_ABC(self, el):
        if el in [chr(i) for i in range(ord('A'), ord('Z')+1)]:
            return True
        return False

cipher = CaesarCipher(10)

print(cipher.encode('G'))
print(cipher.decode('G'))
"""


# 4
"""
class ArithmeticProgression:
    
    def __init__(self, start, step, flag = False):
        self.start = start
        self.step = step
        self.flag = flag
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.flag:
            self.start = self.start+self.step
        self.flag = True    
        return self.start 

        
class GeometricProgression(ArithmeticProgression):
    
    def __next__(self):
        if self.flag:
            self.start = self.start*self.step
        self.flag = True    
        return self.start

progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 0 1 2 3 4 5 6 7 8 9 10

progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 1 2 4 8
"""


# 5
"""
from re import fullmatch, sub, split

class DomainException(Exception):

    def __str__(self):
        return 'Недопустимый домен, url или email'

        
class Domain:

    def __init__(self, domen):
        self.domen = type(self).check_domen(domen)

    def __str__(self):
        return f'{self.domen}'    

    @classmethod
    def from_url(cls, domen):
        domen = sub(r'https://', '', domen)
        domen = sub(r'http://', '', domen)
        return cls(cls.check_domen(domen))
    
    @classmethod
    def from_email(cls, domen):
        domen = split(r'@', domen, maxsplit=1)
        if fullmatch(r'[a-zA-Z]+', domen[0]):
            return cls(cls.check_domen(domen[-1]))
        else:
            raise DomainException

    @staticmethod
    def check_domen(domen):
        if fullmatch(r'[a-zA-Z]+\.[a-zA-Z]+', domen):
            return domen
        else:
            raise DomainException

domain1 = Domain('pygen.ru')                       # непосредственно на основе домена
domain2 = Domain.from_url('https://pygen.ru')      # на основе url-адреса
domain3 = Domain.from_email('support@pygen.ru')    # на основе адреса электронной почты

print(str(domain1))                                # pygen.ru
print(str(domain2))                                # pygen.ru
print(str(domain3))                                # pygen.ru
"""


# 6
"""
class HighScoreTable:

    def __init__(self, max_score, iterable = []):
        self.max_score = max_score
        self.iterable = iterable
    
    @property
    def scores(self):
        self.iterable = sorted(self.iterable, reverse = True)
        self.iterable = self.iterable[:]
        return self.iterable

    def update(self, figure):
        if len(self.iterable) >= self.max_score:
            if min(self.iterable) < figure:
                self.iterable.remove(min(self.iterable))
                self.iterable.append(figure) 
        else:    
            self.iterable.append(figure)    

    def reset(self):
        return self.iterable.clear()
    
high_score_table = HighScoreTable(3)

print(high_score_table.scores)    # []
high_score_table.update(10)
high_score_table.update(8)
high_score_table.update(12)
print(high_score_table.scores)    # [12, 10, 8]

high_score_table.update(6)
high_score_table.update(7)
print(high_score_table.scores)    # [12, 10, 8]
high_score_table.update(9)
print(high_score_table.scores)    # [12, 10, 9]

high_score_table.reset()
print(high_score_table.scores)
"""  


# 7
"""
class Pagination:

    def __init__(self, alphabet, number):
        self.alphabet = alphabet
        self.number = number
        self.index = 1
        if len(alphabet)%self.number > 0:
            self.max_page = len(alphabet)//self.number + 1   
        else:
            self.max_page = int(len(alphabet)/self.number)    

    def get_visible_items(self):
        return self.alphabet[self.number*(self.index-1) : self.number*(self.index)]  

    def next_page(self):
        self.index += 1
        self.index = self.check_number()
        return self

    def prev_page(self):
        self.index -= 1
        self.index = self.check_number() 
        return self

    def first_page(self):
        self.index = 1
        return self

    def last_page(self):
        self.index = self.max_page 
        return self

    def go_to_page(self, page):
        self.index = page
        self.index = self.check_number()
        return self

    def check_number(self):
        if self.index > self.max_page:
            self.index = self.max_page
        if self.index < 1:
            self.index = 1    
        return self.index   

    @property
    def total_pages(self):
        return self.max_page
    
    @property
    def current_page(self):
        return self.index


alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.next_page()
print(pagination.get_visible_items())    # ['e', 'f', 'g', 'h']

pagination.last_page()
print(pagination.get_visible_items())    # ['y', 'z']

pagination.first_page()
pagination.next_page().next_page()   
print(pagination.get_visible_items())    # ['i', 'j', 'k', 'l']

print(pagination.total_pages)            # 7
print(pagination.current_page)           # 3

pagination.first_page()
pagination.prev_page()
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.last_page()
pagination.next_page()
print(pagination.get_visible_items())    # ['y', 'z']

pagination.go_to_page(-100)
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.go_to_page(100)
print(pagination.get_visible_items())    # ['y', 'z']
"""


# Классы Testpaper и Student - составляет и проверяет экзаменационные тесты. 
# Каждый тест должен создаваться на основе темы, схемы верных ответов и минимального процента верных решений
"""
class Testpaper:

    def __init__(self, spec, true_answers, pass_degrees):
        self.spec = spec
        self.true_answers = true_answers
        self.pass_degrees = pass_degrees

        
class Student:

    def __init__(self):
        self.res_dict = {}
    
    def take_test(self, answers, student_answers):

        student_degrees = round((100 / len(answers.true_answers)) * sum([answers.true_answers[i] == student_answers[i] for i in range(len(answers.true_answers))]))

        if  student_degrees >= int(answers.pass_degrees.strip('%')):
            student_pass = 'Passed!'
        else:
            student_pass = 'Failed!'
        self.res_dict.setdefault(answers.spec, f'{student_pass} ({student_degrees}%)')
        return self.res_dict
    
    @property
    def tests_taken(self):
        if self.res_dict:
            return self.res_dict
        return 'No tests taken'
    
testpaper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
testpaper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
testpaper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

student1 = Student()
student2 = Student()
student3 = Student()

student1.take_test(testpaper1, ['1A', '2D', '3D', '4A', '5A'])
student2.take_test(testpaper2, ['1C', '2D', '3A', '4C'])
student2.take_test(testpaper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])

print(student1.tests_taken)    # {'Maths': 'Passed! (80%)'}
print(student2.tests_taken)    # {'Chemistry': 'Failed! (25%)', 'Computing': 'Failed! (43%)'}
print(student3.tests_taken)    # No tests taken
"""


##
"""
class TicTacToe:

    def __init__(self):
        self.game_place = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.point = 1
        self.game_end = False
        
    def mark(self, x, y):
        type(self).winner(self)
        if self.game_end is not True:
            if self.point % 2 != 0:
                mark_point = 'X'
            else:
                mark_point = 'O'

            current_element = self.game_place[x-1].pop(y-1)    
            if current_element != mark_point:
                self.game_place[x-1].insert(y-1, mark_point)
                self.point += 1
            else:
                self.game_place[x-1].insert(y-1, current_element)
                print('Недоступная клетка')
        else:
            print('Игра окончена')        
            
    def show(self):
        for i in range(len(self.game_place)-1):
            print('|'.join(self.game_place[i]))
            print('-'*5)
        print('|'.join(self.game_place[-1]))    
            
    def winner(self):
        for line in self.game_place:
            if (
                line.count('X') == 3 or 
                [self.game_place[0][0], self.game_place[1][0], self.game_place[2][0]].count('X') == 3 or
                [self.game_place[0][1], self.game_place[1][1], self.game_place[2][1]].count('X') == 3 or
                [self.game_place[0][2], self.game_place[1][2], self.game_place[2][2]].count('X') == 3 or
                [self.game_place[0][0], self.game_place[1][1], self.game_place[2][2]].count('X') == 3 or
                [self.game_place[0][2], self.game_place[1][1], self.game_place[2][0]].count('X') == 3
                ): 
                self.game_end = True   
                return 'X' 
            elif (
                line.count('O') == 3 or 
                [self.game_place[0][0], self.game_place[1][0], self.game_place[2][0]].count('O') == 3 or
                [self.game_place[0][1], self.game_place[1][1], self.game_place[2][1]].count('O') == 3 or
                [self.game_place[0][2], self.game_place[1][2], self.game_place[2][2]].count('O') == 3 or
                [self.game_place[0][0], self.game_place[1][1], self.game_place[2][2]].count('O') == 3 or
                [self.game_place[0][2], self.game_place[1][1], self.game_place[2][0]].count('O') == 3
                ):
                self.game_end = True   
                return 'O'  
            elif self.point >= len(self.game_place)*3+1:
                self.game_end = True
                return 'Ничья' 
            return None 
                  
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 2)
tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)
tictactoe.mark(2, 2)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)

#tictactoe.show()
"""


## Не доделал!!
"""
import random
import itertools
import time

class Game:

    def __init__(self, rows: int, cols: int, mines: int) -> None:
        self.rows = rows
        self.cols = cols
        self.mines = mines
    
    @property
    def board(self) -> list:
        res_place = []
        temp_list = []
        try:
            for row in range(self.rows):
                for col in range(self.cols):
                    cell = Cell(row, col)
                    temp_list.append(cell)        
                res_place.append(temp_list)
                temp_list = []
            for row in itertools.cycle(range(self.rows)):
                for col in range(self.cols):
                    if res_place[row][col].mine != 1:
                        res_place[row][col].mine = random.randint(0,1)
                        if res_place[row][col].mine == 1:
                            self.mines -= 1
                    if self.mines == 0:
                        raise StopIteration
        except StopIteration:      
            for row in range(self.rows):
                for col in range(self.cols):
                    if col-1 >= 0 or col+1<= self.cols:
                        print(row, col)
                        if res_place[row][col-1].mine == 1:
                            print('test1')
                            res_place[row][col].neighbours += 1
                        if res_place[row][col+1].mine == 1:   
                            print('test2')
                            res_place[row][col].neighbours += 1

        finally:
            return res_place                          

            
class Cell:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.mine = 0       #через random 1 или 0 устанавливаем мину или нет
        self.open = False      #по умолчанию ячейка закрыта
        self.neighbours = 0 #?

game = Game(2, 2, 2)    # 14 строк, 18 столбцов и 40 мин
#print(game.rows)           # 14
#print(game.cols)           # 18
#print(game.mines)          # 40

#cell = game.board[0][0]

#print(cell.row)            # 0; строка ячейки
#print(cell.col)            # 0; столбец ячейки
#print(cell.mine)           # True или False в зависимости от того, содержит ячейка мину или нет
#print(cell.open)           # True или False в зависимости от того, открыта ячейка или нет, по умолчанию закрыта
#print(cell.neighbours)     # число от 0 до 8, количество мин в соседних ячейках


for line in game.board:
    for cell in line:
        print(cell.row, cell.col, cell.mine, cell.neighbours)
"""


## Не доделал!
"""
class Currency:

    def __init__(self, value: int, money: str):
        self.value = value
        self.money = money

    def __str__(self) -> str:
        return f'{self.value} {self.money}'

    def change_to(self, money):
        if self.money == 'RUB':
            if money == 'USD':
                self.value = round(self.value / 81.81818, 2)
            elif money == 'EUR':
                self.value = round(self.value / 90, 2) 
        elif self.money == 'USD':
            if money == 'RUB':
                self.value = round(self.value * 81.81818, 2)
            elif money == 'EUR':
                self.value = round(self.value / 1.1, 2)
        elif self.money == 'EUR':
            if money == 'RUB':
                self.value = round(self.value * 90, 2)
            elif money == 'USD':
                self.value = round(self.value * 1.1, 2)
        self.money = money 

    def __add__(self, other):
        other.change_to(self.money)
        self.value = round(self.value + other.value, 2)
        return self   

    def __sub__(self, other):
        other.change_to(self.money)
        self.value = round(self.value - other.value, 2)
        return self 

    def __mul__(self, other):
        other.change_to(self.money)
        self.value = round(self.value * other.value, 2)
        return self  

    def __truediv__(self, other):
        other.change_to(self.money)
        self.value = round(self.value / other.value, 2)
        return self        
         
money = Currency(2000, 'RUB')
currencies = ['EUR', 'USD', 'RUB']
operation_funcs = ['__sub__', '__mul__', '__add__', '__truediv__']
operation_signs = ['-', '*', '+', '/']
currency = 0
operation = 0

values = [46, 54, 18, 81, 16, 86, 40, 82, 31, 74, 82, 39, 72, 40, 16, 72, 16, 24, 74, 30, 37, 87, 67, 95, 54, 79, 86,
          69, 44, 24, 92, 22, 80, 10, 46, 93, 10, 81, 43, 30, 12, 80, 99, 77, 89, 71, 55, 93, 77, 70, 26, 38, 16, 49,
          34, 33, 98, 22, 13, 79, 67, 99, 48, 97, 38, 96, 43, 72, 64, 74, 97, 52, 96, 86, 37, 36, 52, 63, 43, 13, 39,
          43, 52, 33, 92, 56, 17, 20, 94, 21, 28, 57, 96, 77, 99, 88, 38, 28, 70, 59]

for value in values:
    money.change_to(currencies[currency % 3])
    current_currency = currency % 3 - 1
    current_operation = operation % 4
    print(f'{money} {operation_signs[current_operation]} {value} {currencies[current_currency]} = ', end='')
    print(Currency.__dict__[operation_funcs[current_operation]](money, Currency(value, currencies[current_currency])))
    currency += 1
    operation += 1
"""

############################################## Классы Game и Cell ######################################################
import random

# игровое поле
class Game:
    def __init__(self, rows: int, cols: int, mines: int) -> None:
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.mines_count = mines
        self.board = []

        temp_list = []    
        index_list = []
        neighbours = 0

        # заполнение игрового поля экземплярами ячейки
        for row in range(self.rows):
            for col in range(self.cols):
                temp_list.append(Cell(row, col))
            self.board.append(temp_list)
            temp_list =[]

        # минируем поле в произвольном порядке    
        while self.mines_count > 0:
            row = random.randint(0,self.rows-1) 
            col = random.randint(0,self.cols-1) 
             
            # проверка уникальности координат минирования
            if (row,col) not in index_list:
                index_list.append((row,col)) 
                current_cell = self.board[row][col]
                current_cell.__dict__['mine'] = True 
                self.board[row][col] = current_cell
                self.mines_count -= 1

        # подсчет мин у соседей
        for row in range(self.rows):
            for col in range(self.cols):
                for i in range(-1,2):
                    for j in range(-1,2):
                        if row+i in range(0,self.rows) and col+j in range(0,self.cols):
                            if self.board[row+i][col+j].mine == True:
                                neighbours +=1
                if self.board[row][col].__dict__['mine'] == True and neighbours > 0:                
                    neighbours -= 1
                self.board[row][col].__dict__['neighbours'] = neighbours
        
        # подсчет мин у соседей

        # перебираем ячейки поля
        for row in range(self.rows):
            for col in range(self.cols):
                current_cell = self.board[row][col]

                # перебираем соседей current_cell
                for i in range(-1,2):
                    for j in range(-1,2):
                        neighbour_row, neighbour_col = row+i, col+j

                        # проверяем, что сосед в переделах доски
                        if neighbour_row in range(0,self.rows) and neighbour_col in range(0,self.rows):
                            neighbour_cell = self.board[neighbour_row][neighbour_col]
                            print(neighbour_row,neighbour_col)
                            if neighbour_cell.mine == True:
                                neighbours +=1

                # не учитываем мину в current_cell              
                if current_cell.mine == True and neighbours > 0:                
                    neighbours -= 1
                current_cell.neighbours = neighbours
                neighbours = 0


# ячейка
class Cell(Game):
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.mine = False
        self.open = False
        self.neighbours = 0
        

# проверочная зона
game = Game(3, 5, 4)    # 14 строк, 18 столбцов и 40 мин
print(game.rows)           
print(game.cols)           
print(game.mines) 

for i in range(game.rows):
    for j in range(game.cols):
        print(('*' if game.board[i][j].mine == True else '-', game.board[i][j].neighbours), end = ' ')
    print()           

"""
cell = game.board[0][0]
print(cell.row)            # 0; строка ячейки
print(cell.col)            # 0; столбец ячейки
print(cell.mine)           # True или False в зависимости от того, содержит ячейка мину или нет
print(cell.open)           # True или False в зависимости от того, открыта ячейка или нет, по умолчанию закрыта
print(cell.neighbours)     # число от 0 до 8, количество мин в соседних ячейках
"""