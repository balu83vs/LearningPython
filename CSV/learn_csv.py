import csv

FILE_DIR = 'd:/py_learning/py_programs/csv/files/'

# Скидки
"""
with open(f'{FILE_DIR}sales.csv', encoding = 'utf-8') as file:
    data = csv.DictReader(file, delimiter=';')
    data = list(filter(lambda x: x if int(x['old_price']) > int(x['new_price']) else None, data))
    for el in data:
        print(el['name'])
"""


# Средняя зарплата
"""
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
    
with open(f'{FILE_DIR}salary_data.csv', encoding = 'utf-8') as file:
    data = csv.DictReader(file, delimiter = ';')     
    data = sorted(data, key = lambda x: x['company_name'])
    print(*midle_salary(data), sep = '\n')     
"""        


# Функция csv_columns()
"""
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

print(csv_columns(f'{FILE_DIR}test.csv'))
"""


# Популярные домены
"""
with open(f'{FILE_DIR}data.csv', encoding = 'utf-8') as input_file, 
     open(f'{FILE_DIR}domain_usage.csv', 'w', encoding = 'utf-8', newline = '') as output_file:
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
temp_dict = {}
temp_list = []

with open(f'{FILE_DIR}wifi.csv', encoding='utf-8') as file:
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
    file = open(f'{FILE_DIR}titanic.csv',  encoding = 'utf-8')
    passengers = csv.DictReader(file, delimiter = ';')
    return passengers    

male_pass = list(filter(lambda pas: pas if (
                                            pas['survived'] == '1' 
                                            and pas['sex'] == 'male' 
                                            and float(pas['age']) < 18
                                            ) 
                                        else None, file_load()
                        )
                )
female_pass = list(filter(lambda pas: pas if (
                                             pas['survived'] == '1' 
                                             and pas['sex'] == 'female' 
                                             and float(pas['age']) < 18
                                             ) 
                                        else None, file_load()
                        )
                )

for pas in male_pass:
    print(pas['name'])
for pas in female_pass:
    print(pas['name'])  
"""


# Лог-файл
"""
from datetime import datetime

temp_list = []
temp_email_list = []
res_list = []
columns = ['username', 'email', 'dtime']

with open(f'{FILE_DIR}name_log.csv', encoding = 'utf-8') as input_file, 
     open(f'{FILE_DIR}new_name_log.csv', 'w', encoding = 'utf-8', newline = '') as output_file:
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
with open(f'{FILE_DIR}deniro.csv', encoding = 'utf-8') as file:
    data_list = [el.strip('\n').split(',') for el in file.readlines()]
    choice = int(input())

    data_list.sort(key = lambda x: int(x[choice - 1]) if x[choice - 1].isdigit() else x[choice - 1])

    for el in data_list:
        print(f'{el[0]},{el[1]},{el[2]}')
"""


# Проще, чем кажется
"""
def condense_csv(filename, id_name):

    temp_dict = {}
    res_list = []
    columns = []

    with open(filename, encoding = 'utf-8') as input_file, 
         open(f'{FILE_DIR}condensed.csv', 'w', encoding = 'utf-8', newline = '') as output_file:
        data = [el.strip('\n').split(',') for el in input_file.readlines()]
        columns.append(id_name)
        data.sort(key = lambda x: x[0])
        temp_name = data[0][0]
        
        for el in data:
            if el[1] not in columns:
                columns.append(el[1])
            if el[0] == temp_name:
                temp_dict.setdefault(id_name, temp_name)
                temp_dict.setdefault(el[1], el[2])
                temp_name = el[0]
            else:
                res_list.append(temp_dict)
                temp_dict = {}
                temp_dict.setdefault(id_name, el[0])
                temp_dict.setdefault(el[1], el[2])
                temp_name = el[0]
        res_list.append(temp_dict)

        output_data = csv.DictWriter(output_file, delimiter = ',', fieldnames = columns)
        output_data.writeheader()

        for el in res_list:
            output_data.writerow(el)    

filename = f'{FILE_DIR}data2.csv'            
id_name = 'object'

condense_csv(filename, id_name)
"""


# Возрастание классов
"""
with open(f'{FILE_DIR}student_counts.csv', encoding = 'utf-8') as input_file, 
     open(f'{FILE_DIR}sorted_student_counts.csv', 'w', encoding = 'utf-8', newline = '') as output_file:
    data_list = [el for el in csv.DictReader(input_file, delimiter = ',')]
    columns = list(data_list[0].keys())
    new_columns = columns[0:1]
    new_columns.extend(sorted(sorted(columns[1:]), key = lambda x: int(x.split('-')[0])))
    res_file = csv.DictWriter(output_file, delimiter = ',', fieldnames = new_columns)
    res_file.writeheader()
    for el in data_list:
        res_file.writerow(el)
"""


# Голодный студент  # ???
"""
res_dict = {}
win_list = []

with open(f'{FILE_DIR}prices.csv', encoding = 'utf-8') as file:
    data = csv.DictReader(file, delimiter = ';')

    for el in data:
        temp_key = el.pop('Магазин')
        res_dict.setdefault(temp_key, 
                            [list(filter(lambda x: x if int(el[x]) == min([int(el[x]) for x in el]) else None, el))[0], 
                            el[list(filter(lambda x: x if int(el[x]) == min([int(el[x]) for x in el]) else None, el))[0]]]
                            )

win_list = list(filter(lambda x: x if int(res_dict[x][1]) == min([int(res_dict[el][1]) for el in res_dict]) else None, res_dict))

print(f'{res_dict[win_list[0]][0]}: {win_list[0]}')
"""
