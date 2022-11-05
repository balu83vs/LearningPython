from datetime import date, datetime

def is_available_date(dates, some_date):
    temp = []
    temp2 = []
    temp3 = []
    temp4 = []
    for el in dates:
        temp.append(el.split('-'))
    
    for el in temp:
        el = list(map(lambda x: str(int(datetime.strptime(x, '%d.%m.%Y').timestamp())), el))
        temp2.append(el)  

    temp3 = some_date.split('-')

    for el in temp3:
        el = str(int(datetime.strptime(el, '%d.%m.%Y').timestamp()))
        temp4.append(el)


    print(temp)
    print(temp2)
    print(temp3)
    print(temp4)



#    return dates

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021-08.11.2021'

print(is_available_date(dates, some_date))
