import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

##class Button(Screen):


class StartScreen(Widget):
    def Przycisk(self):
        button = Button(text = 'Listy zakupów', size_hint=(0.5,0.5), font_size='20sp', pos_hint={'center_x':0.1 , 'center_y':0.1})
        return button


class TwojaLodowaApp(App):
    def build(self):
        layout = GridLayout(cols=3)
        btn1 = Button(text = 'Listy zakupów', size_hint=(0.5,0.5), font_size='20sp', pos_hint={'center_x':0.1 , 'center_y':0.1})
        btn2 = Button(text = 'Moja Ladówa', size_hint=(0.5,0.5), font_size='20sp', pos_hint={'center_x':0.1 , 'center_y':0.1})
        btn3 = Button(text = 'Przepisy', size_hint=(0.5,0.5), font_size='20sp', pos_hint={'center_x':0.1 , 'center_y':0.1})
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout




if __name__ == '__main__':
    TwojaLodowaApp().run()

