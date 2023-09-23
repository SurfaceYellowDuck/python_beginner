from models import PhoneNumbers
import orm_sqlite


def connect_to_db():
    db = orm_sqlite.Database('PhoneNumbers.db')
    PhoneNumbers.objects.backend = db


def write_phone(name, phone):
    new_phone = PhoneNumbers({"name": name, "phone_number": phone})
    new_phone.save()
    info = PhoneNumbers.objects.all()[-1]
    return info


def get_phone(pk):
    contact = PhoneNumbers.objects.get(pk)
    return contact

def get_all_phones():
    return PhoneNumbers.objects.all()


def update_contact_db(pk, name='', phone=''):
    name_phone = get_phone(pk)
    if name != '':
        name_phone["name"] = name
    if phone != '':
        name_phone["phone_number"] = phone
    name_phone.update()


def delete_phone(name_to_find):
    name_phone = get_phone(name_to_find)
    name_phone.delete()
    # pass