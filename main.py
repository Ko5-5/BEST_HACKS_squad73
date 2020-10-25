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
from datetime import datetime 

#CZESC PYTHONOWA - PRZEPISY - POCZATEK
def odswiez_sniadanie():
    class przepis:
        def __init__(self,name,skladniki=None):
            self.name = name
            self.skladniki = skladniki or []
            
    ###tworzymy liste z przepisami
    sniadanie = open("kolacje.txt")
    przepisy = []
    znacznik = True
    for line in sniadanie:
        if line[0] != "*":
            if znacznik == False:
                przepisy.append(przepis(line[:-1]))
                znacznik = True
            else:
                przepisy[-1].skladniki.append(line[:-1])  
        else:
            znacznik = False

    ###sprawdzamy do jakiego przepisu brakuje najmniej skladników
    lodowka = []
    braki=[]
    indeksy=[]
    mozliwe_przepisy=[]

    fridge = open("lista.txt")
    for line in fridge:
        lodowka.append(line[:-1])

    for i in range(len(przepisy)):
        counter=0
        for j in range(len(przepisy[i].skladniki)):
            if not(przepisy[i].skladniki[j] in lodowka):
                counter+=1
        braki.append(counter)
        indeksy.append(counter)

    braki.sort()
    k=0
    while True:
        if braki[k] > 3 or k>len(braki):
            break
        else:
            k+=1

    ###tworzymy listę przepisów najoptymalniejszych
    kolejna_zmienna_pomocnicza = 0
    for i in range(k):
        mozliwe_przepisy.append(przepisy[indeksy.index(braki[i],kolejna_zmienna_pomocnicza+1)])
        try:
            if braki[i]==braki[i+1]:
                kolejna_zmienna_pomocnicza=indeksy.index(braki[i])
        except: pass

    ###wpierdalamy do pliku
    wyniki=open("sniadanie_przepis.txt","w")

    for i in range(len(mozliwe_przepisy)):
        wyniki.write(mozliwe_przepisy[i].name+" -> "+str(braki[i])+"\n")
        for j in range(len(mozliwe_przepisy[i].skladniki)):
            if mozliwe_przepisy[i].skladniki[j] in lodowka:
                wyniki.write(mozliwe_przepisy[i].skladniki[j]+"\n")
            else:
                wyniki.write("#"+mozliwe_przepisy[i].skladniki[j]+"\n")
    wyniki.close()

def odswiez_lunch():
    class przepis:
        def __init__(self,name,skladniki=None):
            self.name = name
            self.skladniki = skladniki or []
            
    ###tworzymy liste z przepisami
    sniadanie = open("kolacje.txt")
    przepisy = []
    znacznik = True
    for line in sniadanie:
        if line[0] != "*":
            if znacznik == False:
                przepisy.append(przepis(line[:-1]))
                znacznik = True
            else:
                przepisy[-1].skladniki.append(line[:-1])  
        else:
            znacznik = False

    ###sprawdzamy do jakiego przepisu brakuje najmniej skladników
    lodowka = []
    braki=[]
    indeksy=[]
    mozliwe_przepisy=[]

    fridge = open("lista.txt")
    for line in fridge:
        lodowka.append(line[:-1])

    for i in range(len(przepisy)):
        counter=0
        for j in range(len(przepisy[i].skladniki)):
            if not(przepisy[i].skladniki[j] in lodowka):
                counter+=1
        braki.append(counter)
        indeksy.append(counter)

    braki.sort()
    k=0
    while True:
        if braki[k] > 3 or k>len(braki):
            break
        else:
            k+=1

    ###tworzymy listę przepisów najoptymalniejszych
    kolejna_zmienna_pomocnicza = 0
    for i in range(k):
        mozliwe_przepisy.append(przepisy[indeksy.index(braki[i],kolejna_zmienna_pomocnicza+1)])
        try:
            if braki[i]==braki[i+1]:
                kolejna_zmienna_pomocnicza=indeksy.index(braki[i])
        except: pass

    ###wpierdalamy do pliku
    wyniki=open("lunch_przepis.txt","w")

    for i in range(len(mozliwe_przepisy)):
        wyniki.write(mozliwe_przepisy[i].name+" -> "+str(braki[i])+"\n")
        for j in range(len(mozliwe_przepisy[i].skladniki)):
            if mozliwe_przepisy[i].skladniki[j] in lodowka:
                wyniki.write(mozliwe_przepisy[i].skladniki[j]+"\n")
            else:
                wyniki.write("#"+mozliwe_przepisy[i].skladniki[j]+"\n")
    wyniki.close()

def odswiez_obiad():
    class przepis:
        def __init__(self,name,skladniki=None):
            self.name = name
            self.skladniki = skladniki or []
            
    ###tworzymy liste z przepisami
    sniadanie = open("kolacje.txt")
    przepisy = []
    znacznik = True
    for line in sniadanie:
        if line[0] != "*":
            if znacznik == False:
                przepisy.append(przepis(line[:-1]))
                znacznik = True
            else:
                przepisy[-1].skladniki.append(line[:-1])  
        else:
            znacznik = False

    ###sprawdzamy do jakiego przepisu brakuje najmniej skladników
    lodowka = []
    braki=[]
    indeksy=[]
    mozliwe_przepisy=[]

    fridge = open("lista.txt")
    for line in fridge:
        lodowka.append(line[:-1])

    for i in range(len(przepisy)):
        counter=0
        for j in range(len(przepisy[i].skladniki)):
            if not(przepisy[i].skladniki[j] in lodowka):
                counter+=1
        braki.append(counter)
        indeksy.append(counter)

    braki.sort()
    k=0
    while True:
        if braki[k] > 3 or k>len(braki):
            break
        else:
            k+=1

    ###tworzymy listę przepisów najoptymalniejszych
    kolejna_zmienna_pomocnicza = 0
    for i in range(k):
        mozliwe_przepisy.append(przepisy[indeksy.index(braki[i],kolejna_zmienna_pomocnicza+1)])
        try:
            if braki[i]==braki[i+1]:
                kolejna_zmienna_pomocnicza=indeksy.index(braki[i])
        except: pass

    ###wpierdalamy do pliku
    wyniki=open("obiad_przepis.txt","w")

    for i in range(len(mozliwe_przepisy)):
        wyniki.write(mozliwe_przepisy[i].name+" -> "+str(braki[i])+"\n")
        for j in range(len(mozliwe_przepisy[i].skladniki)):
            if mozliwe_przepisy[i].skladniki[j] in lodowka:
                wyniki.write(mozliwe_przepisy[i].skladniki[j]+"\n")
            else:
                wyniki.write("#"+mozliwe_przepisy[i].skladniki[j]+"\n")
    wyniki.close()

def odswiez_kolacja():
    class przepis:
        def __init__(self,name,skladniki=None):
            self.name = name
            self.skladniki = skladniki or []
            
    ###tworzymy liste z przepisami
    sniadanie = open("kolacje.txt")
    przepisy = []
    znacznik = True
    for line in sniadanie:
        if line[0] != "*":
            if znacznik == False:
                przepisy.append(przepis(line[:-1]))
                znacznik = True
            else:
                przepisy[-1].skladniki.append(line[:-1])  
        else:
            znacznik = False

    ###sprawdzamy do jakiego przepisu brakuje najmniej skladników
    lodowka = []
    braki=[]
    indeksy=[]
    mozliwe_przepisy=[]

    fridge = open("lista.txt")
    for line in fridge:
        lodowka.append(line[:-1])

    for i in range(len(przepisy)):
        counter=0
        for j in range(len(przepisy[i].skladniki)):
            if not(przepisy[i].skladniki[j] in lodowka):
                counter+=1
        braki.append(counter)
        indeksy.append(counter)

    braki.sort()
    k=0
    while True:
        if braki[k] > 3 or k>len(braki):
            break
        else:
            k+=1

    ###tworzymy listę przepisów najoptymalniejszych
    kolejna_zmienna_pomocnicza = 0
    for i in range(k):
        mozliwe_przepisy.append(przepisy[indeksy.index(braki[i],kolejna_zmienna_pomocnicza+1)])
        try:
            if braki[i]==braki[i+1]:
                kolejna_zmienna_pomocnicza=indeksy.index(braki[i])
        except: pass

    ###wpierdalamy do pliku
    wyniki=open("kolacja_przepis.txt","w")

    for i in range(len(mozliwe_przepisy)):
        wyniki.write(mozliwe_przepisy[i].name+" -> "+str(braki[i])+"\n")
        for j in range(len(mozliwe_przepisy[i].skladniki)):
            if mozliwe_przepisy[i].skladniki[j] in lodowka:
                wyniki.write(mozliwe_przepisy[i].skladniki[j]+"\n")
            else:
                wyniki.write("#"+mozliwe_przepisy[i].skladniki[j]+"\n")
    wyniki.close()

#CZESC PYTHONOWA - PRZEPISY - KONIEC

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
        x =  [{'text':str(x)} for x in lista]
        #x.sort(key=lambda date: datetime.strptime(date, "%d-%m-%y"))
        self.data = x

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

class MojaLodowa(Screen):
    fridge_list = ListProperty()
    table = StringProperty()
    value = StringProperty()

    def read(self):
        '''
        Reading scores from txt file
        
        input file.txt
        output string(self.table)
        '''
        #renew data
        self.fridge_list.clear()
        self.table = ""

        #new data read from file
        score_file = open('lista.txt','r')
        self.fridge_list = score_file.readlines()
        
        
        for item in self.fridge_list[::-1]:
            self.table += item
        
        score_file.close()

    def zjedzone(self, value):
        self.fridge_list.remove(value)
        with open('lista.txt', 'w') as f:
            for item in self.fridge_list:
                f.write("%s" % item)

    def data(self, value):
        global lll
        lll = value
        self.fridge_list.remove(value)
        with open('lista.txt', 'w') as f:
            for item in self.fridge_list:
                f.write("%s" % item)

        self.manager.current = 'DataPrzydatnosci'

class DataPrzydatnosci(Screen):
    textinput = ObjectProperty(None)
    score = ObjectProperty(None)
    

    def new_score(self):
        global lll 
        
        with open('lista.txt', 'a') as f:
            f.write(self.textinput.text+' - '+lll)

        self.manager.current = 'MojaLodowa'

class Przepisy(Screen):
    pass

class Sniadanie(Screen):
    def odswiez(self):
        odswiez_sniadanie()


class Lunch(Screen):
    def odswiez(self):
        odswiez_lunch()

class Obiad(Screen):
    def odswiez(self):
        odswiez_obiad()

class Kolacja(Screen):
    def odswiez(self):
        odswiez_kolacja()

class TwojaLodowaApp(App):
    def build(self):
        return ScreenManagement()

if __name__ == '__main__':
    Window.size = (450, 900)
    TwojaLodowaApp().run()

