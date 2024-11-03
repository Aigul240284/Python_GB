from return_data_file import data_file
def change_row():
    data,nf = data_file()
    count_rows = len(data)
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

    name = input('Введите свое имя: ')
    surname = input('Введите свою фамлию: ')
    birthdate = input('Введите дату рождения: ')
    town = input('Введите город: ')
    data[number_row-1] = f'{number_row};{name};{surname}:{birthdate};{town}\n'
    with open(f'data_directory12/data{nf}.txt','w', encoding = 'utf-8') as file:
                  file.writelines(data)
    print('Данные успешно изменены!')



    
    