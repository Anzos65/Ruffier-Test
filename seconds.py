from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput
from kivy import Clock

class seconds(Label):
    def __init__(self, total, **kwargs):
        self.total = 0
        self.current = 0
        my_txt = "Seconds passed: " + str(self.current) 
        super().__init__(text = my_txt)
    def start(self):
        Clock.schedule_interval(self.change, 1)
    def change(self, dt):
        self.current += 1
        my_txt = "Seconds passed: " + str(self.current)
        if self.current >= 0:
            return False

