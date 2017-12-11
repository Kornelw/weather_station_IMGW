#-*- coding: utf-8 -*-
# @author = Kornel Wojtasiak
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.animation import Animation

import pymysql
import Login

class WeatherView(ScrollView):
    
    
    
    connect = pymysql.connect(Login.dataLogin["host"], Login.dataLogin["user"], Login.dataLogin["pass"], Login.dataLogin["db"], use_unicode = 1, charset ="utf8")
    cdb = connect.cursor()
    cdb.execute("SET NAMES 'utf8'")
    
    
    def cdb_data(self,query):
        cdb_d = []
        
        self.cdb.execute(query)
        
        result = self.cdb.fetchall()
        
        for row in result:
            string = str(row[0])+ "," +str(row[1]) + "," +str(row[2])+ "," +str(row[3])+ "," +str(row[4])+ "," +str(row[5])
            cdb_d.append(string)
        
        return cdb_d
    
Builder.load_string("""


<MenuScreen>:
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                spacing: 10
                
                AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'bootom'
                    
                    Button:
                        size_hint: 0.5, 0.2
                        text: "Logowanie"
                        on_press:
                            root.manager.transition.direction = "up"
                            root.manager.current = 'login'
                            
                            
                AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'top'
                    
                    Button:
                        size_hint: 0.5, 0.2
                        text: "Quit"
                        
            Image:
                source: 'IMGW.png'
                
<SettingsScreen>:

<ForPeople>:


""")

wsm = ScreenManager()
wsm.add_widget(MenuScreen(name='menu'))
wsm.add_widget()
wsm.add_widget()
wsm.add_widget()



class Weather(App):
    def build(self):
        return wsm


if __name__ == '__main__':
    Weather().run()
