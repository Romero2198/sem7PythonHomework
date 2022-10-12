import gui
def save_str()->str:
    name = gui.request_name()
    surname = gui.request_surname()
    number = gui.request_phone_number()
    description = gui.request_description()
    path = 'PhoneBook.txt'
    with open(path, 'a') as file:
        file.write(f'{name} {surname} {number} {description}\n')
    print(f'"{name} {surname} {number} {description}" записан в файл "PhoneBook.txt"')

def find_needed_in_list(find):
    word_is_fount = False
    with open('PhoneBook.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            if not word_is_fount:
                if find in line:
                    print(line)