from tkinter import *
from tkinter import font

root = Tk()
root.geometry("300x250")
root.title("Blue Tiger")
root.iconbitmap('c:/Users/rares/Documents/GitHub/BlueTiger/platform/images/tigru_albastru.ico')

login_text = Label(
    root,
    text="Login",
    font=("Consolas", 15)
)
login_text.pack()

#-----------------name--------------

name_text = Label(
    root,
    text="Name",
    font=("Arial", 10)
)
name_text.place(x=2, y=30)

name_field = Entry(
    root,
)
name_field.place(x=2, y=50)

#-------------password-------------

password_text = Label(
    root,
    text="Password",
    font=("Arial", 10)
)
password_text.place(x=2, y=70)

password_field = Entry(
    root,
    show="*"
)
password_field.place(x=2, y=90)

#--------------admin mode-------------

admin_mode = False

admin_text = Label(
    root,
    text="Admin Mode",
    font=("Arial", 10)
)
admin_text.place(x=2, y=115)

admin_cb =  Checkbutton(root, variable=admin_mode, onvalue=True, offvalue=False)
admin_cb.place(x=80, y=115)

#---------------login button------------

login_button = Button(
    root,
    text="Login",
    command=root.quit()
)

login_button.place(x=5, y=143)

root.mainloop() 