                                                                                              # программа для определения правильности бронирования

from datetime import datetime

def is_available_date(dates, some_date):                                                      # основная функция
    stop_num = []
    in_date = []

    stop_date = [el.split('-') for el in dates]                                               # заполняем список значений занятых дат
    
    for el in stop_date:
        el = list(map(lambda x: str(int(datetime.strptime(x, '%d.%m.%Y').timestamp())), el))  # создание списка занятых дат в представлении timestamp
        stop_num.append(el)     

    in_date = some_date.split('-')                                                            # список желаемых дат бронирования
    in_num = [str(int(datetime.strptime(el, '%d.%m.%Y').timestamp())) for el in in_date]      # список желаемых дат в представлении  timestamp

    for stop_el in stop_num:                                                                  # главный цикл блока проверки
        if len(stop_el) == 1:
            if len(in_num) == 1:
                if int(in_num[0]) == int(stop_el[0]):                                         # если списки бронирования и желаемых дат состоят из одной записи
                    return False
            else:    
                if int(in_num[0]) <= int(stop_el[0]) <= int(in_num[1]):                       # если дата бронирования одна, а список желаемых - диапазон
                    return False
        else:
            if len(in_num) == 1:
                if int(stop_el[0]) <= int(in_num[0]) <= int(stop_el[1]):                      # если желаемая дата одна, а даты бронирования - диапазон
                    return False
            else:                                                                             # оба списка - состоят из диапазонов дат
                if set(list(i for i in range(int(in_num[0]), int(in_num[1]) + 86400, 86400))).intersection(set(list(i for i in range(int(stop_el[0]), int(stop_el[1]) + 86400, 86400)))):
                                                                                              # проверка условия пересечения двух множеств, составленных на основе списков бронирования и желаемых дат
                    return False
    return True
    
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']        # входные условия
some_date = '22.11.2021-25.11.2021'
print(is_available_date(dates, some_date))                                                    # вызов основной функции
