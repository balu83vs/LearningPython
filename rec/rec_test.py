# Песочные часы
"""
def times():    
    def rec(step):
        el = ['1', '2', '3', '4']
        if 4 <= step <= 16:
            line = el[-int(step/4)] * step
            print(line.center(16))
            rec(step-4)
    rec(16)  
    def rec(step):
        el = ['1', '2', '3']
        if 8 <= step <= 16:
            line = el[- int(step/4) + 1] * step
            print(line.center(16))
            rec(step+4)
    rec(8)  

times()  
"""

# Функция print_digits()
"""
def print_digits(number):
    res_list = [num for num in str(number)]
    def rec(el):
        if el <= len(res_list):
            print(res_list[-el])
            rec(el + 1)
    rec(1)  
"""

# Количество цифр
"""
def cost(num):
    def rec(index):
        if index == 0:
            return 0
        else:
            return 1 + rec(index - 1)
    return rec(len(num))

print(cost(input()))
"""

# Сумма цифр
"""
def summa(num):
    def rec(index):
        if index == 0:
            return 0
        else:
            return int(num[index-1]) + rec(index - 1)
    return rec(len(num))
    
print(summa(input()))
"""

# number_of_frogs()
"""
def number_of_frogs(years):
    if years == 1:
        return 77
    else:
        return 3*(number_of_frogs(years - 1) - 30)
    
print(number_of_frogs(2))
"""

# Функция  is_power
"""
def is_power(number):
    if number < 2:
        if number == 1:
            return True
        else:
            return False
    else:
        return is_power(number / 2)

print(is_power(512))        
"""

# Tribonachi
"""
def tribonacci(n):
    cache = {1: 1, 2: 1, 3: 1}
    def rec(n):
        res = cache.get(n)
        if res is None:
            res = rec(n-3) + rec(n-2) + rec(n-1)
            cache[n] = res
        return res
    return rec(n)
"""

# Функция is_palindrome()
"""
def is_palindrome(s):
    def forward(index):
        if index >= len(s)/2:
            return True
        else:
            if s[index] != s[::-1][index]:
                return False
            return forward(index + 1) 
    return forward(0)

print(is_palindrome('122333221'))
"""

# to binary
"""
res = []

def to_binary(n):
    if n // 2 == 0:
        res.append(str(n % 2))        
        return ''.join(res[::-1])
    else:
        res.append(str(n % 2))
        return to_binary(n // 2)
"""

# Функция recursive_sum()
"""
total = 0

def recursive_sum(my_list):
    global total
    if not my_list:
        return 0
    if type(my_list) is not list:
        total += my_list
    if type(my_list) is list:
        for i in my_list:
            recursive_sum(i)
    return total 

my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))
"""

# Функция linear()
"""
def linear(my_list):
    res_list = []
    for i in my_list:
        if type(i) is list:
            res_list.extend(linear(i))
        else:
            res_list.append(i)
    return res_list     

my_list = [3, [4], [5, [6, [7, 8]]]]
print(linear(my_list))
"""

# Функция get_value()
"""
def get_value(my_dict, my_key):
    if my_key in my_dict:
        return my_dict[my_key]

    for k, v in my_dict.items():
        if type(v) is dict:
            value = get_value(v, my_key)
            if value is not None:
                return value

data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}
print(get_value(data, 'cityName'))                
"""

# Функция get_all_values() 
"""
def get_all_values(my_dict, my_key):
    res_set = set()
    
    for k, v in my_dict.items():
        if k == my_key:
            res_set.add(v)
        if isinstance(v, dict):
            res_set.update(get_all_values(v, my_key))

    return res_set

my_dict = {
           'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 
           'Timur': {'hobby': 'math'},
           'Dima': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'age')
print(*result)    
"""    

# Функция dict_travel()
"""
def dict_travel(data, res_str = ''):
    for k,v in sorted(data.items()):
        if isinstance(v, dict):
            dict_travel(v, res_str + f'{k}.')
        else:
            print(f'{res_str}{k}: {v}')
"""

def fib(n):
    cache = {0: 0, 1: 1, 2: 1}
    #for k,v in cache.items():
        #print(v)
    def rec(n):
        res = cache.get(n)
        if res is None:
            res = rec(n-2) + rec(n-1)
            cache[n] = res
            #print(res)    
        return res
    return rec(n)    

    
print(fib(10))