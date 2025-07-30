from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

class PreferencesPopup():
    def __init__(self):
        self.count = 0

        self.contentlayout = PreferencesContentLayout()
        self.contentscrollview = ScrollView()
        self.contentscrollview.add_widget(self.contentlayout)

        self.popup = Popup(title="pop", content=self.contentscrollview, auto_dismiss=False, size_hint=(.5, .5))

    def update(self):
        if self.count < 1200:
            self.count += 1
        else:
            self.popup.open()

class PreferencesContentLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint_y = None

        self.bind(minimum_height=self.setter('height'))

        self.add_widget(Label(text="1", size_hint_y=None, height=dp(80)))
        self.add_widget(Label(text="2", size_hint_y=None, height=dp(80)))
        self.add_widget(Label(text="3", size_hint_y=None, height=dp(80)))
        self.add_widget(Button(text="4", size_hint_y=None, height=dp(80)))