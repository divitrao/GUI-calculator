from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title('image viewer')
root.iconbitmap('images/marriage.ico.jpg')

my_image1 = ImageTk.PhotoImage(Image.open('images/marriage.jpg'))
my_image2 = ImageTk.PhotoImage(Image.open('images/marriage2.jpg'))
my_image3 = ImageTk.PhotoImage(Image.open('images/marriage3.jpg'))
my_image4 = ImageTk.PhotoImage(Image.open('images/marriage4.jpg'))
my_image_list = [my_image1, my_image2, my_image4, my_image2]

def back(imageNumber):
    global my_label
    global button_backward
    global button_forward

    my_label.grid_forget()
    my_label = Label(image=my_image_list[imageNumber-1])
    button_forward = Button(root,text=">>",command= lambda :forward(imageNumber+1))
    button_backward = Button(root,text="<<",command=lambda :back(imageNumber-1))

    my_label.grid(row=0, column=0, columnspan=3)

    if imageNumber == 1:
        button_backward = Button(root, text="<<", state=DISABLED)

    button_forward.grid(row=1, column=2)
    button_backward.grid(row=1, column=0)

    #status_bar updation
    status = Label(root, text="image " + str(imageNumber) +" of " + str(len(my_image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def forward(imageNumber):
    global  my_label
    global button_backward
    global  button_forward

    my_label.grid_forget()
    my_label=Label(image=my_image_list[imageNumber-1])
    button_forward = Button(root, text=">>", command=lambda: forward(imageNumber+1))
    button_backward = Button(root, text="<<", command=lambda :back(imageNumber-1))


    my_label.grid(row=0,column=0,columnspan=3)

    if imageNumber==4:
        button_forward = Button(root,text=">>",state=DISABLED)

    button_forward.grid(row=1, column=2)
    button_backward.grid(row=1, column=0)

    # status_bar updation
    status = Label(root, text="image " + str(imageNumber) +" of " + str(len(my_image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)



button_forward = Button(root,text=">>", command=lambda : forward(2))
button_quit=Button(root,text="Exit",command=root.quit)
button_backward = Button(root,text="<<", command=back)
button_forward.grid(row=1,column=2)
button_quit.grid(row=1,column=1,pady=10)
button_backward.grid(row=1,column=0)

my_label = Label(image=my_image1)

status = Label(root,text="image 1 of " + str(len(my_image_list)) ,bd=1,relief=SUNKEN,anchor=E)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

my_label.grid(row=0,column=0,columnspan=3)

root.mainloop()