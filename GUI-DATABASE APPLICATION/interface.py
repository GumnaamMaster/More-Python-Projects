from tkinter import *
import data

def select_row(event): # takes default arguments to settle things up.
    global selected
    if(not t1.curselection()):
        print("Nothing in here...")
    else:
        index=t1.curselection()[0] # will select the row number of selected row and a comma to have other things with [0] at end
                            # will only select the row number of selected row.
                            # we can use below function, but from where we will get the index so above method to get index.
        selected=t1.get(index) # this will take the data of complete row of index number index.
        if(type(selected[0]) is tuple):
            selected=selected[0]
        else:
            pass
        e1.delete(0,END)
        e1.insert(END,selected[1])

        e2.delete(0,END)
        e2.insert(END,selected[2])

        e3.delete(0,END)
        e3.insert(END,selected[3])

        e4.delete(0,END)
        e4.insert(END,selected[4])

def view_data():
    t1.delete(0,END)
    for row in data.view():
        t1.insert(END,row)

def search_data():
    values=data.search(title_e1.get(),author_e2.get(),year_e3.get(),isbn_e4.get())
    t1.delete(0,END)
    for row in values:
        t1.insert(END,row)

def add_data():
    t1.delete(0,END)
    data.insert(title_e1.get(),author_e2.get(),year_e3.get(),isbn_e4.get())
    values=(selected[0],title_e1.get(),author_e2.get(),year_e3.get(),isbn_e4.get())
    t1.insert(END,values)

def delete_data():
    data.delete(selected[0])

def update_data():
    data.update(selected[0],title_e1.get(),author_e2.get(),year_e3.get(),isbn_e4.get())

window=Tk()

window.wm_title("BookStore")
lab1=Label(window,text="Title",width=10)
lab1.grid(row=0,column=0)
title_e1=StringVar()
e1=Entry(window,textvariable=title_e1)
e1.grid(row=0,column=1)

lab2=Label(window,text="Author",width=10)
lab2.grid(row=0,column=2)
author_e2=StringVar()
e2=Entry(window,textvariable=author_e2)
e2.grid(row=0,column=3)

lab3=Label(window,text="Year",width=10)
lab3.grid(row=1,column=0)
year_e3=StringVar()
e3=Entry(window,textvariable=year_e3)
e3.grid(row=1,column=1)

lab4=Label(window,text="ISBN",width=10)
lab4.grid(row=1,column=2)
isbn_e4=StringVar()
e4=Entry(window,textvariable=isbn_e4)
e4.grid(row=1,column=3)

t1=Listbox(window,width=40,height=10)
t1.grid(row=2,column=0,columnspan=2,rowspan=6)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

t1.bind('<<ListboxSelect>>',select_row)
#it takes 2 arguments event type and list object.

t1.configure(yscrollcommand=sb1.set)
sb1.configure(command=t1.yview)

b1=Button(window,text="View all",width=10,command=view_data)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry",width=10,command=search_data)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry",width=10,command=add_data)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=10,command=update_data)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=10,command=delete_data)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=10,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
