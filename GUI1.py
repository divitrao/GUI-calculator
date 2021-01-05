from  tkinter import *
root = Tk()
root.title('simple calculator')

def myclick():
    myLabel1 =  Label(root,text="hello "+ ent.get()) #.grid(row=0,column=0)
    # myLabel2 =  Label(root,text="hello2") #.grid(row=1,column=1)
    # myLabel3 =  Label(root,text="hello3") #.grid(row=2,column=2)
    # myLabel1.grid(row=0,column=0)
    # myLabel2.grid(row=1,column=1)
    # myLabel3.grid(row=2,column=2)
    myLabel1.pack()
    # myLabel2.pack()
    # myLabel3.pack()

ent = Entry(root,width=35,borderwidth=5)
ent.grid(row=0,column=0,columnspan=3,padx=50,pady=40)

def button_click(number):
    current_number = ent.get()
    ent.delete(0,END)
    ent.insert(0,str(current_number) + str(number))
    return

def button_clear():
    ent.delete(0,END)

def button_add():
    first_number = ent.get()
    global f_num
    f_num = int(first_number)
    ent.delete(0,END)
    return
def button_equal():
    second_number = ent.get()
    ent.delete(0,END)
    ent.insert(0,f_num + int(second_number))

# myButton = Button(root,text="click me",command=myclick)
myButton_1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
myButton_2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
myButton_3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
myButton_4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
myButton_5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
myButton_6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
myButton_7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
myButton_8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
myButton_9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
myButton_0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
myButton_add = Button(root,text="+",padx=39,pady=20,command=button_add)
myButton_equal = Button(root,text="=",padx=90,pady=20,command= button_equal)
myButton_clear = Button(root,text="AC",padx=90,pady=20,command= button_clear)

myButton_1.grid(row=1,column=0)
myButton_2.grid(row=1,column=1)
myButton_3.grid(row=1,column=2)

myButton_4.grid(row=2,column=0)
myButton_5.grid(row=2,column=1)
myButton_6.grid(row=2,column=2)

myButton_7.grid(row=3,column=0)
myButton_8.grid(row=3,column=1)
myButton_9.grid(row=3,column=2)

myButton_0.grid(row=4,column=0)
myButton_equal.grid(row=4,column=1,columnspan=2)
myButton_add.grid(row=5,column=0)
myButton_clear.grid(row=5,column=1,columnspan=2)




root.mainloop()

# def niz():
#     global x
#     x=20
#     print("inside ",x)
# niz()
#
# print(x)
