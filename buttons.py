from tkinter import *

root = Tk()
def myClick():
    mylabel = Label(root,text="Look! I clicked a button!!")
    mylabel.pack()
myButton = Button(root, text="Click Me!!", command=myClick, fg="blue", background="green")
myButton.pack()



root.mainloop()
#background u can use "bg"