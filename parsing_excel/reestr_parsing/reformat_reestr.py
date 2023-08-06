import csv
from datetime import datetime, date, timedelta 
import xlsxwriter

columns = ["Дата", "Время", "RRN", "Код авторизации", "Номер карты", "Сумма, ₽"]

__INPUT_FILE = 'D:\\List_of_trips.csv'
__OUTPUT_FILE = 'D:\\test_reestr.xlsx'

base_price = 65
sale_price = 44

temp_list = []
start_date = date(2023,3,1)
stop_date = date(2023,7,11)
date_step = timedelta(days=1)

####### functions ########
def head_creator(price): #формирует заголовки на каждом листе
    rows = 8
    worksheet = workbook.add_worksheet(f"{datetime.strftime(stop_date, '%d.%m.%Y')}-{price}")

    merge_format_small = workbook.add_format({'align': 'left'})
    merge_format = workbook.add_format({'align': 'left', 'font_size': 12})
    merge_format_bold = workbook.add_format({'align': 'left', 'font_size': 12, 'bold': True})

    worksheet.write(0, 0, 'ООО "ТКК"')
    worksheet.merge_range(1, 0, 1, 5, 'Реестр операций, совершенных при оплате Банковскими картами в', merge_format_bold)
    worksheet.merge_range(2, 0, 2, 5, 'терминалах АО "СЕВЕРГАЗБАНК"', merge_format_bold)
    worksheet.merge_range(3, 0, 3, 5, '(выгрузка из Транспортной процессинговой платформы (ТПП))', merge_format)
    worksheet.merge_range(6, 0, 6, 2, 'Дата совершения операций:', merge_format_small)
    worksheet.write(6, 3, f"{datetime.strftime(stop_date, '%d.%m.%Y')}")


    for i in range(len(columns)):
        worksheet.write(8, i, f'{columns[i]}')
    rows += 1

    worksheet.set_column_pixels(0, 0, 7.4*10.14)
    worksheet.set_column_pixels(1, 1, 7.4*9.43)
    worksheet.set_column_pixels(2, 2, 7.4*13.86)
    worksheet.set_column_pixels(3, 3, 7.4*15.71)
    worksheet.set_column_pixels(4, 4, 7.4*12.14)
    worksheet.set_column_pixels(5, 5, 7.4*12.43)

    return rows, worksheet

def temp_list_creator(price): #формирует список данных для каждой строки
    temp_list.append(datetime.strptime(line.get('\ufeffЛокальная дата поездки'), '%d.%m.%Y').date())
    temp_list.append(datetime.strptime(line.get('Локальное время поездки'), '%H:%M:%S').time())
    temp_list.append(line.get('RRN').strip('\u200b'))
    temp_list.append(line.get('Код авторизации'))
    temp_list.append(line.get('Маска карты'))
    temp_list.append(price)
    return temp_list

def row_writer(date_format, time_format, rrn_format, autorisation_format, card_number_format, summa_format, summa_format_bold):
    worksheet.write_datetime(rows, 0, temp_list[0], date_format) #Дата (30.06.2023, право)
    worksheet.write_datetime(rows, 1, temp_list[1], time_format) #Время (23:55:27, право)
    if temp_list[2]:
        worksheet.write_number(rows, 2, int(temp_list[2]), rrn_format) #RRN (​001173332214, лево)
    worksheet.write(rows, 3, f'{temp_list[3]}', autorisation_format) #Код авторизации (259071, право)
    worksheet.write(rows, 4, f'{temp_list[4]}') #Номер карты (510070*200, лево)
    worksheet.write_number(rows, 5, temp_list[5], summa_format) #Сумма, ₽ (65,00, право)

def format_creator():
    # Инициализация форматов
    text_bold = workbook.add_format({'bold': True})
    date_format = workbook.add_format({'num_format': 'dd.mm.yyyy'})
    date_format_bold = workbook.add_format({'num_format': 'dd.mm.yyyy', 'bold': True})
    time_format = workbook.add_format({'num_format': 'HH:MM:ss'})
    rrn_format = workbook.add_format()
    autorisation_format = workbook.add_format()
    card_number_format = workbook.add_format()
    summa_format = workbook.add_format()
    summa_format_bold = workbook.add_format()

    # установка форматов
    text_bold.set_align('right')
    rrn_format.set_num_format('0')
    rrn_format.set_align('left')
    autorisation_format.set_align('right')
    summa_format.set_num_format('0.00')
    summa_format_bold.set_num_format('0.00')
    summa_format_bold.set_bold()
    return date_format, time_format, rrn_format, autorisation_format, card_number_format, summa_format, summa_format_bold, date_format_bold, text_bold
#########################


################### main part ###############
with open(__INPUT_FILE, 'r', encoding = 'utf-8') as input_file:
    all_data = csv.DictReader(input_file, delimiter=';')
    list_data = [el for el in all_data]

    workbook = xlsxwriter.Workbook(__OUTPUT_FILE)

    date_format, time_format, rrn_format, autorisation_format, card_number_format, summa_format, summa_format_bold, date_format_bold, text_bold = format_creator() 

    while stop_date >= start_date:

        rows, worksheet = head_creator(base_price)
        for line in list_data:
            if line.get('\ufeffЛокальная дата поездки') == datetime.strftime(stop_date, '%d.%m.%Y') and line.get('Сумма, ₽') == '65.0': 
                temp_list = temp_list_creator(base_price)
                row_writer(date_format, time_format, rrn_format, autorisation_format, card_number_format, summa_format, summa_format_bold)
                temp_list = [] 
                rows += 1
        worksheet.write(rows, 0, 'Итого за:', text_bold)  
        worksheet.write(rows, 1, f"{datetime.strftime(stop_date, '%d.%m.%Y')}", date_format_bold)  
        worksheet.write_number(rows, 5, base_price*(rows-9), summa_format_bold)   

        rows, worksheet = head_creator(sale_price)    
        for line in list_data:
            if line.get('\ufeffЛокальная дата поездки') == datetime.strftime(stop_date, '%d.%m.%Y') and line.get('Сумма, ₽') != '65.0': 
                temp_list = temp_list_creator(sale_price)
                row_writer(date_format, time_format, rrn_format, autorisation_format, card_number_format, summa_format, summa_format_bold)           
                temp_list = [] 
                rows += 1
        worksheet.write(rows, 0, 'Итого за:', text_bold)
        worksheet.write(rows, 1, f"{datetime.strftime(stop_date, '%d.%m.%Y')}", date_format_bold) 
        worksheet.write_number(rows, 5, sale_price*(rows-9), summa_format_bold)

        stop_date -= date_step        
    workbook.close()  