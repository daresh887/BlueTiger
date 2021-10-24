from tkinter import *

root = Tk()

root.geometry("900x500")

button = Button(root, text="button")
button.pack()
text = Label(root, text="text")
text.pack()

root.mainloop() 