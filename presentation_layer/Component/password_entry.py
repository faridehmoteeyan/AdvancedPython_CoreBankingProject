from tkinter import Frame,Entry, Button

class Password_Entry(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=0,column=0, padx=(0,10), sticky="ew")
        self.change_state_button = Button(self,text="show", command=self.change_state_button_clicked)
        self.change_state_button.grid(row=0, column=1, padx=0, sticky="w")

    def change_state_button_clicked(self):
        if self.change_state_button.cget("text") == "show":
            self.change_state_button.config(text="hide")
            self.password_entry.config(show="")
        else:
            self.change_state_button.config(text="show")
            self.password_entry.config(show="*")
    def get_value(self):
        return self.password_entry.get()

