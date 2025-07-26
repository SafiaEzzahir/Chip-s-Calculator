from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class NumberLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 5
        self.button_texts = ["7", "8", "9", "DEL", "AC",
                             "4", "5", "6", "X", "/",
                             "1", "2", "3", "+", "-",
                             "0", ".", "x10", "Ans", "="]
        self.buttons = {}

        for num in self.button_texts:
            button = Button(text=num)
            self.add_widget(button)
            self.buttons[num] = button

        self.format()

    def format(self):
        self.buttons["DEL"].background_color = (1, 0, 0, 1)
        self.buttons["AC"].background_color = (0, 0, 1, 1)

class OtherButtonsLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cols = 6
        self.button_texts = ["OPTN", "CALC", "txt", "txt", "S", "x",
                             "fraction", "sq root", "sq", "indices", "log", "ln"
                             "(-)", "'", "x-1", "sin", "cos", "tan",
                             "STO", "ENG", "(", ")", "S->D", "M+"]
        
        self.buttons = {}
        
        for op in self.button_texts:
            button = Button(text=op)
            self.add_widget(button)
            self.buttons[op] = button

class MainButtonsLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.upanddown = ArrowButtonsUpAndDown()

        self.shiftbutton = Button(text="shift")
        self.alphabutton = Button(text="alpha")
        self.upbutton = Button(text="up")
        self.downbutton = Button(text="down")
        self.leftbutton = Button(text="left")
        self.rightbutton = Button(text="right")
        self.menubutton = Button(text="menu")
        self.onbutton = Button(text="on")

        self.add_widget(self.shiftbutton)
        self.add_widget(self.alphabutton)
        self.add_widget(self.leftbutton)
        self.add_widget(self.upanddown)
        self.upanddown.add_widget(self.upbutton)
        self.upanddown.add_widget(self.downbutton)
        self.add_widget(self.rightbutton)
        self.add_widget(self.menubutton)
        self.add_widget(self.onbutton)

class ArrowButtonsUpAndDown(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"
