import tkinter
from bookstore_backend_oop import Database

database = Database("books.db")

#Functions for buttons to tie backend to frontend
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,len(title_string))
        e1.insert(len(title_string), selected_tuple[1])
        e2.delete(0,len(author_string))
        e2.insert(len(author_string), selected_tuple[2])
        e3.delete(0,len(year_string))
        e3.insert(len(year_string), selected_tuple[3])
        e4.delete(0,len(isbn_string))
        e4.insert(len(isbn_string), selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0, len(database.view()))
    count = 0
    for row in database.view():
        list1.insert(count, row)
        count += 1

def search_command():
    list1.delete(0, len(database.view()))
    count = 0
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(count, row)
        count += 1

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, len(database.view()))
    list1.insert(-1, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

#User interface starts here

window = tkinter.Tk()

window.wm_title("Bookstore")

#labels
l1 = tkinter.Label(window, text = "Title")
l1.grid(row =0, column = 0)

l2 = tkinter.Label(window, text = "Author")
l2.grid(row =0, column = 2)

l3 = tkinter.Label(window, text = "Year")
l3.grid(row =1, column = 0)

l4 = tkinter.Label(window, text = "ISBN")
l4.grid(row =1, column = 2)

#entries
title_text = tkinter.StringVar()
e1 = tkinter.Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)
title_string=str(title_text)

author_text = tkinter.StringVar()
e2 = tkinter.Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)
author_string=str(author_text)

year_text = tkinter.StringVar()
e3 = tkinter.Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)
year_string = str(year_text)

isbn_text = tkinter.StringVar()
e4 = tkinter.Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)
isbn_string = str(isbn_text)

#list box & scroll bar
list1 = tkinter.Listbox(window, height = 15, width = 40)
list1.grid (row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = tkinter.Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

#search buttons
b1 = tkinter.Button(window, text = "View All", width = 12, command=view_command)
b1.grid(row = 2, column = 3)

b2 = tkinter.Button(window, text = "Search Entry", width = 12, command=search_command)
b2.grid(row = 3, column = 3)

b3 = tkinter.Button(window, text = "Add Entry", width = 12, command=add_command)
b3.grid(row = 4, column = 3)

b4 = tkinter.Button(window, text = "Update Selected", width = 12, command=update_command)
b4.grid(row = 5, column = 3)

b5 = tkinter.Button(window, text = "Delete Selected", width = 12,command=delete_command)
b5.grid(row = 6, column = 3)

b6 = tkinter.Button(window, text = "Exit", width = 12, command=window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop() 