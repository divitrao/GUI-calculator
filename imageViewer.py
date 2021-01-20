from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title('image viewer')
root.iconbitmap('images/marriage.jpg')
button_forward = Button(root,text=">>")
button_quit=Button(root,text="Exit",command=root.quit)
button_backward = Button(root,text="<<" )
button_forward.grid(row=1,column=2)
button_quit.grid(row=1,column=1)
button_backward.grid(row=1,column=0)
my_image1 = ImageTk.PhotoImage(Image.open('images/marriage.jpg'))
my_image2 = ImageTk.PhotoImage(Image.open('images/marriage2.jpg'))
my_image3 = ImageTk.PhotoImage(Image.open('images/marriage3.jpg'))
my_image = [my_image1,my_image2,my_image3]
my_label = Label(image=my_image1)

my_label.grid(row=0,column=0,columnspan=3)

root.mainloop()