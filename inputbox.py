from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="blue", fg="White")
e.pack()
e.insert(0,"Enter your name:")
def myClick():
    hello = "Hello " + e.get()
    mylabel = Label(root,text=hello)
    mylabel.pack()
myButton = Button(root, text="Enter your stock Quote", command=myClick, fg="blue", background="green")
myButton.pack()


root.mainloop()