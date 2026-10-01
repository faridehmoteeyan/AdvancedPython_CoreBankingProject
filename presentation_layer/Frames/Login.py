from tkinter import Frame,Label, Entry, Checkbutton, Button, messagebox

#from presentation_layer.main_view import MainView
from presentation_layer.Component.password_entry import Password_Entry
from businessLogic.useer_bussiness_logic import UserBusinessLogic

class loginFrame(Frame):
    def __init__(self, main_window, main_view,user_business_logic:UserBusinessLogic):
        super().__init__(main_window)
        self.main_view = main_view
        #self.user_business_logic = UserBusinessLogic()# its not good for testing use DEPENDANCY INJECTION : get instance as input,dont make it
        self.user_business_logic = user_business_logic

        self.grid_columnconfigure(1, weight=1)

        self.username_label = Label(self, text="username")
        self.username_label.grid(row=0 ,column=0, pady=10 , padx=10, sticky="w")
        self.username_entry = Entry(self)
        self.username_entry.grid(row=0, column=1, pady=10, padx=(0,10), sticky="ew")

        self.password_label = Label(self, text="password")
        self.password_label.grid(row=1 ,column=0, pady=(0,10) , padx=10, sticky="w")
        self.password_entry = Password_Entry(self)
        #self.password_entry = Entry(self)
        self.password_entry.grid(row=1, column=1, pady=(0,10), padx=(0,10), sticky="ew")

        self.remmeber_me_button = Checkbutton(self, text="Remmeber me")
        self.remmeber_me_button.grid(row=2, column=1, pady=(0,10), padx=(0,10), sticky="w")#اگر اندازه سلول بزرگتر شود وسط نیاید

        self.login_button = Button(self, text="login", command=self.login_button_clicked)
        self.login_button.grid(row=3,column=1, pady=(0,10), padx=(0,10), sticky="w")
        self.register_button = Button(self, text="register",command=self.register_button_clicked)
        self.register_button.grid(row=4,column=1, pady=(0,10), padx=(0,10), sticky="w")

    def login_button_clicked(self):
        user_name = self.username_entry.get()
        password = self.password_entry.get_value()

        response = self.user_business_logic.login(user_name, password)###ن ابجکت نمسازم بهتر نیست؟
        if response.is_successed:
            messagebox.showinfo("Welcome")
        else:
            messagebox.showerror("login_failed",response.message)
    def register_button_clicked(self):
        self.main_view.show_frame("register")











