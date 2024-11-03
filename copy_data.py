from return_data_file import data_file
# from ui_yes_or_no import yes_or_no

def copy_row():
    data,nf = data_file()
    count_rows = len(data)
    nf_for_copy = None
    data_for_copy=[]
    data1=[]
    number_row = 0
    if count_rows == 0:
        print('Файл пустой!')
    else:
        number_row = int(input(f'Введите номер строки '
                           f'от одного до {count_rows}: '))
    while 1 > number_row or number_row> count_rows:
        number_row = int(input('Ошибка!'
                               f'Введите номер строки '
                               f'от 1 до {count_rows}: '))
    if nf ==1:
        nf_for_copy=2
    else: nf_for_copy=1
    with open(f'data_directory12/data{nf_for_copy}.txt','r', encoding = 'utf-8') as file1:
                  data_for_copy = file1.readlines()
    data1=data[number_row-1].split(';')
    data1[0]= len(data_for_copy) + 1
    data1 = [str(item) for item in data1]
    string_for_copy = ';'.join(data1)
    with open(f'data_directory12/data{nf_for_copy}.txt','a', encoding = 'utf-8') as file:
                  file.writelines(string_for_copy)
    print('Данные успешно cкопированы!')
# print(copy_row())
