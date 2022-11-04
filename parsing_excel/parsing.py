def read_csv():
    with open('price.csv', encoding = 'utf-8') as file:
        list_res = []
        key_list = list(map(lambda x: x.strip().lstrip('\ufeff'), file.readline().split(';')))
        value_list = list(map(lambda x: x.strip(), file.readline().split(';')))

        while True:
            value_list = list(map(lambda x: x.strip(), file.readline().split(';')))
            if len(value_list) > 1:
                list_res.append(dict(zip(key_list, value_list)))
            else:
                break
        
#        value_list = list(map(lambda x: x.strip(), file.readlines()))
#        print(value_list)

#        for val in value_list:
#            list_res.append(dict(zip(key_list, val.split(','))))

        return list_res    

        

print(read_csv())
#read_csv()
