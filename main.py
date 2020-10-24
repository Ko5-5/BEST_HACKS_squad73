import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty,ListProperty, ReferenceListProperty, ObjectProperty, BooleanProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from random import randrange
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

##class Button(Screen):
class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

    def Przycisk(self):
        layout = GridLayout(cols=3, row_force_default=True, row_default_height=60)
        #btn1 = Button(text = 'Listy zakupów', size_hint=(0.5,0.5), font_size='20sp', pos_hint={'center_x':0.1 , 'center_y':0.1})
        #btn2 = Button(text = 'Moja Ladówa', size_hint=(0.5,0.5), font_size='20sp', pos_hint={'center_x':0.1 , 'center_y':0.1})
        #btn3 = Button(text = 'Przepisy', size_hint=(0.5,0.5), font_size='20sp', pos_hint={'center_x':0.1 , 'center_y':0.1})
        btn1 = Button(text = 'Listy zakupów')
        btn2 = Button(text = 'Moja Ladówa')
        btn3 = Button(text = 'Przepisy')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout

class ListyZakupow(Screen):
    pass

class MojaLodowa(Screen):
    pass

class Przepisy(Screen):
    pass


class TwojaLodowaApp(App):
    def build(self):
        return ScreenManagement()

if __name__ == '__main__':
    Window.size = (450, 900)
    TwojaLodowaApp().run()

