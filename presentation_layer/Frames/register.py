from tkinter import Frame, Label, Entry, Button
from presentation_layer.Component.password_entry import Password_Entry
#from presentation_layer.main_view import MainView


class RegisterFrame(Frame):
    def __init__(self,master,main_view):
        super().__init__(master)
        self.main_view = main_view
        self.grid_columnconfigure(index=1,weight=1)

        self.firstname_label = Label(self, text="firstname")
        self.firstname_label.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=0,column=1,padx=(0,10),pady=(0,10),sticky="ew")

        self.lastname_label = Label(self, text="lastname")
        self.lastname_label.grid(row=1,column=0,padx=10,pady=(0,10),sticky="w")
        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=1,column=1,padx=(0,10),pady=(0,10),sticky="ew")

        self.username_label = Label(self,text="Username")
        self.username_label.grid(row=2,column=0,padx=10,pady=(0,10),sticky="w")
        self.username_entry = Entry(self)
        self.username_entry.grid(row=2,column=1,padx=(0,10),pady=(0,10),sticky="ew")

        self.password_label = Label(self,text="Password")
        self.password_label.grid(row=3,column=0,padx=10,pady=(0,10),sticky="w")
        self.password_entry = Password_Entry(self)
        self.password_entry.grid(row=3,column=1,padx=(0,10),pady=(0,10),sticky="ew")

        self.register_button = Button(self,text="Register")
        self.register_button.grid(row=4,column=1,padx=0,pady=(0,10),sticky="w")
        self.return_to_login = Button(self,text="login",command=self.login_clicked)
        self.return_to_login.grid(row=5,column=1,padx=0,pady=10,sticky="w")

    def login_clicked(self):
        self.main_view.show_frame("login")

