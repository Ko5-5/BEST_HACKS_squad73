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
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label 
from kivy.uix.spinner import Spinner
import time
##class Button(Screen):

class RV_Lodowa(RecycleView):
    def __init__(self,**kwargs):
        super(RV_Lodowa,self).__init__(**kwargs)
        self.event = Clock.schedule_interval(self.read, 1.0/10.0)
        self.time_start = time.time()

    def read(self, dt):
        f = open("lista.txt", "r")
        lista = list(())
        for x in f:
            lista.append(x)
        f.close()
        self.data = [{'text':str(x)} for x in lista]

#Scrolled shoplist
class RV_Lista(RecycleView):
    def __init__(self,**kwargs):
        super(RV_Lista,self).__init__(**kwargs)
        
        self.event = Clock.schedule_interval(self.read, 1.0/10.0)
        self.time_start = time.time()

    def read(self, dt):
        f = open("shop_list.txt", "r")
        lista_zak = list(())
        for x in f:
            lista_zak.append(x)
        f.close()
        
        self.data = [{'text':str(x)} for x in lista_zak]

class RV_Sniadanie(RecycleView):
    def __init__(self,**kwargs):
        super(RV_Sniadanie,self).__init__(**kwargs)
        
        self.event = Clock.schedule_interval(self.read, 1.0/10.0)
        self.time_start = time.time()

    def read(self, dt):
        f = open("sniadanie_przepis.txt", "r")
        lista_zak = list(())
        for x in f:
            lista_zak.append(x)
        f.close()
        
        self.data = [{'text':str(x)} for x in lista_zak]

class RV_Lunch(RecycleView):
    def __init__(self,**kwargs):
        super(RV_Lunch,self).__init__(**kwargs)
        
        self.event = Clock.schedule_interval(self.read, 1.0/10.0)
        self.time_start = time.time()

    def read(self, dt):
        f = open("lunch_przepis.txt", "r")
        lista_zak = list(())
        for x in f:
            lista_zak.append(x)
        f.close()
        
        self.data = [{'text':str(x)} for x in lista_zak]

class RV_Obiad(RecycleView):
    def __init__(self,**kwargs):
        super(RV_Obiad,self).__init__(**kwargs)
        
        self.event = Clock.schedule_interval(self.read, 1.0/10.0)
        self.time_start = time.time()

    def read(self, dt):
        f = open("obiad_przepis.txt", "r")
        lista_zak = list(())
        for x in f:
            lista_zak.append(x)
        f.close()
        
        self.data = [{'text':str(x)} for x in lista_zak]

class RV_Kolacja(RecycleView):
    def __init__(self,**kwargs):
        super(RV_Kolacja,self).__init__(**kwargs)
        
        self.event = Clock.schedule_interval(self.read, 1.0/10.0)
        self.time_start = time.time()

    def read(self, dt):
        f = open("kolacja_przepis.txt", "r")
        lista_zak = list(())
        for x in f:
            lista_zak.append(x)
        f.close()
        
        self.data = [{'text':str(x)} for x in lista_zak]


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

class StartScreen(Screen):
    pass

class ListyZakupow(Screen):
    shop_list = ListProperty()
    table = StringProperty()
    value = StringProperty()
    
    def read(self):
        '''
        Reading scores from txt file
        
        input file.txt
        output string(self.table)
        '''
        #renew data
        self.shop_list.clear()
        self.table = ""

        #new data read from file
        score_file = open('shop_list.txt','r')
        self.shop_list = score_file.readlines()
        
        
        for item in self.shop_list[::-1]:
            self.table += item
        
        score_file.close()

    def kup(self, value):
        '''
        Usuwa produkt z listy shop_list i przenosi do listy lodowa
        '''
        self.shop_list.remove(value)
        print(self.shop_list)
        with open('shop_list.txt', 'w') as f:
            for item in self.shop_list:
                f.write("%s" % item)

        with open('lista.txt', 'a') as f:
            f.write("%s" % value)


class DodajProdukt(Screen):
    textinput = ObjectProperty(None)
    score = ObjectProperty(None)

    def new_score(self):
        score_file = open('shop_list.txt','a')
        
        score_file.write(self.textinput.text)
        score_file.write('\n')
        score_file.close()
        
        self.manager.current = 'ListyZakupow'

class DataPrzydatnosci(Screen):
    pass

class MojaLodowa(Screen):
    pass

class Przepisy(Screen):
    pass

class Sniadanie(Screen):
    pass

class Lunch(Screen):
    pass

class Obiad(Screen):
    pass

class Kolacja(Screen):
    pass

class TwojaLodowaApp(App):
    def build(self):
        return ScreenManagement()

if __name__ == '__main__':
    Window.size = (450, 900)
    TwojaLodowaApp().run()

