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
       

