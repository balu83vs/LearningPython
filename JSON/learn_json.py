import json

FILE_DIR = 'D:/py_learning/py_programs/JSON/files'

# 1
"""
countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

countries_json = json.loads(countries, separators = (',', ' - '), indent = 3, sort_keys = True)

print(countries_json)
"""


# 2
"""
words = {
         frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
         "travel": "trævl",
         ("hello", "world"): ("həˈləʊ", "wɜːld"),
         "moonlight": "muːn.laɪt",
         "sunshine": "ˈsʌn.ʃaɪn",
         ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
         "adventure": "ədˈventʃər",
         "beautiful": "ˈbjuːtɪfl",
         frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
         "bicycle": "baisikl",
         ("pilot", "fly"): ("pailət", "flai")
        }

data_json = json.loads(words, skipkeys = True)

print(data_json)
"""


# 3
"""
club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
         "trainer": "Julian Nagelsmann", "gaolkeeper": "M. Neuer", "league_position": 1}

club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
         "trainer": "Xavier Creus", "gaolkeeper": "M. Ter Stegen", "league_position": 7}

club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
         "trainer": "Michael Carrick", "gaolkeeper": "D. De Gea", "league_position": 8}

with open(f'{FILE_DIR}data.json', 'w', encoding = 'utf-8') as file:
    json.load([club1, club2, club3], file, indent = 3)
"""    


# Разные типы
"""
def mod(data):
    json_new_data = []

    for el in data:
        if type(el) == str:
            el += '!'
        elif type(el) == int:
            el += 1
        elif type(el) == dict:
            el.setdefault('newkey', None)
        elif type(el) == bool:
            el = not el     
        elif type(el) == list:
            el = el * 2
        else:
            continue    
            
        json_new_data.append(el)      
    return json_new_data                       

with open(f'{FILE_DIR}test_data.json', encoding = 'utf-8') as input_file, 
    open(f'{FILE_DIR}updated_data.json', 'w', encoding = 'utf-8') as output_file:
    json_data = json.load(input_file)
    json.load(mod(json_data), output_file)
"""    


# Объединение объектов
"""
with open(f'{FILE_DIR}data1.json', encoding = 'utf-8') as input1, 
    open(f'{FILE_DIR}data2.json', encoding = 'utf-8') as input2, 
    open(f'{FILE_DIR}data_merge.json', 'w', encoding = 'utf-8') as output:

    input_1 = json.load(input1)
    input_2 = json.load(input2)

    for el in input_2:
        if el in input_1:
            input_1[el] = input_2[el]
        else:
            input_1.setdefault(el, input_2[el])

    json.dump(input_1, output, sort_keys = True)
"""


# Объединение объектов
"""
with open(f'{FILE_DIR}people.json', encoding = 'utf-8') as input, 
    open(f'{FILE_DIR}updated_people.json', 'w', encoding = 'utf-8') as output:

    data = json.load(input)
    max_len = max(map(lambda x: len(x), data))
    
    for el in list(filter(lambda x: x if len(x) == max_len else None, data)):
        max_key_list = sorted(el.keys())
        break

    for dict_el in data:
        for el in max_key_list:
            dict_el.setdefault(el, None)

    json.dump(data, output)    
"""


# Я исповедую Python, а ты?
"""
with open(f'{FILE_DIR}countries.json', encoding = 'utf-8') as input, 
    open(f'{FILE_DIR}religion.json', 'w', encoding = 'utf-8') as output:

    data = json.load(input)

    temp_list = [y['country'] if y['religion'] == x else '_' for y in data]

    res_dict = {x: list(filter(lambda x: x if x != '_' else None, temp_list)) for x in set(el['religion'] for el in data)}

    json.dump(res_dict, output)
"""


# Спортивные площадки
"""
import csv

with open(f'{FILE_DIR}playgrounds.csv', encoding = 'utf-8') as input_csv,
    open(f'{FILE_DIR}addresses.json', 'w', encoding = 'utf-8') as output_json:

    data_list = list(csv.DictReader(input_csv, delimiter = ';'))
    res_dict = {adm['AdmArea']: None for adm in data_list}

    temp_dict = dict()

    for adm in res_dict:
        for dis in list(filter(lambda x: x['District'] if x['AdmArea'] == adm else None, data_list)):
    	    temp_dict.setdefault(dis['District'], None)

        res_dict[adm] = temp_dict
        temp_dict = dict()   

        for el2 in res_dict[adm]:
            res_dict[adm][el2] = [adm['Address'] for adm in list(filter(lambda x: x if x['District'] == el2 else None, data_list))]

    json.dump(res_dict, output_json, ensure_ascii = False)#, indent = 3)
"""


# Студенты курса
"""
import csv

with open(f'{FILE_DIR}students.json', encoding = 'utf-8') as input_json, 
    open(f'{FILE_DIR}data.csv', 'w', encoding = 'utf-8', newline = '') as output_csv:

    data_json = json.load(input_json)
    columns = ['name', 'phone']
    
    out_to_csv = csv.DictWriter(output_csv, delimiter=',', fieldnames = columns)
    out_to_csv.writeheader()

    res_list = filter(lambda x: map(x['name'], x) if (int(x['age']) >= 18 and int(x['progress']) >= 75) else None, data_json)
    res_list = list(sorted(res_list, key = lambda x: x['name']))

    for el in res_list:
        out_to_csv.writerow({'name': el['name'], 'phone': el['phone']})
"""


# Бассейны
"""
from datetime import time, datetime

with open(f'{FILE_DIR}pools.json', encoding = 'utf-8') as input_file:

    time1 = time(10, 00, 00)
    time2 = time(12, 00, 00)
    pools = json.load(input_file)

    res_list = list(filter(lambda x: x 
                                if datetime.strptime(x['WorkingHoursSummer']['Понедельник'].split('-')[0], '%H:%M').time() <= time1
                                    and datetime.strptime(x['WorkingHoursSummer']['Понедельник'].split('-')[1], '%H:%M').time() >= time2 
                                else None, pools
                            )
                    )

    res_list = sorted(res_list, key = lambda x: x['DimensionsSummer']['Length'], reverse = True)  
    max_lenght = res_list[0]['DimensionsSummer']['Length']  
    res_list = list(filter(lambda x: x if x['DimensionsSummer']['Length'] == max_lenght else None, res_list))
    max_wight = max([el['DimensionsSummer']['Width'] for el in res_list])
    res_list = list(filter(lambda x: x if x['DimensionsSummer']['Width'] == max_wight else None, res_list))

    print(f"{res_list[0]['DimensionsSummer']['Length']}x{res_list[0]['DimensionsSummer']['Width']}")
    print(res_list[0]['Address'])        
"""


# Результаты экзамена
"""
import csv
from datetime import datetime

with open(f'{FILE_DIR}exam_results.csv', encoding = 'utf-8') as csv_input, 
    open(f'{FILE_DIR}best_scores.json', 'w', encoding = 'utf-8') as json_output:

    csv_data = sorted(csv.DictReader(csv_input, delimiter = ','), key = lambda x: x['email'])
    res_dict = dict()

    for el in csv_data:
        res_dict.setdefault(el['email'], list(filter(lambda x: x if x['email'] == el['email'] else None, csv_data)))

    for el in res_dict:
        best_score = max([int(x['score']) for x in res_dict[el]])
        res_dict[el] = list(filter(lambda x: x if int(x['score']) == best_score else None, res_dict[el]))
        if len(res_dict[el]) > 1:
            res_dict[el] = sorted(res_dict[el], key = lambda x: datetime.strptime(x['date_and_time'], '%Y-%m-%d %H:%M:%S'), reverse = True)[0]     
            res_dict[el]['score'] = int(res_dict[el]['score'])  
        else:
            res_dict[el] = res_dict[el][0]
            res_dict[el]['score'] = int(res_dict[el]['score'])

    res_list = [dict(zip(['name', 'surname', 'best_score', 'date_and_time', 'email'], el.values())) for el in res_dict.values()]

    json.dump(res_list, json_output, indent = 3)      
"""    


# Общественное питание
"""
with open(f'{FILE_DIR}food_services.json', encoding = 'utf-8') as input_json:

    input_data = json.load(input_json)
    temp_list = list()
    temp_list2 = list()
    res_list = list()

    temp_list = [el['District'] for el in input_data]

    for el in set(temp_list):
        res_list.append((el, temp_list.count(el)))

    print(f'{sorted(res_list, key = lambda x: x[1], reverse = True)[0][0]}: {sorted(res_list, key = lambda x: x[1], reverse = True)[0][1]}')

    res_list = []
        
    temp_list = [el['OperatingCompany'] for el in list(filter(lambda x: x if x['IsNetObject'] == 'да' else None, input_data))]

    for el in set(temp_list):
        res_list.append((el, temp_list.count(el)))

    print(f'{sorted(res_list, key = lambda x: x[1], reverse = True)[0][0]}: {sorted(res_list, key = lambda x: x[1], reverse = True)[0][1]}')
"""


# Общественное питание 2
"""
temp_list = list()

with open(f'{FILE_DIR}food_services2.json', encoding = 'utf-8') as input_json:

   input_data = json.load(input_json)

   for obj in sorted(list(set([el['TypeObject'] for el in input_data]))):
        temp_list = [(el['Name'], el['SeatsCount'])  for el in list(filter(lambda x: x if x['TypeObject'] == obj else None, input_data))]  
        temp_list = list(sorted(temp_list, key = lambda x: x[1])[-1])
        print(f'{obj}: {temp_list[0]}, {temp_list[1]}')        
"""        