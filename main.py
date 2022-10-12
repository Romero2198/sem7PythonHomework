import controller
def find_or_read(my_str)->str:
    if my_str == '1':
        controller.phonebook_record()
    elif my_str == '2':
        controller.phonebook_read()
my_str = input('Введите что сделать 1 - Записать, или 2 - Найти: ')
find_or_read(my_str)