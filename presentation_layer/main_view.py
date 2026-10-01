# which frame maps to window
from jedi.cache import signature_time_cache


from presentation_layer.window import Window
from tkinter import Frame
from presentation_layer.Frames.Login import loginFrame
from presentation_layer.Frames.register import RegisterFrame

class MainView():
    def __init__(self,user_business_logic):
        self.frames = {}
        self.window = Window("core banking")

        self.add_frame("login", loginFrame(self.window,self,user_business_logic),300,200)
        self.add_frame("register",RegisterFrame(self.window,self),300,250)

        self.show_frame("login")

        self.window.show()


    def add_frame(self, frame_name:str, frame:Frame, width, height ): #یه ابجکت از کلاس فریم یا فرزندان فریم
        self.frames[frame_name] = (frame, width, height)
        self.frames[frame_name][0].grid(row=0, column=0, sticky = "news")

    def show_frame(self, frame_name:str):
        current_frame_value = self.frames[frame_name]
        current_frame_value[0].tkraise()
        width, height = current_frame_value[1], current_frame_value[2]
        self.window.resize(width, height)


