import db,gui
def phonebook_record():
    db.save_str()
def phonebook_read():
    find = gui.request_parameter()
    db.find_needed_in_list(find)