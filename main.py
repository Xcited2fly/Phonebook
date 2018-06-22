from mongoengine import connect
from creation import User
from Tkinter import *

connect("phonebook")

def new_contact():
    n = e1.get()
    no = e2.get()
    a = User(name=n,phone=no).save()
    l4.configure(text="Contact Saved!!")

def search():
    global text
    s = e3.get()
    c = 0
    for user in User.objects.filter(name__iexact=s):
        c = 1
        n = user.name
        p = user.phone
##    l4.configure(text=n)
##    l5.configure(text=p)
    if c==1:
        l4.configure(text=n)
        l5.configure(text=p)
    else:
        l4.configure(text="Contact not found!!")
        l5.configure(text='')

tk = Tk()
tk.configure(background='green')
tk.title('Phonebook')
tk.geometry('200x400')

l = Label(tk,text="Phonebook",bg="green",font="Times 25 bold")
l.pack()
l1=Label(tk,text="Name:",bg='green',font="Times 15 bold")
l2=Label(tk,text="Number:",bg='green',font="Times 15 bold")
l1.pack()
e1=Entry(tk, bd=5)
e1.pack()
e2=Entry(tk, bd=5)
l2.pack()
e2.pack()
b=Button(tk,text="SAVE",command=new_contact,bg='green',font="Times 15 bold")
b.pack()
l3=Label(tk,text="Search:",bg='green',font="Times 15 bold")
l3.pack()
e3=Entry(tk, bd=5)
e3.pack()
b1=Button(tk,text="FIND",command=search,bg='green',font="Times 15 bold")
b1.pack()
l4=Label(tk,text="",bg='green',font="Times 15 bold")
l4.pack()
l5=Label(tk,text="",bg='green',font="Times 15 bold")
l5.pack()

tk.mainloop()

