from tkinter import *
import contact_book_BE

def get_selected_row(event):
    try:
        global selected_tuple
        index=list.curselection()[0]
        selected_tuple=list.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list.delete(0,END)
    for row in contact_book_BE.view():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    for row in contact_book_BE.search(name_text.get(),email_id_text.get(),number_text.get(),second_number_text.get()):
        list.insert(END,row)

def add_entry_command():
    contact_book_BE.entry(name_text.get(),email_id_text.get(),number_text.get(),second_number_text.get())
    list.delete(0,END)
    list.insert(END,(name_text.get(),email_id_text.get(),number_text.get(),second_number_text.get()))

def delete_command():
    contact_book_BE.delete(selected_tuple[0])

def update_command():
    contact_book_BE.update(selected_tuple[0],name_text.get(),email_id_text.get(),number_text.get(),second_number_text.get())

window=Tk()

l1 = Label(window, text="name")
l1.grid(row=0, column=0)

l2 = Label(window, text="email_id")
l2.grid(row=0, column=3)

l3 = Label(window, text="number")
l3.grid(row=1, column=0)

l4 = Label(window, text="second_number")
l4.grid(row=1, column=3)

name_text= StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0,column=2)

email_id_text= StringVar()
e2 = Entry(window, textvariable=email_id_text)
e2.grid(row=0,column=4)

number_text= StringVar()
e3 = Entry(window, textvariable=number_text)
e3.grid(row=1,column=2)

second_number_text= StringVar()
e4 = Entry(window, textvariable=second_number_text)
e4.grid(row=1,column=4)

list = Listbox(window,height=6,width=30)
sb1 = Scrollbar(window,orient="vertical")

list.grid(row=2,column=0,rowspan=6,columnspan=2)
list.config(yscrollcommand = sb1.set)

sb1.grid(row=3,column=2,rowspan=4,sticky=N+S,)
sb1.config(command= list.yview)

list.configure(yscrollcommand=sb1.set)
sb1.configure(command=list.yview())

list.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window, text= "View All", width=12, command =view_command)
b1.grid(row=2,column=3)

b2 = Button(window, text= "Search Entry", width=12, command =search_command)
b2.grid(row=3,column=3)

b3 = Button(window, text= "Add Entry", width=12, command =add_entry_command)
b3.grid(row=4,column=3)

b4 = Button(window, text= "Update", width=12, command= update_command)
b4.grid(row=5,column=3)

b5 = Button(window, text= "Delete", width=12, command= delete_command)
b5.grid(row=6,column=3)

b6 = Button(window, text= "Close", width=12, command= window.destroy)
b6.grid(row=7,column=3)



contact_book_BE.connection()

window.mainloop()