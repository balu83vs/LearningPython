import pickle
import operator

#1
"""
obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}

# запись сериализованного бинарного представления в файл
with open('D:/py_learning/py_programs/collections/files/file.pkl', 'wb') as file:
    pickle.dump(obj, file)                                          

# используется файл полученный на предыдущем шаге    
with open('D:/py_learning/py_programs/collections/files/file.pkl', 'rb') as file:
    obj = pickle.load(file)
    print(obj)
    print(type(obj))    
"""    


# filter_dump()
""" 
def filter_dump(filename, objects, typename):                                
    # функция генерации pickle-файла
    res = list(filter(lambda x: x if type(x) is typename else None, objects))
    with open(f'D:/py_learning/py_programs/{filename}', 'wb') as pi_file:
        pickle.dump(res, pi_file)

filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)                                            # запуск функции

with open('D:/py_learning/py_programs/collections/files/numbers.pkl', 'rb') as file:            # десереализация содержимого файла
    print(pickle.load(file))
"""


# Контрольная сумма
"""
with open(input(), 'rb') as pi_file:
    obj = pickle.load(pi_file)
    if type(obj) is dict:
        filter_list = list(filter(lambda x: x if type(x) == int else None, obj.keys()))
        if len(filter_list) == 0:
            test_sum = 0
        else:    
            test_sum = sum(filter_list)
    else:
        filter_list = list(filter(lambda x: x if type(x) == int else None, obj))
        if len(filter_list) == 0:
            test_sum = 0
        else:
            test_sum = max(filter_list) * min(filter_list)
    print('Контрольные суммы не совпадают' if test_sum != int(input()) else 'Контрольные суммы совпадают')
"""