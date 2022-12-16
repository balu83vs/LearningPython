# 1
"""
import json

countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

countries_json = json.loads(countries, separators = (',', ' - '), indent = 3, sort_keys = True)

print(countries_json)
"""

# 2
"""
import json

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
import json

club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
         "trainer": "Julian Nagelsmann", "gaolkeeper": "M. Neuer", "league_position": 1}

club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
         "trainer": "Xavier Creus", "gaolkeeper": "M. Ter Stegen", "league_position": 7}

club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
         "trainer": "Michael Carrick", "gaolkeeper": "D. De Gea", "league_position": 8}

with open('d:/py_learning/py_programs/JSON/data.json', 'w', encoding = 'utf-8') as file:
    json.load([club1, club2, club3], file, indent = 3)
"""    

# Разные типы
"""
import json

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



with open('d:/py_learning/py_programs/JSON/test_data.json', encoding = 'utf-8') as input_file, open('d:/py_learning/py_programs/JSON/updated_data.json', 'w', encoding = 'utf-8') as output_file:
    json_data = json.load(input_file)
    json.load(mod(json_data), output_file)
"""    

# Объединение объектов
"""
import json

with open('d:/py_learning/py_programs/JSON/data1.json', encoding = 'utf-8') as input1, open('d:/py_learning/py_programs/JSON/data2.json', encoding = 'utf-8') as input2, open('d:/py_learning/py_programs/JSON/data_merge.json', 'w', encoding = 'utf-8') as output:
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
import json

with open('d:/py_learning/py_programs/JSON/people.json', encoding = 'utf-8') as input, open('d:/py_learning/py_programs/JSON/updated_people.json', 'w', encoding = 'utf-8') as output:
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
import json

with open('D:/py_learning/py_programs/JSON/countries.json', encoding = 'utf-8') as input, open('D:/py_learning/py_programs/JSON/religion.json', 'w', encoding = 'utf-8') as output:
    data = json.load(input)

    res_dict = {x: list(filter(lambda x: x if x != '_' else None, [y['country'] if y['religion'] == x else '_' for y in data])) for x in set(el['religion'] for el in data)}

    json.dump(res_dict, output)
"""

# Спортивные площадки
"""
import csv
import json

with open('D:/py_learning/py_programs/JSON/playgrounds.csv', encoding = 'utf-8') as input_csv, \
    open('D:/py_learning/py_programs/JSON/addresses.json', 'w', encoding = 'utf-8') as output_json:
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