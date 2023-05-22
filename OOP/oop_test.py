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