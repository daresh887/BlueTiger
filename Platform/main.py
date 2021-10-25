from tkinter import *
from tkinter import ttk

import mysql.connector
 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(Tk):
     
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        container = Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        self.frames = {} 
  
        for F in (SignIn, SignUp, Page2):
  
            frame = F(container, self)
  
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(SignIn)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
  
class SignIn(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
         
        login_text = Label(
        self,
        text="Login",
        font=("Consolas", 15)
        )
        login_text.pack()
        #-----------------name--------------

        email_text = Label(
            self,
            text="Name",
            font=("Arial", 10)
        )
        email_text.place(x=2, y=30)

        email_field = Entry(
            self,
        )
        email_field.place(x=2, y=50)

        #-------------password-------------

        password_text = Label(
            self,
            text="Password",
            font=("Arial", 10)
        )
        password_text.place(x=2, y=70)

        password_field = Entry(
            self,
            show="*"
        )
        password_field.place(x=2, y=90)

        #--------------admin mode-------------

        admin_mode = False

        admin_text = Label(
            self,
            text="Admin Mode",
            font=("Arial", 10)
        )
        admin_text.place(x=2, y=115)

        admin_cb = Checkbutton(self, variable=admin_mode, onvalue=True, offvalue=False)
        admin_cb.place(x=80, y=115)

        #---------------login button------------

        login_button = Button(
            self,
            text="Login",
            command=lambda:self.zainin(email_field.get(), password_field.get())
        )

        login_button.place(x=5, y=143)

        #----------------sign up-----------------
        
        signup_button = Button(
            self,
            text="Don't have an account? Register by pressing this button",
            command=lambda: controller.show_frame(SignUp)
        )
        signup_button.place(x=5, y=170)

    def zainin(self, e, p):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="prolix99",
        database="bluetiger"
        )

        mycursor = mydb.cursor()

        sql = "SELECT * from accounts where email=\"" + e +"\" && password=\"" + p + "\";"
        mycursor.execute(sql)

        account = mycursor.fetchall()
        if account:
            print("Succesfully logged in!")
        else:
            print("Incorrect password or email")

        mydb.commit()
  
# second window frame page1
class SignUp(Frame):
     
    def __init__(self, parent, controller):
         
        Frame.__init__(self, parent)
        
        signup_text = Label(
        self,
        text="SignUp",
        font=("Consolas", 15)
        )
        signup_text.pack()
        #-----------------name--------------

        name_text = Label(
            self,
            text="Name",
            font=("Arial", 10)
        )
        name_text.place(x=2, y=30)

        name_field = Entry(
            self,
        )
        name_field.place(x=2, y=50)

        firstname_text = Label(
            self,
            text="First Name",
            font=("Arial", 10)
        )
        firstname_text.place(x=2, y=70)

        firstname_field = Entry(
            self,
        )
        firstname_field.place(x=2, y=90)

        #------------e-mail---------------

        email_text = Label(
            self,
            text="E-mail",
            font=("Arial", 10)
        )
        email_text.place(x=2, y=110)

        email_field = Entry(
            self,
        )
        email_field.place(x=2, y=130)

        #-------------password-------------

        password_text = Label(
            self,
            text="Password",
            font=("Arial", 10)
        )
        password_text.place(x=2, y=150)

        password_field = Entry(
            self,
            show="*"
        )
        password_field.place(x=2, y=170)

        #---------------signup button------------

        signup_button = Button(
            self,
            text="Sign Up",
            command = lambda:self.zainap(name_field.get(), firstname_field.get(), email_field.get(), password_field.get())
        )
        signup_button.place(x=40, y=195)

    def zainap(self, n, pn, e, p):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="prolix99",
        database="bluetiger"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO accounts(last_name, first_name, email, password) VALUES (%s, %s, %s, %s)"
        val = (n, pn, e, p)
        mycursor.execute(sql, val)

        mydb.commit()

  
# third window frame page2
class Page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(SignUp))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(SignIn))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
# Driver Code
app = tkinterApp()
app.mainloop()