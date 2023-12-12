##################################################################################   
                                #Регулярные выражения 
##################################################################################

# Задача поиска телефонных номеров в тексте, без использоания регулярных выражений
"""
input_string = input()
number = ''
numbers_list = []
temp_number = [0,0,0,0,0]
for el in input_string:
    if el in [str(i) for i in range(10)] + ['-']:
        number += el
        if (number[0] == '7' and len(number) == 15) or (number[0] == '8' and len(number) == 15):
            numbers_list.append(number)
            number = ''
    else:
        if len(number)<15:
            number = ''

for number in numbers_list:
    temp = number.split('-')
    if temp[1:] != temp_number[1:] and len(temp[1]) == 3 and 2 < len(temp[2]) < 5:
        print(number)
        temp_number = temp
"""
# Тимур: 7-ddd-ddd-dd-dd, Сослан: 8-ddd-dddd-dddd, Артур: 7-123-123-11-22,,,, Дима: 8-123-123-11-22, Анри: 8-123-1231-1221...... Гвидо: 7-123-1231-1221, 7-123-13-181-22, 8-1237-131-1221        



##############################  Модуль RE ###########################

# 1
"""
import sys
from re import search
for el in sys.stdin:
    match1 = search(r'(?P<w1>\d+)(\-|\s)?(?P<w2>\d+)(\-|\s)?(?P<w3>\d+)', el)
    res1, res2, res3 = match1.group('w1', 'w2', 'w3')
    print(f'Код страны: {res1}, Код города: {res2}, Номер: {res3}')

#1 877 2638277
#91-011-23413627
"""

# проверка пароля
"""
import sys
from re import fullmatch, search

for log in sys.stdin:
    match1 = fullmatch(r'(_)\d+[a-zA-Z]*\1?', log.strip('\n')) # обязательно убираем символ переноса строки
    if match1:
        print('True')
    else:
        print('False')    
       
# _123abc_
# _1abc_
# 123abc
# _abc123
# _123abc__
"""

# Одинаковые слоги
"""
import sys
from re import fullmatch

for word in sys.stdin:
    match = fullmatch(r'\b(\w+)(\w+)\1\2\b', word.strip('\n'))
    if match:
        print(word[match.start():match.end()])

"""

# Beegeek
"""
from re import search
import sys

sum_1 = 0
sum_2 = 0

for line in sys.stdin:
    match1 = search(r'bee.+bee', line)
    match2 = search(r'\bgeek\b', line)
    if match1:
        sum_1 +=1
    if match2:
        sum_2 +=1
print(sum_1, sum_2, sep = '\n')

#beebee bee
#beegeek
#bee geek bee
"""

# Популярность
"""
import sys
from re import search, fullmatch

res_sum = 0
for line in sys.stdin:
    match_3 = search(r'beegeek.*beegeek', line.strip('\n'))
    match_2_1 = search(r'^\s*beegeek\s*$', line.strip('\n'))
    match_2_2 = search(r'^\s*[^b].+beegeek\s*$', line.strip('\n'))
    match_2_3 = search(r'^\s*beegeek.+[^k]\s*$', line.strip('\n'))
    match_1 = search(r'^\s*.+beegeek.+\s*$', line.strip('\n'))

    if match_3:
        res_sum += 3
    elif match_2_1 or match_2_2 or match_2_3:
        res_sum += 2
    elif match_1:
        res_sum += 1
print(res_sum)

#hi, beegeek
#beegeek is an awesome place for programmers
#beegeek rocks, rocks beegeek
#i think beegeek is a great place to hangout
"""

#
"""
article = '''Stepik (до августа 2016 года Stepic) — это образовательная платформа и конструктор онлайн-курсов!

Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android. В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном режиме для iOS и Android...

На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
Stepik позволяет любому зарегистрированному пользователю создавать интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и разнообразные задачи с автоматической проверкой и моментальной обратной связью. 

Проект сотрудничает как с образовательными учреждениями, так и c индивидуальными преподавателями и авторами.  
Stepik сегодня предлагает онлайн-курсы от образовательных организаций, а также индивидуальных авторов!

Система автоматизированной проверки задач Stepik была использована в ряде курсов на платформе Coursera, включая курсы по биоинформатике от Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ «Высшая школа экономики»...

Stepik также может функционировать как площадка для проведения конкурсов и олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ (2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант в 2017 году, соревнования по информационной безопасности StepCTF-2015...'''

from re import findall, IGNORECASE
count1 = 0
count2 = 0
for line in article.split('\n'):
    
    match1 = findall(r'^(Stepik).*', line.strip('\n'), IGNORECASE)
    match2 = findall(r'(\.\.\.)$|(!)$', line.strip('\n'))
    if match1:
        count1 += 1
    if match2:
        count2 += 1
print(count1, count2, sep = '\n')  
"""     

# Абревиатура слов
"""
from re import findall

def abbreviate(phrase):
    match = findall(r'([A-Z]|\b[a-z])', phrase)
    if match:
        return ''.join(match).upper()
    
print(abbreviate('javaScript object notation'))    
"""

# Парсер
"""
from re import findall
import sys

for line in sys.stdin:
    match = findall(r'\.*<a href="(.+)">(.+)</a>\.*', line) 
    if match:
        url, text = match[0]
        print(url,text, sep=', ')


<div id="oldie-warning" class="do-not-print">
    <p>
        <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
        <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
    </p>
</div>        
"""

# HTML
"""
from re import findall, finditer
import sys
# загрузка данных из файла заданий N6
with open('D:/py_learning/py_programs/regular/html_test/6', encoding='utf-8') as data:
    res_dict = {}
    temp_list = []

    for line in data.readlines():
        match = finditer(r'(<[^/].*?>)', line)
        if match:
            for el in match:
                temp_res = el.group()
                match2 = findall(r'<(.*?)[>| ](.*)=?', temp_res)
                if match2:            
                    match3 = findall(r'([a-zA-Z-]+?)=', match2[0][1])
                    if res_dict.get(match2[0][0]) == None:  
                        if match3:
                            res_dict.setdefault(match2[0][0], sorted(match3))
                        else: 
                            res_dict.setdefault(match2[0][0], match2[0][1])
                    else:
                        temp_list = res_dict.get(match2[0][0])
                        if type(temp_list) == list:
                            if match3:
                                temp_list.extend(sorted(match3))
                                temp_list = set(temp_list)
                            res_dict.update([(match2[0][0], sorted(temp_list))])    
                            temp_list = [] 
                        else:
                            if match3:
                                res_dict.update([(match2[0][0], sorted(match3))])
                                
    for key in sorted(res_dict.keys()):
        print(key, ', '.join(res_dict.get(key)), sep = ': ')  
print()
# вызов файла проверки ответов
with open('D:/py_learning/py_programs/regular/html_test/6.clue', encoding='utf-8') as answers:
    for answer in answers:
        print(answer.strip('\n'))
"""       

#
"""
import keyword
from re import sub, IGNORECASE

input_text = input()

input_list = keyword.kwlist
for in_word in input_list:
    input_text = sub(fr'\b{in_word}\b', r'<kw>', input_text, flags=IGNORECASE)
print(input_text)   
# True, assert, as, false, or, Import
#
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

#
"""
from re import sub

def change(match_obj):
    s = match_obj.group()
    return s[::-1]
    
text = input()
res = sub(r'\b\w{2}', change, text)

print(res)
# This is Python
"""

# Умножение строк
"""
from re import sub, IGNORECASE

def change(match_obj):
    d = match_obj.group(1)
    t = match_obj.group(2)
    return t * int(d)


def math_res(text):
    while ')' in text:
        text = sub(r'(\d+)\(([a-z]+)\)', change, text, flags = IGNORECASE)
    return text

print(math_res('bbbb10(2(a))bbb'))
"""

# Повторяющиеся слова
"""
from re import sub

text = input()
text = sub(r'\b(\w+)(\W+\1\b)+', r'\g<1>', text)

print(text)

#beegeek,beegeek,beegeek! python python.. Python.. stepik?stepik?stepik
"""

# Удаление всевозможных комментариев из программы
"""
from re import sub, MULTILINE, DOTALL

def comments():
    with open('D:/py_learning/py_programs/regular/test_comments.txt', encoding='utf-8') as text: 
        line = sub(r'[ ]*(\"){3}(.*?)(\"){3}\n', r'', ''.join(text.readlines()), flags= DOTALL) 
        line = sub(r'^[ ]*#+ (.)*\n', r'', line, flags = MULTILINE) 
        line = sub(r'\.*  # (.)+', r'', line)   
    
        print(line)

comments()
"""

# Функция multiple_split()
"""
from re import split, escape

def format(symbols):
    if len(symbols)>1:
        return '|'.join([f'\\{el[0]}{{{len(el)}}}' for el in symbols])
    else:
        return f'{escape(symbols[0])}'

def multiple_split(string, delimiters):
    string = split(fr'{format(delimiters)}', string)
    return string    

print(multiple_split('beegeek-python.stepik', ['.', '-']))   
print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****'])) 
print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))
print(multiple_split('stepik_python-dima*roma*jenya-timur__arthur', ['_', '*', '#', '@']))
"""

#
"""
from functools import reduce
from re import compile

a, b = input().split(' ')
text = input()

red = compile(r'\d+')
re_obj = red.findall(text, pos = int(a), endpos = int(b))
if len(re_obj) > 0:
    res = reduce(lambda x, y: int(x)+int(y), re_obj)
else:
    res = 0

print(res)

# 0 5
#11:20 a.m. - 12:00 p.m
"""