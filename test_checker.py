################### Импорт файла с программой ###################
from itertools_test import test

################### Основное тело программы ####################
from zipfile import ZipFile

def checker(zip_file_name):
    code_list = []
    answers_list = []
    with ZipFile(f'D:/Downloads/{zip_file_name}.zip') as zip_file:
        file_list = zip_file.infolist()     
        for i in range(len(file_list)):
            with zip_file.open(file_list[i].filename) as data_file:
                data_file = data_file.read().decode('utf-8')
                if (i+1)%2 != 0:
                    code_list.append(''.join(data_file))
                else:
                    answers_list.append(''.join(data_file))
    return zip(code_list, answers_list)

################### Код проверки #####################

codes = checker(input())
count = 1
for code in codes:
    print('Ответ из программы:')
    exec(code[0])
    print(f'Ответ из условия № {count}:') 
    print(code[1])
    print()
    count += 1