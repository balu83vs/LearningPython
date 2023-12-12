from zipfile import ZipFile

FILE_DIR = 'D:\py_learning\py_programs\zip\files'

# Введение
"""
with ZipFile(f'{FILE_DIR}test.zip') as zipfile:
    zipfile.printdir()   
"""

# Количество файлов
"""
with ZipFile(f'{FILE_DIR}workbook.zip') as zipfile:
    info = zipfile.infolist()
    count = 0
    for i in range(len(info)):
        if info[i].is_dir() == False:
            count += 1
    print(count)        
"""

# Объем файлов
"""
with ZipFile(f'{FILE_DIR}workbook.zip') as zipfile:
    info = zipfile.infolist()
    non_compres_dicts = 0
    compres_dicts = 0

    for i in range(len(info)):
        if info[i].is_dir() == False:
            non_compres_dicts += info[i].file_size
            compres_dicts += info[i].compres_dicts_size
    print(f'Объем исходных файлов: {non_compres_dicts} байт(а)')
    print(f'Объем сжатых файлов: {compres_dicts} байт(а)') 
"""

# Наилучший показатель
"""
with ZipFile(f'{FILE_DIR}workbook.zip') as zipfile:    info = zipfile.infolist()
    temp_limit = 100
    temp = 0
    res_dict_name = ''
    for i in range(len(info)):
        if info[i].is_dir() == False:
            temp = info[i].compres_dicts_size / info[i].file_size * 100
            if temp < temp_limit:
                res_dict_name = info[i].filename.split('/')[-1]
                temp_limit = temp
    print(res_dict_name)
"""

# Избранные    
"""
from datetime import datetimewith ZipFile(f'{FILE_DIR}workbook.zip') as zipfile:
    test_date = datetime(2021, 11, 30, 14, 22, 00)
    info_files = sorted(zipfile.infolist(), key = lambda x: x.filename.split('/')[-1])    
    res_dict_list = list(filter(
                                lambda x: x.filename.split('/')[-1] 
                                    if datetime.strptime(str(x.date_time), "(%Y, %m, %d, %H, %M, %S)") > test_date 
                                    else None, 
                                info_files
                                )
                        )
    for el in res_dict_list:
        print(el.filename.split('/')[-1])    
"""

# Форматированный вывод    
"""
import json
from datetime import datetime

with ZipFile(f'{FILE_DIR}workbook.zip') as zipfile, 
    open(f'{FILE_DIR}workbook.json', 'w', encoding = 'utf-8') as json_out:

    info = zipfile.infolist()
    info = sorted(info, key = lambda x: x.filename.split('/')[-1])
    res_dict_dict = dict()

    for i in range(len(info)):
        if info[i].is_dir() is not True:
            res_dict_dict.setdefault(
                                    info[i].filename.split('/')[-1], 
                                    {'Дата модификации файла:': info[i].date_time, 
                                    'Объем исходного файла:': info[i].file_size, 
                                    'Объем сжатого файла:': info[i].compres_dicts_size}
                                    )
    json.dump(res_dict_dict, json_out, ensure_ascii = False, indent = 3) 

with open(f'{FILE_DIR}workbook.json', encoding = 'utf-8') as json_in:

    res_dict = json.load(json_in)

    for el in res_dict:
        print(el)
        print(f'  {list(res_dict[el].keys())[0]} {datetime.strptime(str(res_dict[el][list(res_dict[el].keys())[0]]), "[%Y, %m, %d, %H, %M, %S]")}')
        print(f'  {list(res_dict[el].keys())[1]} {res_dict[el][list(res_dict[el].keys())[1]]} байт(а)')
        print(f'  {list(res_dict[el].keys())[2]} {res_dict[el][list(res_dict[el].keys())[2]]} байт(а)')
        print()
"""

# запись в файл
"""
file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',              
                'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
                'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']

with ZipFile(f'{FILE_DIR}files.zip', mode='w') as zip_save:
    
    for el in file_names:
        ZipFile.write(zip_save, el)          
"""

# Функция extract_this()
"""
def extract_this(file_name, *files):
    with ZipFile(ff'{FILE_DIR}{file_name}') as zipfile:
    
        info = zipfile.infolist()

        if len(files) == 0:
            zipfile.extractall()
        else:
            for el in files:
                for i in range(len(info)):
                    if info[i].filename.split('/')[-1] == el:
                        zipfile.extract(info[i].filename) 

extract_this('workbook.zip', 'earth.jpg', 'exam.txt')
"""

# Шахматы были лучше
"""
import jsonres_list = []

def is_correct_json(string):
    try:
        type(json.loads(string))
        return True
    except:
        return False 

with ZipFile(f'{FILE_DIR}data.zip') as zipfile:

    file_list = zipfile.namelist()

    for name in file_list:
        with zipfile.open(name) as json_file:
            test = json_file.read()
            if is_correct_json(test): 
                test = test.decode('utf-8')
                res_list.append(json.loads(test))
            else:
                continue 
                     
for res_name in sorted(list(filter(lambda x: x if x['team'] == 'Arsenal' else None, res_list)), key = lambda x: x['first_name']):
    print(f'{res_name["first_name"]} {res_name["last_name"]}')
"""

# Структура архива
"""
def size(filesize):
    res = 0
    res2 = ''

    if filesize // (1024**3) >= 1:
        res = round(filesize / (1024**3))
        res2 = 'GB'
    elif filesize // (1024**2) >= 1:
        res = round(filesize / (1024**2))
        res2 = 'MB' 
    elif filesize // 1024 >= 1:
        res = round(filesize / 1024)
        res2 = 'KB'        
    else:
        res = filesize
        res2 = 'B'
    return res, res2

res_dict = dict()
det = ''
short_name = ''
temp_list = []

with ZipFile(f'{FILE_DIR}desktop.zip') as zipfile:

    info = zipfile.infolist()
    
    for el in info:
        short_name = el.filename.split('/')
        if el.is_dir() == True:
            det = '  ' * (len(short_name) - 2)
            print(f'{det}{short_name[-2]}')
        else:
            det = '  ' * (len(short_name) - 1)
            temp_list = size(el.file_size)
            print(f'{det}{short_name[-1]} {temp_list[0]} {temp_list[1]}')      
"""