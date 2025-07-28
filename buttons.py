from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ShiftButton(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"

        self.label = Label(text="shift", color=(0.8, 0.75, 0, 1))
        self.button = Button(on_press=self.pressed)

        self.shift = False
        self.last_pressed = 0

        self.add_widget(self.label)
        self.add_widget(self.button)

    def pressed(self, instance):
        if self.shift:
            self.shift = False
        else:
            self.shift = True
        self.last_pressed = 0

    def falseformat(self):
        self.button.background_color = (1, 1, 1, 1)

    def trueformat(self):
        self.button.background_color = (0, 1, 0, 1)

    def update(self, managervalue):
        if managervalue:
            self.trueformat()
        else:
            self.falseformat()

        if self.shift:
            self.last_pressed +=1

class AlphaButton(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"

        self.label = Label(text="alpha", color=(0.8, 0, 0, 1))
        self.button = Button(on_press=self.pressed)

        self.alpha = False
        self.last_pressed = 0

        self.add_widget(self.label)
        self.add_widget(self.button)

    def pressed(self, instance):
        if self.alpha:
            self.alpha = False
        else:
            self.alpha = True
        self.last_pressed = 0

    def falseformat(self):
        self.button.background_color = (1, 1, 1, 1)

    def trueformat(self):
        self.button.background_color = (0, 1, 0, 1)

    def update(self, managervalue):
        if managervalue:
            self.trueformat()
        else:
            self.falseformat()

        if self.alpha:
            self.last_pressed += 1

class ShiftAndAlphaManager():
    def __init__(self, shiftlayout, alphalayout):
        self.shiftlayout = shiftlayout
        self.alphalayout = alphalayout

        self.shift = False
        self.alpha = False

    def update(self):
        if self.shiftlayout.shift and self.alphalayout.alpha:
            if self.shiftlayout.last_pressed > self.alphalayout.last_pressed:
                self.shift = False
                self.alpha = True
                self.shiftlayout.shift = False
            else:
                self.shift = True
                self.alpha = False
                self.alphalayout.alpha = False
        else:
            self.shift = self.shiftlayout.shift
            self.alpha = self.alphalayout.alpha

        self.shiftlayout.update(self.shift)
        self.alphalayout.update(self.alpha)