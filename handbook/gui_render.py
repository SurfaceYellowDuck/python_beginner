from tkinter import Label, Scrollbar, RIGHT, Y, BOTTOM, X, CENTER, NO, END
from tkinter import Tk, ttk, Frame, Button, Entry
from db_methods import write_phone, connect_to_db, get_all_phones, delete_phone, update_contact_db

window = Tk()
window.geometry('500x600')

lbl = Label(window, text="Handbook")

n_book = ttk.Notebook()
frame1 = Frame()
root_2 = Frame()

n_book.add(frame1, text="Add contact")
n_book.add(root_2, text="Contact list")


def get_phone():
    return add_phone_field.get()


def get_name():
    return add_name_field.get()


def get_all_info_to_add_contact():
    name = get_name()
    phone = get_phone()
    info = {"name": name, "phone": phone}
    return info


def write_contact_to_db():
    connect_to_db()
    info = get_all_info_to_add_contact()
    new_phone_info = write_phone(info["name"], info["phone"])
    frame2.insert(parent='', index='end', iid=new_phone_info['id'], text='',
                  values=(f'{new_phone_info["id"]}', f'{new_phone_info["name"]}',
                          f'{new_phone_info["phone_number"]}'))


def get_all_contacts():
    return get_all_phones()


contact_list_scroll = Scrollbar(root_2)
contact_list_scroll.pack(side=RIGHT, fill=Y)

contact_list_scroll = Scrollbar(root_2, orient='horizontal')
contact_list_scroll.pack(side=BOTTOM, fill=X)

frame2 = ttk.Treeview(root_2, yscrollcommand=contact_list_scroll.set, xscrollcommand=contact_list_scroll.set,
                      selectmode="extended")


def get_selection(event=None):
    selected_items = []
    for selection in frame2.selection():
        item = frame2.item(selection)
        selected_items.append(item)
        # id_, name, phone = item["values"][0:3]

        # text = f"Выбор: {id_}, {name} <{phone}>"
    # print(selected_items)
    return selected_items


frame2['columns'] = ('id', 'contact_name', 'contact_phone')

frame2.column("#0", width=0, stretch=NO)
frame2.column("id", anchor=CENTER, width=10)
frame2.column("contact_name", anchor=CENTER, width=175)
frame2.column("contact_phone", anchor=CENTER, width=175)

frame2.heading("#0", text="", anchor=CENTER)
frame2.heading("id", text="id", anchor=CENTER)
frame2.heading("contact_name", text="name", anchor=CENTER)
frame2.heading("contact_phone", text="phone", anchor=CENTER)
frame2.bind("<<TreeviewSelect>>", get_selection)


def render_contacts():
    connect_to_db()
    contacts = get_all_contacts()
    # delete_contacts_button.pack()
    for contact in contacts:
        frame2.insert(parent='', index='end', iid=contact['id'], text='',
                      values=(f'{contact["id"]}', f'{contact["name"]}', f'{contact["phone_number"]}'))


render_contacts()
frame2.pack()


def delete_items():
    content = get_selection()
    for el in content:
        delete_phone(int(el['values'][0]))
        frame2.delete(el['values'][0])
    # frame2.delete(content[0]['values'][0])
    # print(type(cont))


def update_contact(pk, phone, name):
    update_contact_db(pk, name, phone)
    frame2.delete(pk)
    frame2.insert(parent='', index='end', iid=pk, text='',
                  values=(f'{pk}', f'{name}', f'{phone}'))


def click_update():
    content = get_selection()
    for el in content:
        window_update = Tk()

        window_update.title("Обновить контакт")
        window_update.geometry('250x200')

        edit_phone_field = Entry(window_update, width=30)
        edit_name_field = Entry(window_update, width=30)

        name_update_label = Label(window_update, justify='left', text='name')
        phone_update_label = Label(window_update, justify='left', text='phone')

        phone_update_label.pack()
        edit_phone_field.pack()
        name_update_label.pack()
        edit_name_field.pack()

        edit_phone_field.delete(0, END)
        edit_phone_field.insert(0, el['values'][2])

        edit_name_field.delete(0, END)
        edit_name_field.insert(0, el['values'][1])

        button = Button(window_update, text="Подтвердить изменения", command=lambda: update_contact(
            int(el["values"][0]),
            edit_phone_field.get(),
            edit_name_field.get()))

        button.pack()


delete_button = ttk.Button(root_2, text="Удалить", command=delete_items)
update_button = ttk.Button(root_2, text="Изменить", command=click_update)

delete_button.pack()
update_button.pack()
contact_list_scroll.config(command=frame2.yview)
contact_list_scroll.config(command=frame2.xview)

name_label = Label(frame1, justify='left', text='name')
phone_label = Label(frame1, justify='left', text='phone')

add_phone_field = Entry(frame1, width=30)
add_name_field = Entry(frame1, width=30)
add_contact_button = Button(frame1, text='Add contact', command=write_contact_to_db)

n_book.pack()
phone_label.pack()
add_phone_field.pack()
name_label.pack()
add_name_field.pack()
add_contact_button.pack()

window.mainloop()
