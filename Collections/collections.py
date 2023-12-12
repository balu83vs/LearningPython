##########################################################################################
                                    # namedtuple
##########################################################################################

# 1
"""
from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('D:/py_learning/py_programs/files/data.pkl', 'rb') as input_pkl:
     
# реализация через обычный словарь    
 #   for in_dict in pickle.load(input_pkl):
 #       for el in in_dict._asdict():
 #           print(f'{el}: {in_dict._asdict()[el]}')
 #       print() 

# реализация через _fields и zip
    for in_dict in pickle.load(input_pkl):
        for field, value in zip(Animal._fields, in_dict):
            print(f'{field}: {value}')
        print()
"""


# 2
"""
from collections import namedtuple

res_list = []
temp_list = []

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]


def view(input_list):
    # функция вывода на экран
    for el in input_list:
        print(el.name, el.surname)
        print(f'  {User._fields[2].capitalize()}: {el.email}')
        print(f'  {User._fields[3].capitalize()}: {el.plan}')
        print()         

# создаем рабочий список User-ов
for el in users:
    res_list.append(el)

res_list = sorted(res_list, key = lambda x: x.email)                            # сортируем по почте
temp_list = list(filter(lambda x: x if x.plan == 'Gold' else None, res_list))   # фильтруем по статусу подписки Gold
view(temp_list)
temp_list = list(filter(lambda x: x if x.plan == 'Silver' else None, res_list)) # фильтруем по статусу подписки Silver
view(temp_list)
temp_list = list(filter(lambda x: x if x.plan == 'Bronze' else None, res_list)) # фильтруем по статусу подписки Bronze
view(temp_list)
temp_list = list(filter(lambda x: x if x.plan == 'Basic' else None, res_list))  # фильтруем по статусу подписки Basic
view(temp_list)

# вариант реализации через обычные Tuple
#users = sorted(users, key = lambda x: x[2])
#temp = list(filter(lambda x: x if x[3] == 'Gold' else None, users))
#for el in temp:
#    print(el)
"""


# Вы кто такие? Я вас не звал
"""
import csv
from collections import namedtuple
from datetime import datetime

res_list =[]

with open('D:/py_learning/py_programs/meetings.csv', encoding='utf-8') as input_csv:
    csv_file = csv.DictReader(input_csv, delimiter=',')

    headers = csv_file.fieldnames  
    Meetings = namedtuple('Meetings', [*headers])
    
    for el in csv_file:
        res_list.append(Meetings._make(el.values()))
    res_list = sorted(res_list, key = lambda x: datetime.strptime((x.meeting_date + ' ' + x.meeting_time), '%d.%m.%Y %H:%M'))
    for el in res_list:
        print(f'{el.surname} {el.name}')
"""


##########################################################################################
                                    # defaultdict
##########################################################################################
# 1
"""
from collections import defaultdict

data = [('Books', 1343), 
        ('Books', 1166), 
        ('Merch', 616), 
        ('Courses', 966), 
        ('Merch', 1145), 
        ('Courses', 1061), 
        ('Books', 848), 
        ('Courses', 964), 
        ('Tutorials', 832), 
        ('Merch', 642), 
        ('Books', 815), 
        ('Tutorials', 1041), 
        ('Books', 1218), 
        ('Tutorials', 880), 
        ('Books', 1003), 
        ('Merch', 951), 
        ('Books', 920), 
        ('Merch', 729), 
        ('Tutorials', 977), 
        ('Books', 656)]
data = sorted(data)
res_dict = defaultdict(int)

for el in data:
    res_dict[el[0]] += el[1]

for el in res_dict:
    print(f'{el}: ${res_dict.get(el)}')
"""


# подсчет сотрудников в каждом отделе
"""
from collections import defaultdict

staff = [('Sales', 'Robert Barnes'), 
         ('Developing', 'Thomas Porter'), 
         ('Accounting', 'James Wilkins'), 
         ('Sales', 'Connie Reid'), 
         ('Accounting', 'Brenda Davis'), 
         ('Developing', 'Miguel Norris'), 
         ('Accounting', 'Linda Hudson'), 
         ('Developing', 'Deborah George'), 
         ('Developing', 'Nicole Watts'), 
         ('Marketing', 'Billy Lloyd'), 
         ('Sales', 'Charlotte Cox'), 
         ('Marketing', 'Bernice Ramos'), 
         ('Sales', 'Jose Taylor'), 
         ('Sales', 'Katie Warner'), 
         ('Accounting', 'Steven Diaz'), 
         ('Accounting', 'Kimberly Reynolds'), 
         ('Accounting', 'John Watts'), 
         ('Accounting', 'Dale Houston'),
         ('Developing', 'Arlene Gibson'), 
         ('Marketing', 'Joyce Lawrence'), 
         ('Accounting', 'Rosemary Garcia'), 
         ('Marketing', 'Ralph Morgan'), 
         ('Marketing', 'Sam Davis'), 
         ('Marketing', 'Gail Hill'), 
         ('Accounting', 'Michelle Wright'), 
         ('Accounting', 'Casey Jenkins'), 
         ('Sales', 'Evelyn Martin'), 
         ('Accounting', 'Aaron Ferguson'), 
         ('Marketing', 'Andrew Clark'), 
         ('Marketing', 'John Gonzalez'), 
         ('Developing', 'Wilma Woods'), 
         ('Sales', 'Marie Cooper'), 
         ('Accounting', 'Kay Scott'),
         ('Sales', 'Gladys Taylor'), 
         ('Accounting', 'Ann Bell'), 
         ('Accounting', 'Craig Wood'), 
         ('Accounting', 'Gloria Higgins'), 
         ('Marketing', 'Mario Reynolds'), 
         ('Marketing', 'Helen Taylor'),
         ('Marketing', 'Mary King'),
         ('Accounting', 'Jane Jackson'),
         ('Marketing', 'Carol Peters'),
         ('Sales', 'Alicia Mendoza'),
         ('Accounting', 'Edna Cunningham'),
         ('Developing', 'Joyce Rivera'),
         ('Sales', 'Joseph Lee'),
         ('Sales', 'John White'),
         ('Marketing', 'Charles Bailey'),
         ('Sales', 'Chester Fernandez'),
         ('Sales', 'John Washington')]

staff = sorted(staff)
res_dict = defaultdict(int)

for el in staff:
    res_dict[el[0]] += 1
    
for el in res_dict.keys():
    print(f'{el}: {res_dict.get(el)}') 
"""


# списки работников по отделам
"""
from collections import defaultdict

staff_broken = [('Developing', 'Miguel Norris'), 
                ('Sales', 'Connie Reid'), 
                ('Sales', 'Joseph Lee'), 
                ('Marketing', 'Carol Peters'), 
                ('Accounting', 'Linda Hudson'), 
                ('Accounting', 'Ann Bell'), 
                ('Marketing', 'Ralph Morgan'), 
                ('Accounting', 'Gloria Higgins'), 
                ('Developing', 'Wilma Woods'),
                ('Developing', 'Wilma Woods'),
                ('Marketing', 'Bernice Ramos'),
                ('Marketing', 'Joyce Lawrence'),
                ('Accounting', 'Craig Wood'),
                ('Developing', 'Nicole Watts'),
                ('Sales', 'Jose Taylor'),
                ('Accounting', 'Linda Hudson'),
                ('Accounting', 'Edna Cunningham'),
                ('Sales', 'Jose Taylor'),
                ('Marketing', 'Helen Taylor'),
                ('Accounting', 'Kimberly Reynolds'),
                ('Marketing', 'Mary King'),
                ('Sales', 'Joseph Lee'),
                ('Accounting', 'Gloria Higgins'),
                ('Marketing', 'Andrew Clark'),
                ('Accounting', 'John Watts'),
                ('Accounting', 'Rosemary Garcia'),
                ('Accounting', 'Steven Diaz'),
                ('Marketing', 'Mary King'),
                ('Sales', 'Gladys Taylor'),
                ('Developing', 'Thomas Porter'),
                ('Accounting', 'Brenda Davis'),
                ('Sales', 'Connie Reid'),
                ('Sales', 'Alicia Mendoza'),
                ('Marketing', 'Mario Reynolds'),
                ('Sales', 'John White'),
                ('Developing', 'Joyce Rivera'),
                ('Accounting', 'Steven Diaz'),
                ('Developing', 'Arlene Gibson'),
                ('Sales', 'Robert Barnes'),
                ('Sales', 'Charlotte Cox'),
                ('Accounting', 'Craig Wood'),
                ('Marketing', 'Carol Peters'),
                ('Marketing', 'Ralph Morgan'),
                ('Accounting', 'Kay Scott'),
                ('Sales', 'Evelyn Martin'),
                ('Marketing', 'Billy Lloyd'),
                ('Sales', 'Gladys Taylor'),
                ('Developing', 'Deborah George'),
                ('Sales', 'Charlotte Cox'),
                ('Marketing', 'Sam Davis'),
                ('Sales', 'John White'),
                ('Sales', 'Marie Cooper'),
                ('Marketing', 'John Gonzalez'),
                ('Sales', 'John Washington'),
                ('Sales', 'Chester Fernandez'),
                ('Sales', 'Alicia Mendoza'),
                ('Sales', 'Katie Warner'),
                ('Accounting', 'Jane Jackson'),
                ('Sales', 'Chester Fernandez'),
                ('Marketing', 'Charles Bailey'),
                ('Marketing', 'Gail Hill'),
                ('Accounting', 'Casey Jenkins'),
                ('Accounting', 'James Wilkins'),
                ('Accounting', 'Casey Jenkins'),
                ('Marketing', 'Mario Reynolds'),
                ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Kimberly Reynolds'),
                ('Sales', 'Robert Barnes'),
                ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Jane Jackson'),
                ('Developing', 'Deborah George'),
                ('Accounting', 'Michelle Wright'),
                ('Accounting', 'Dale Houston')]

staff_broken = sorted(staff_broken)
res_dict = defaultdict(str)

for el in staff_broken:
    res_dict[el[0]] += f'{el[1]}  '

for el in res_dict:
    res_dict[el] = list(filter(lambda x: x if len(x) != 0 else None, {el2: None for el2 in res_dict.get(el).split('  ')}.keys()))

for res in res_dict:
    print(f'{res}: ', end = '')
    for i in range(len(res_dict.get(res))):
        if i == len(res_dict.get(res)) - 1:
            print(res_dict.get(res)[i], end = '')
        else:
            print(res_dict.get(res)[i] + ', ', end = '')    
    print()
"""


# Функция wins()
"""
from collections import defaultdict

def wins(args):
    res_dict = defaultdict(set)
    for el in args:
        res_dict[el[0]].add(el[1])
    return res_dict

result = wins([('Артур', 'Дима'),
                ('Артур', 'Тимур'),
                ('Артур', 'Анри'),
                ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))
"""


# Функция flip_dict()
"""
from collections import defaultdict

def flip_dict(dict_of_lists):
    res_dict = defaultdict(list)
    for el in dict_of_lists.items():
        for el2 in el[1]:
            res_dict[el2].append(el[0])
    return res_dict

data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')
"""


# Функция best_sender()
"""
from collections import defaultdict

def best_sender(messages, senders):
    res_dict = defaultdict(int)
    for el in zip(senders, messages):
        res_dict[el[0]] += len(el[1].split())
    max = 0
    res_list = []
    for name in sorted(res_dict.items(), key = lambda x: x[1], reverse=True):
        if name[1] >= max:
            res_list.append(name[0])
            max = name[1]    
    res_list = sorted(res_list, reverse = True)
    return res_list[0]

messages = ['bu bu da', 'bu bu da', 'bu bu da', 'bu bu da', 'bu bu da', 'bu bu net']
senders = ['dima', 'anri', 'timur', 'timur', 'anri', 'dima']

print(best_sender(messages, senders))
"""


##########################################################################################
                                    # OrderedDict
##########################################################################################
#1
"""
from collections import OrderedDict

grades = OrderedDict(Timur=100, Arthur=84, Anri=94, Dima=98)
new_grades = OrderedDict()
for rule in (True, False, False, True):
    name, grade = grades.popitem(last=rule)
    print(name, grade)
    new_grades[name] = grade    
print(*new_grades)
"""


#2
"""
from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 
                    'IsNetObject': 'да', 
                    'OperatingCompany': 'Брусника', 
                    'TypeObject': 'кафе', 
                    'AdmArea': 'Центральный административный округ', 
                    'District': 'район Арбат', 
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 
                    'SeatsCount': '10'})
print(OrderedDict(reversed(data.items())))
"""


#3
"""
from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 
                    'IsNetObject': 'да',
                    'OperatingCompany': 'Брусника',
                    'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ',
                    'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
                    'SeatsCount': '10'})
new_data = OrderedDict()

for rule in range(1, len(data) + 1):
    if rule % 2 != 0:
        el1, el2 = data.popitem(last = False)
        #print(el1,el2)
    else:
        el1, el2 = data.popitem(last = True)    
        #print(el1,el2)
    new_data[el1] = el2

print(OrderedDict(new_data.items()))       
"""


#4
"""
from collections import OrderedDict

def my_sort_keys(reverse = False):
    return sorted(data.keys(), reverse = reverse)

def my_sort_values(reverse = False):
    return sorted(data.values(), reverse = reverse)    

data = OrderedDict({'Law & Order': 1990,
                    'The Practice': 1997,
                    'Six Feet Under': 2001,
                    'Joan of Arcadia': 2003,
                    'The West Wing': 1999,
                    'Deadwood': 2004,
                    'The Sopranos': 1999,
                    'Boston Legal': 2004,
                    'ER': 1994,
                    'Friday Night Lights': 2006,
                    '24': 2001,
                    'Heroes': 2006,
                    'Lost': 2004,
                    'Dexter': 2006,
                    'Damages': 2007,
                    'Big Love': 2006,
                    'House': 2004,
                    'Downton Abbey': 2010,
                    "Grey's Anatomy": 2005,
                    'Homeland': 2011,
                    'Breaking Bad': 2008,
                    'Game of Thrones': 2011,
                    'CSI: Crime Scene Investigations': 2000,
                    'Boardwalk Empire': 2010,
                    'True Blood': 2008,
                    'House of Cards': 2013,
                    'True Detective': 2014})

data.sorted_keys = my_sort_keys
data.sorted_values = my_sort_values

print(data.sorted_keys(reverse = True))
print(data.sorted_values(reverse = True))
"""


# custom_sort()
"""
from collections import OrderedDict

def get_key(data, value):
    for k, v in data.items():
        if v == value:
            return k

def custom_sort(data, by_values=False):
    if by_values is True:
        for value in sorted(data.values()):
            data.move_to_end(get_key(data, value))
    else:
        for key in sorted(data):
            data.move_to_end(key)

data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)

custom_sort(data, by_values=False)

print(data)
"""


##########################################################################################
                                        # Counter
##########################################################################################
#1
"""
from collections import Counter

files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
         'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
         'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
         'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
         'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
         'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
         'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
         'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
         'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
         'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
         'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
         'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
         'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']

files = list(map(lambda x: x.split('.')[1], files))
res_dict = Counter(files)
for el in sorted(res_dict.keys()):
    print(f'{el}: {res_dict[el]}')
"""


# Функция count_occurences()
"""
from collections import Counter

def count_occurences(word, words):
    words  = list(map(lambda x: x.lower(), words.split(' ')))
    res = Counter(words)
    return res[word.lower()]

word = 'python'
words = 'Python Conferences python training python events'

print(count_occurences(word, words))
"""


# А сколько стоит курс?
"""
from collections import Counter, defaultdict

count_symbol = defaultdict(int)
products = input().split(',')

for el in products:
    count_symbol[el] = len(el)

max_len = max(count_symbol.values())
res = Counter(products)
keys = sorted(res.keys())

for key in keys: 
    sum_ord = sum(list(map(lambda x: ord(x), ''.join(key.split(' ')))))
    print(f'{key}{" "*(max_len - len(key))}: {sum_ord} UC x {res[key]} = {sum_ord*res[key]} UC')
"""


# The Zen of Python
"""
# длинное решение с алфавитом и сравнением
from collections import Counter, OrderedDict

abc = [chr(el) for el in range(97, 123)]

with open('D:/py_learning/py_programs/files/pythonzen.txt', encoding='utf-8') as input_file:
    data = input_file.read().lower()   
    small_data = list(filter(lambda x: x if x in abc else None, data))                   
    
res = OrderedDict(Counter(small_data))
res.items_sorted = lambda: sorted(res.items())

for key, value in dict(res.items_sorted()).items():
    print(f'{key}: {value}')

# упрощенное решение с использованием isalpha()
from collections import Counter, OrderedDict

with open('D:/py_learning/py_programs/files/pythonzen.txt', encoding='utf-8') as input_file:
    data = list(filter(lambda x: x if x.isalpha() else None, input_file.read().lower())) 

res = OrderedDict(Counter(data))
res.items_sorted = lambda: sorted(res.items())

for key, value in dict(res.items_sorted()).items():
    print(f'{key}: {value}')
"""


# Статистика длин слов
"""
from collections import Counter, defaultdict, OrderedDict

res_dict = defaultdict(int)

def get_key(data, value):
    for k, v in data.items():
        if v == value:
            return k

data = input().split()
data = Counter(data)

for el in data:
    res_dict[len(el)] += data[el]

res_dict = OrderedDict(res_dict)    

for value in sorted(res_dict.values()):
    res_dict.move_to_end(get_key(res_dict, value))

for key, value in res_dict.items():
    print(f'Слов длины {key}: {value}')
"""


# Все еще достоин
"""
import sys
from collections import Counter, defaultdict

data_dict = {el.strip('\n').split(' ')[0]: int(el.strip('\n').split(' ')[1]) for el in sys.stdin}
    
print(Counter(data_dict).most_common()[-2][0])
"""


#2
"""
from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewttoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.min_values = lambda: list(filter(lambda x: x if x[1] == data.most_common()[-1][1] else None, data.most_common()))
data.max_values = lambda: list(filter(lambda x: x if x[1] == data.most_common()[0][1] else None, data.most_common()))

print(data.min_values())
print(data.max_values())
"""


# Here we go again
"""
import csv

# с помощью defaultdict
from collections import Counter, defaultdict

res_dict = defaultdict(int)

with open('D:/py_learning/py_programs/files/name_log.csv', encoding='utf-8') as input_data:
    
    data = csv.DictReader(input_data, delimiter=',')
    data = sorted(data, key = lambda x: x['email'])

    for el in data:
        res_dict[el['email']] +=1    

    for key, value in res_dict.items():    
        print(f'{key}: {value}')

# с помощью Counter
from collections import Counter

with open('D:/py_learning/py_programs/files/name_log.csv', encoding='utf-8') as input_data:
    
    data = csv.DictReader(input_data, delimiter=',')
    email_list = sorted([el.get('email') for el in data])
    
    for key, value in Counter(email_list).items():
        print(f'{key}: {value}')
"""


# Функция print_bar_chart()
"""
from collections import Counter, OrderedDict

def print_bar_chart(languages, symbol):
    res_list = Counter(languages).most_common()
    max_len_word = max([len(word[0]) for word in res_list])
    for el in res_list:
        print(f'{el[0]}{" " * (max_len_word - len(el[0]))} |{symbol * el[1]}')

my_list = ['bbb', 'bbb', 'e', 'e', 'bbb', 'gggg', 'gggg', 'kkkkk', 'kkkkk', 'e', 'bbb', 'kkkkk']
print_bar_chart(my_list, '#')        
"""


# Расчет заработка
"""
import csv, json
from collections import Counter, defaultdict

data_dict = defaultdict(int)
sum_res = Counter()
    
def load_data(i):
    file = open(f'D:/py_learning/py_programs/collections/files/quarter{i}.csv', encoding='utf-8')
    data = csv.reader(file, delimiter=',') 
    next(data)
    #_, *data = csv.reader(file, delimiter=',') # более изящный вариант next на итераторе         
    
    for el in data:
        data_dict[el[0]] = sum([int(el2) for el2 in el[1:]]) 
    file.close()       
    return data_dict

for i in range(1,5):
    sum_res += Counter(load_data(i))  

with open('D:/py_learning/py_programs/collections/files/prices.json', encoding='utf-8') as prices:
    price = json.load(prices)
    for key, value in sum_res.items():
       sum_res[key] = value * price[key]
print(Counter(sum_res).total())
"""


# Расчет заработка2
"""
from collections import Counter

books = Counter(map(int, input().split(' ')))
summa = 0

for _ in range(int(input())):
    class_book, price_book = list(map(int, input().split(' ')))
    if books.get(class_book):
        summa += price_book
        books[class_book] -= 1
        
print(summa)
"""


######################################################################################
                                    # ChainMap
######################################################################################
# Зоопарк
"""
import json
from timeit import default_timer
from pympler import asizeof
from collections import ChainMap, Counter

def show_time(func):
    def wraper():
        start_time = default_timer()
        res = func()
        total_time = default_timer() - start_time
        print('Время выполнения программы: {:.10f}'.format(total_time))
        return res    
    return wraper

@ show_time
def animals_zoo():
    with open('D:/py_learning/py_programs/collections/files/zoo.json', encoding='utf-8') as animals:

        animals_data = json.load(animals)

        # res = Counter(ChainMap(*animals_data)).total()                    # через Counter
        # res = sum(ChainMap(*animals_data).values())                       # просто через SUM
        # res = sum([value for value in ChainMap(*animals_data).values()])  # через суммирование значений списка value

        #print(asizeof.asizeof(res))
        return res

print(animals_zoo())
"""


# Булочный магнат
"""
from collections import ChainMap, Counter  

summa = 0

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

menu = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(input().split(','))
max_name = max([len(name) for name in order.keys()])

for el, count in sorted(order.items()):
    summa += menu.get(el) * count
    print(f'{el}{" " * (max_name - len(el))} x {count}')

if len(f'ИТОГ: {summa}р') > len(f'{el}{" " * (max_name - len(el))} x {count}'):
    max_string = f'ИТОГ: {summa}р'
else:
    max_string = f'{el}{" " * (max_name - len(el))} x {count}'     

print("-" * len(max_string))
print(f'ИТОГ: {summa}р')
"""


# Функция get_all_values()
"""
from collections import ChainMap

def get_all_values(chainmap, key):
    res = set(filter(lambda x: x if type(x) is not None else None, [el.get(key) for el in chainmap.maps]))
    return res

chainmap = ChainMap({'name': 'Anri'}, {'name': 'Arthur', 'age': 20}, {'name': 'Timur', 'age': 29})
result = get_all_values(chainmap, 'age')

print(*sorted(result))
"""


# Функция deep_update()
"""
from collections import ChainMap

def deep_update(chainmap, key, value):
    map_chainmap = chainmap.maps
    if key in chainmap.keys():   
        if key in map_chainmap[0].keys():
            for i in range(len(map_chainmap)):
                map_chainmap[i][key] = value
        else:    
            for i in range(1, len(map_chainmap)):
                map_chainmap[i][key] = value 
    else:    
        chainmap[key] = value
   
chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')

print(chainmap)   
"""
