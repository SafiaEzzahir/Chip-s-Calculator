from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from buttonlayouts import NumberLayout, OtherButtonsLayout, MainButtonsLayout
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.properties import Clock

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = dp(10)
        self.spacing =dp(8)

        Clock.schedule_interval(self.update, 1.0/60.0)

        self.mainbuttonslayout = MainButtonsLayout(size_hint=(1, 0.15))
        self.otherbuttonslayout = OtherButtonsLayout(size_hint=(1, 0.27))
        self.numberlayout = NumberLayout(size_hint=(1, 0.4))

        self.add_widget(Label(text="answer", size_hint=(1, 0.18), color=(0, 0, 0, 1)))
        self.add_widget(self.mainbuttonslayout)
        self.add_widget(self.otherbuttonslayout)
        self.add_widget(self.numberlayout)

    def update(self, dt):
        self.mainbuttonslayout.update()
        self.otherbuttonslayout.update()
        self.numberlayout.update()

class ChipsCalculatorApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return Builder.load_file("calculator.kv")
    
if __name__ == '__main__':
    ChipsCalculatorApp().run()