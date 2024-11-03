from return_data_file import data_file
def delete_row():
    data,nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print('Файл пустой!')
    else:
        number_row = int(input(f'Введите номер строки '
                           f'от одного до {count_rows}: '))
    while 1 > number_row or number_row> count_rows:
        number_row = int(input('Ошибка!'
                               f'Введите номер строки '
                               f'от 1 до {count_rows}: '))
    
    del data[number_row-1]
    # data=[f'{i+1};{data[i].split(";")[1]};'
    #       f'{data[i].split(";")[2]}'
    #       f'{data[i].split(";")[3]}'
    #       f'{data[i].split(";")[4]}'
    #       for i in range(len(data))]
    data = [d.split(';') for d in data]
    data = [f'{i+1};{data[i][1]};{data[i][2]};{data[i][3]};{data[i][4]}'
    for i in range(len(data))]
    with open(f'data_directory12/data{nf}.txt','w', encoding = 'utf-8') as file:
                  file.writelines(data)
    print('Данные успешно удалены!\n')
    

    

