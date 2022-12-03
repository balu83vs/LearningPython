# Скидки
"""
import csv

with open('d:/py_learning/py_programs/csv/sales.csv', encoding = 'utf-8') as file:
    data = csv.DictReader(file, delimiter=';')
    data = list(filter(lambda x: x if int(x['old_price']) > int(x['new_price']) else None, data))
    for el in data:
        print(el['name'])
"""

# Средняя зарплата
"""
import csv
from statistics import mean

def midle_salary(data):
    temp_list = []
    res_dict = dict()
    temp_name = data[0]['company_name']
    for el in data:
        if el['company_name'] == temp_name:
            temp_list.append(int(el['salary']))
        else: 
            res_dict.setdefault(temp_name, int(mean(temp_list)))
            temp_list = []
            temp_list.append(int(el['salary']))
            temp_name = el['company_name'] 
    res_dict.setdefault(temp_name, int(mean(temp_list)))
    res_dict = sorted(res_dict, key = lambda x: int(res_dict.get(x)))  

    return res_dict
    

with open('d:/py_learning/py_programs/csv/salary_data.csv', encoding = 'utf-8') as file:
    data = csv.DictReader(file, delimiter = ';')     
    data = sorted(data, key = lambda x: x['company_name'])
    print(*midle_salary(data), sep = '\n')     
"""        

# Функция csv_columns()
"""
import csv

def csv_columns(file_dir):
    with open(file_dir, encoding = 'utf-8') as file:
        data = csv.DictReader(file, delimiter = ',')
        temp_dict = {}    
        temp_list = []
        res_list = []
        for el in data:
            for el2 in list(el):
                temp_dict.setdefault(el2)  
                temp_list.append(el[el2])    
        for j in range(len(el)):
            for i in range(j, len(temp_list), len(el)):
                res_list.append(temp_list[i])
            temp_dict[list(temp_dict.keys())[j]] = res_list    
            res_list = []    
    return temp_dict   

print(csv_columns('d:/py_learning/py_programs/csv/test.csv'))
"""

# Популярные домены
"""
import csv

with open('d:/py_learning/py_programs/csv/data.csv', encoding = 'utf-8') as input_file, open('d:/py_learning/py_programs/csv/domain_usage.csv', 'w', encoding = 'utf-8', newline = '') as output_file:
    temp_list = []
    columns = ['domain', 'count']
    input_data = csv.DictReader(input_file, delimiter = ',')  
    output_data = csv.DictWriter(output_file, fieldnames = columns, delimiter = ',')
    output_data.writeheader()
    for el in input_data:
        temp_list.append(el['email'].split('@')[1])
    domens_list = list(set(temp_list))
    count_list = [temp_list.count(el) for el in domens_list]
    res_list = [{columns[0]: domens_list[i], columns[1]: count_list[i]} for i in range(len(domens_list))]
    res_list = sorted(res_list, key = lambda x: x[columns[0]])
    res_list = sorted(res_list, key = lambda x: x[columns[1]])   
    for el in res_list:
        output_data.writerow(el)
"""        

# Wi-Fi Москвы
"""
import csv
temp_dict = {}
temp_list = []

with open('d:/py_learning/py_programs/csv/wifi.csv', encoding='utf-8') as file:
    data = file.read()
    table = [[r.split(';')[1], r.split(';')[3]] for r in data.splitlines()]
    del table[0]   
    table = sorted(table, key = lambda x: x[0])#.strip('район '))                                   
    for el in table:
        temp_dict.setdefault(el[0])
    for el in temp_dict:
        for el2 in table:
            if el2[0] == el:
                temp_list.append(int(el2[1]))    
        temp_dict[el] = sum(temp_list)
        temp_list = []   
    for block in sorted(temp_dict, key = lambda x: temp_dict[x], reverse = True):
        print(f'{block}: {temp_dict[block]}')    
"""

# Последний день на Титанике
"""
def file_load():
    import csv
    file = open('d:/py_learning/py_programs/csv/titanic.csv',  encoding = 'utf-8')
    passengers = csv.DictReader(file, delimiter = ';')
    return passengers    

male_pass = list(filter(lambda pas: pas if (pas['survived'] == '1' and pas['sex'] == 'male' and float(pas['age']) < 18) else None, file_load()))
female_pass = list(filter(lambda pas: pas if (pas['survived'] == '1' and pas['sex'] == 'female' and float(pas['age']) < 18) else None, file_load()))


for pas in male_pass:
    print(pas['name'])
for pas in female_pass:
    print(pas['name'])  
"""

# Лог-файл
"""
import csv
from datetime import datetime

temp_list = []
temp_email_list = []
res_list = []
columns = ['username', 'email', 'dtime']

with open('d:/py_learning/py_programs/csv/name_log.csv', encoding = 'utf-8') as input_file, open('d:/py_learning/py_programs/csv/new_name_log.csv', 'w', encoding = 'utf-8', newline = '') as output_file:
    log_file = [el for el in csv.DictReader(input_file, delimiter = ',')]

    new_log_file = csv.DictWriter(output_file, fieldnames = columns, delimiter = ',')
    new_log_file.writeheader()

    for el in log_file:
        if el[columns[1]] not in temp_email_list:
            temp_email = el[columns[1]]
        else:
            continue
        temp_list = list(filter(lambda x: x if x['email'] == temp_email else None, log_file))
        temp_list.sort(key = lambda x: datetime.strptime(x['dtime'], '%d/%m/%Y %H:%M'), reverse = True)
        res_list.append(temp_list[0])
        temp_email_list.append(temp_email)
        temp_list = []
    res_list = sorted(res_list, key = lambda x: x['email'])

    for el in res_list:
        new_log_file.writerow(el)
"""

# Сортировка по столбцу
"""
with open('d:/py_learning/py_programs/csv/deniro.csv', encoding = 'utf-8') as file:
    data_list = [el.strip('\n').split(',') for el in file.readlines()]
    choice = int(input())

    data_list.sort(key = lambda x: int(x[choice - 1]) if x[choice - 1].isdigit() else x[choice - 1])

    for el in data_list:
        print(f'{el[0]},{el[1]},{el[2]}')
"""

# Проще, чем кажется
