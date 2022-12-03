# Раздел Date и Time

# Дневник космонавта
"""
from datetime import datetime

with open('diary.txt', encoding = 'utf-8') as diary_file:
    temp = ' '
    temp_value = []
    res_key = []
    res_value = []
    res_dict = dict()
    while len(temp) != 0:
        temp = diary_file.readline()
        temp_str = temp.strip()

        try: 
            res_key.append(datetime.strptime(temp_str, '%d.%m.%Y; %H:%M'))
        except ValueError:
            if len(temp_str) > 2:
                temp_value.append(temp_str)
            else:
                res_value.append(temp_value)                                     
                temp_value = []

    res_dict = dict(zip(res_key[0:len(res_key)], res_value[0:len(res_value)]))
    list_value = sorted(res_dict, key = lambda x: x.timestamp())

    for i in range(len(list_value)):
        print(list_value[i].strftime('%d.%m.%Y; %H:%M'))
        print(*res_dict[list_value[i]], sep = '\n')
        if i != len(list_value) - 1:
            print()
"""

# Функция is_available_date()
"""
from datetime import datetime

def is_available_date(dates, some_date):
    stop_num = []
    in_date = []

    stop_date = [el.split('-') for el in dates]    
    
    for el in stop_date:
        el = list(map(lambda x: str(int(datetime.strptime(x, '%d.%m.%Y').timestamp())), el))
        stop_num.append(el)     

    in_date = some_date.split('-')
    in_num = [str(int(datetime.strptime(el, '%d.%m.%Y').timestamp())) for el in in_date]    

    for stop_el in stop_num:
        if len(stop_el) == 1:
            if len(in_num) == 1:
                if int(in_num[0]) == int(stop_el[0]):
                    return False
            else:    
                if int(in_num[0]) <= int(stop_el[0]) <= int(in_num[1]):
                    return False
        else:
            if len(in_num) == 1:
                if int(stop_el[0]) <= int(in_num[0]) <= int(stop_el[1]):
                    return False
            else: 
                if set(list(i for i in range(int(in_num[0]), int(in_num[1]) + 86400, 86400))).intersection(set(list(i for i in range(int(stop_el[0]), int(stop_el[1]) + 86400, 86400)))):
                    return False
    return True
"""

## Раздел TimeDelta

# Таймер 
"""
from datetime import datetime, timedelta

date = datetime.strptime(input(), '%H:%M:%S')

delta = timedelta(seconds = int(input()))

time = date + delta

if len(str(time.hour)) < 2:
    print(f'0{timedelta(hours = time.hour, minutes = time.minute, seconds = time.second)}')
else:
    print(timedelta(hours = time.hour, minutes = time.minute, seconds = time.second))
"""

# Функция num_of_sundays()
"""
from datetime import datetime, timedelta

def num_of_sundays(year):
    time = datetime(year = year, month = 1, day = 1)

    delta = timedelta(days = 1)
    count = 0
    temp = time.year
    while time.year != int(temp) + 1:
        if time.strftime('%A') == 'Sunday':
            count +=1
        time += delta
    return count
"""

# Продуктивность
"""
from datetime import datetime, timedelta

date = datetime.strptime(input(), '%d.%m.%Y')

delta = timedelta(days = 1)
temp = date
print(temp.strftime('%d.%m.%Y'))

for i in range(2, 11): 
    temp = date + delta * i
    print(temp.strftime('%d.%m.%Y'))
    date = temp
"""

# Соседние даты
"""
from datetime import datetime, timedelta

temp_list = []
list_date = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y').toordinal(), input().split(' ')))
temp = list_date[0]

for i in range(1, len(list_date)):
    temp_list.append(abs(list_date[i] - temp))
    temp = list_date[i]
print(temp_list)
"""

# Функция fill_up_missing_dates()
"""
from datetime import datetime, timedelta

def fill_up_missing_dates(dates):
    res_list = []
    list_date = [datetime.strptime(el, '%d.%m.%Y') for el in dates]
    delta = timedelta(days = 1)
    max_date = max(list_date)
    min_date = min(list_date)
    while min_date <= max_date:
        res_list.append(min_date.strftime('%d.%m.%Y'))
        min_date += delta
    return res_list
"""

# Реп по матеше
"""
from datetime import datetime, timedelta

time_start = datetime.strptime(input(), '%H:%M')
time_end = datetime.strptime(input(), '%H:%M')
delta_45 = timedelta(seconds = 45 * 60)
delta_10 = timedelta(seconds = 10 * 60)
temp1 = time_start  
for i in range(1, 100):
    temp2 = temp1 + delta_45
    if temp1 + delta_45 <= time_end:
        print(f"{temp1.strftime('%H:%M')} - {temp2.strftime('%H:%M')}")
        temp1 = temp2 + delta_10
    else:
        print()
        break
"""


## РЕШЕНИЕ ЗАДАЧ
# 1-я
"""
from datetime import date, time, datetime, timedelta
from functools import reduce

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]      

res_list = reduce(lambda x, y: x + y, [timedelta(minutes = 60 * datetime.strptime(el[1], '%H:%M').hour + datetime.strptime(el[1], '%H:%M').minute).total_seconds() - 
            timedelta(minutes = 60 * datetime.strptime(el[0], '%H:%M').hour + datetime.strptime(el[0], '%H:%M').minute).total_seconds()
            for el in data])

print(int(res_list//60))
"""

# Пятница, 13-е
"""
from datetime import datetime, timedelta

week = [0 for i in range(0,7)]

start_date = datetime.strptime ('01.01.0001', '%d.%m.%Y')
finish_date = datetime.strptime ('31.12.9999', '%d.%m.%Y')
delta = timedelta(days = 1)

while start_date < finish_date:
    if start_date.day == 13:
        week[int(start_date.strftime('%w')) - 1] += 1
    start_date += delta

for day in week:
    print(day)
"""

# Снова не успел
"""
from datetime import datetime, timedelta

date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
work_time = {0: ('10:00', '18:00'), 1: ('9:00', '21:00'), 2: ('9:00', '21:00'), 3: ('9:00', '21:00'), 4: ('9:00', '21:00'), 5: ('9:00', '21:00'), 6: ('10:00', '18:00')}

left = datetime.strptime(work_time[int(date.strftime('%w'))][0], '%H:%M')
left_limit = timedelta(hours = left.hour, minutes = left.minute)

right = datetime.strptime(work_time[int(date.strftime('%w'))][1], '%H:%M')
right_limit = timedelta(hours = right.hour, minutes = right.minute)

enter_time = timedelta(hours = date.hour, minutes = date.minute)

if left_limit <= enter_time < right_limit:
    print(int((right_limit - enter_time).seconds/60))
else:
    print('Магазин не работает')
"""

# Самое понятное условие
"""
from datetime import datetime, timedelta

start_date = datetime.strptime(input(), '%d.%m.%Y')
finish_date = datetime.strptime(input(), '%d.%m.%Y')
delta = timedelta(days = 1)
delta3 = timedelta(days = 1) * 3

while int(start_date.day + start_date.month) % 2 == 0:
    start_date += delta
    
while start_date <= finish_date + delta:
    if start_date.strftime('%w') not in '14' and start_date <= finish_date:         
        print(start_date.strftime('%d.%m.%Y'))
    start_date += delta3
"""

# Сотрудники организации
"""
from datetime import datetime, timedelta

empl_list = []
count = 1
temp = ''

n = int(input())
for _ in range(n):
    empl_list.append(input().split())

empl_list = sorted(empl_list, key = lambda x: datetime.strptime(x[2], '%d.%m.%Y').timestamp())

for el in empl_list:
    if el[2] in temp:
        count +=1
    temp = el[2]
        
if count == 1:  
    print(f'{empl_list[0][2]} {empl_list[0][0]} {empl_list[0][1]}')
else:
    print(f'{empl_list[0][2]} {count}')
"""

# Сотрудники организации 2
"""
from datetime import datetime, timedelta

date_list = [datetime.strptime(input().split()[2],'%d.%m.%Y') for _ in range(int(input()))]
date_filter = set(date_list)
date_res = {date: date_list.count(date) for date in date_filter}
date_res = sorted(list(filter(lambda x: date_res.get(x) == max(date_res.values()), date_res)))
for el in date_res:
    print(el.strftime('%d.%m.%Y'))
"""

# Сотрудники организации 3
"""
from datetime import datetime, timedelta

now = datetime.strptime(input(), '%d.%m.%Y')
delta7 = timedelta(days = 7)
delta0 = timedelta(days = 0) 
delta358 = timedelta(days = 358)
year_list = []

temp_list = [input().split() for _ in range(int(input()))]

em_dict = {datetime.strptime(el[2], '%d.%m.%Y').year: None for el in temp_list}
years_temp_list = sorted(em_dict, reverse = True)

for el in em_dict:
    temp_list2 = list(filter(lambda x: x if datetime.strptime(x[2], '%d.%m.%Y').year == el and (delta0 < datetime.strptime(x[2], '%d.%m.%Y').replace(year=now.year) - now <= delta7 or datetime.strptime(x[2], '%d.%m.%Y').replace(year=now.year) - now < -delta358) else None, temp_list))
   
    em_dict[el] = temp_list2
    temp_list2 = []

for el_year in years_temp_list:
    if em_dict[el_year] != []:
        year_list = el_year
        break 

if year_list == []:
    print('Дни рождения не планируются')
else:   
    em_list = list(filter(lambda x: x if delta0 < datetime.strptime(x[2], '%d.%m.%Y').replace(year=now.year) - now <= delta7 or datetime.strptime(x[2], '%d.%m.%Y').replace(year=now.year) - now < -delta358 else None, em_dict[year_list]))
    em_list = sorted(em_list, key = lambda x: datetime.strptime(x[2], '%d.%m.%Y'))
    if len(em_list) != 0:
        print(f'{em_list[0][0]} {em_list[0][1]}')
    else:
        print('Дни рождения не планируются')
"""

# FAKE NEWS
"""
from datetime import datetime, timedelta
DAY_VAR = ('день', 'дня', 'дней')
HOUR_VAR = ('час', 'часа', 'часов')
MIN_VAR = ('минута', 'минуты', 'минут')

def choose_plural(result_input, var_input):
    if result_input > 0:
        if len(str(result_input)) < 2:
            if str(result_input)[-1] in '1':
                return '{0} {1}'.format(result_input, var_input[0])
            elif str(result_input)[-1] in '234':
                return '{0} {1}'.format(result_input, var_input[1])

        else:
            if str(result_input)[-1] in '1' and str(result_input)[-2] not in '1':
                return '{0} {1}'.format(result_input, var_input[0])
            elif str(result_input)[-1] in '234' and str(result_input)[-2] not in '1':
                return '{0} {1}'.format(result_input, var_input[1])

        return '{0} {1}'.format(result_input, var_input[2])  
    else:
        return     
    
def ded_l(dead_line, now_date):
    return dead_line - now_date
    
    
dead_line = datetime(year=2022, month = 11, day = 8, hour = 12, minute = 0)
now_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')


result_input = ded_l(dead_line, now_date)

if result_input.total_seconds() > 0:

    result_input_days = int(result_input.days)
    result_input_hours = int((result_input.seconds / 60) // 60)
    result_input_minutes = int(result_input.seconds / 60 - result_input_hours * 60)

    DAY_VAR = choose_plural(result_input_days, DAY_VAR)
    HOUR_VAR = choose_plural(result_input_hours, HOUR_VAR)
    MIN_VAR = choose_plural(result_input_minutes, MIN_VAR)

    print('До выхода курса осталось:', end = ' ')

    if DAY_VAR != None:
        if HOUR_VAR == None and MIN_VAR == None: 
            print(DAY_VAR, end = ' ')
        else:
            print(DAY_VAR, end = ' и ')
    
    if HOUR_VAR != None:
        if MIN_VAR == None or (DAY_VAR == None and MIN_VAR == None) or (DAY_VAR != None and HOUR_VAR != None): 
            print(HOUR_VAR, end = ' ')
        else:
            print(HOUR_VAR, end = ' и ')
    
    if MIN_VAR != None:
        if DAY_VAR == None or HOUR_VAR == None or (DAY_VAR == None and HOUR_VAR == None):
            print(MIN_VAR)
                
else:
    print('Курс уже вышел!')
"""


## модуль calendar
# Функция get_days_in_month()
"""
import calendar

from datetime import date

def get_days_in_month(year, month):
    months_list = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    day_num = calendar.monthrange(year, months_list.index(month))
    res_list = [date(year = year, month = months_list.index(month), day = i) for i in range(1, day_num[1] + 1)]
    return res_list
"""

# Функция get_all_mondays()
"""
import calendar

from datetime import date, timedelta


def get_all_mondays(year):
    delta = timedelta(days = 1)
    start_date = date(year = year, month = 1, day = 1)
    end_date = date(year = year, month = 12, day = 31)
    res_list = list()
    while start_date <= end_date:
        if calendar.weekday(start_date.year, start_date.month, start_date.day) == 0:
            res_list.append(start_date)
        start_date = start_date + delta
    return res_list
"""

# ТЧМ
"""
import calendar

from datetime import date, timedelta

year = int(input())

def get_all_mondays(year):
    delta = timedelta(days = 1)
    start_date = date(year = year, month = 1, day = 1)
    end_date = date(year = year, month = 12, day = 31)
    res_list = list()
    thursday_count = 0
    while start_date <= end_date:

        if calendar.weekday(start_date.year, start_date.month, start_date.day) == 3:
            thursday_count += 1
            if thursday_count == 3:        
                res_list.append(start_date)
                if start_date.month != 12:
                    start_date = date(year = start_date.year, month = start_date.month + 1, day = 1)
                else:
                    break
                thursday_count = 0
                if calendar.weekday(start_date.year, start_date.month, start_date.day) == 3:
                    thursday_count += 1
        start_date = start_date + delta
    return res_list

for el in get_all_mondays(year):
    print(el.strftime('%d.%m.%Y'))
"""