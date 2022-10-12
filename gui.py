def request_name()->str:
    return input('Введите имя человека: ')
def request_surname()->str:
    return input('Введите фамилию человека: ')
def request_phone_number()->str:
    return input('Введите номер человека: ')
def request_description()->str:
    return input('Введите описание: ')

def request_parameter()->str:
    parameter = input('Введите параметр для поиска 1 - Имя,2 - Фамилия,3 - Номер: ')
    if parameter == '1':
        name = input('Введите имя для поиска: ')
        return name
    elif parameter == '2':
        surname = input('Введите фамилию для поиска: ')
        return surname
    elif parameter == '3':
        phone_number = input('Введите номер для поиска: ')
        return phone_number
    else:
        return print('Введите Имя, Фамилия, Номер')