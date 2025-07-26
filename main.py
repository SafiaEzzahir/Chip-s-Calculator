from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from buttons import NumberLayout, OtherButtonsLayout, MainButtonsLayout

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        self.add_widget(Label(text="answer", size_hint=(1, 0.1)))
        
        self.add_widget(MainButtonsLayout())
        self.add_widget(OtherButtonsLayout())
        self.add_widget(NumberLayout())

class ChipsCalculatorApp(App):
    def build(self):
        return Builder.load_file("calculator.kv")
    
if __name__ == '__main__':
    ChipsCalculatorApp().run()