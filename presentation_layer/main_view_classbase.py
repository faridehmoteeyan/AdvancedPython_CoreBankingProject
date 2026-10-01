from tkinter import Frame
from presentation_layer.Frames.Login import loginFrame
from presentation_layer.window import Window

class MainViewClassBase():
    def __init__(self, frame: Frame,name,width,height):
        self.name = name
        self.frame = frame
        self.width = width
        self.height = height

        self.window = Window("CoreBanking")

    def grid_frame(self):
        pass

