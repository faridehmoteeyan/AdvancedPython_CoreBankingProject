from  tkinter import Tk

class Window (Tk):
    def __init__(self,title_value):
        super().__init__() #access tofather


        self.title(title_value)
        self.grid_columnconfigure(index=0,weight=1)
        self.grid_rowconfigure(index=0,weight=1) # اگر سایز صفحه عوض شد ریسپانسیو باشه

    def resize (self,width,height):
        self.geometry(f"{width}x{height}")
    def show(self):
        self.mainloop()
