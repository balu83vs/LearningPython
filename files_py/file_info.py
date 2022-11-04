def size_check(el, sum_size):
    if el[2] == 'B':
        sum_size += int(el[1])
    elif el[2] == 'KB':
        sum_size += int(el[1]) * 1024
    elif el[2] == 'MB':
        sum_size += int(el[1]) * 1024 ** 2
    elif el[2] == 'GB':
        sum_size += int(el[1]) * 1024 ** 3
    return sum_size

def add_check(sum_size):
    temp = 0
    if 0 < sum_size // 1024 < 1024:
        form_size = 'KB'
        
        temp = sum_size % 1024

        if temp < 1024 / 2:
            sum_size = sum_size // 1024
        else:
            sum_size = (sum_size // 1024) + 1
            
    elif 1024 < sum_size // 1024 < 1024 ** 2:
        form_size = 'MB'
        
        temp = sum_size % (1024 ** 2)

        if temp < (1024 ** 2) / 2:
            sum_size = sum_size // 1024 ** 2
        else:
            sum_size = (sum_size // 1024 ** 2) + 1
            
    elif 1024 ** 2 < sum_size // 1024 < 1024 ** 3:
        form_size = 'GB'
        
        temp = sum_size % (1024 ** 3)

        if temp < (1024 ** 3) / 2:
            sum_size = sum_size // 1024 ** 3
        else:
            sum_size = (sum_size // 1024 ** 3) + 1
    else:
        form_size = 'B'
    temp = 0    
    return form_size, sum_size

with open('files.txt', encoding = 'utf-8') as input_file, open('out_file.txt', 'w', encoding = 'utf-8') as output_file:
    temp_list2 = []
    sum_size = 0
    form_size = 'B'
    index_list = ['name', 'size', 'ect']
    temp_list = list(map(lambda x: str(x).strip().split(), input_file.readlines()))       
    temp_list = sorted(temp_list, key = lambda x: x[0].split('.')[1])     

    temp_add = temp_list[0][0].split('.')[1]

    for el in temp_list:
        if temp_add == el[0].split('.')[1]:
            temp_list2.append(el[0])
            sum_size = size_check(el, sum_size)
        else:
            temp_add = el[0].split('.')[1]
            form_size, sum_size = add_check(sum_size)
            temp_list2 = sorted(temp_list2)
            for el2 in temp_list2:
                print(el2, file = output_file)
            print('----------', file = output_file)
            print(f'Summary: {sum_size} {form_size}', file = output_file)
            print(file = output_file)
            sum_size = 0
            sum_size = size_check(el, sum_size)
            temp_list2 = []
            temp_list2.append(el[0])
    form_size, sum_size = add_check(sum_size)
    temp_list2 = sorted(temp_list2)
    for el2 in temp_list2:
                print(el2, file = output_file)
    print('----------', file = output_file)
    print(f'Summary: {sum_size} {form_size}', file = output_file, end = '')        

with open('out_file.txt', encoding = 'utf-8') as out:
    while True:
        line = out.readline()
        if len(line) != 0:
            print(line, end = '')
        else:
            break
