from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.clock import Clock

class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        self.done = False
        self.total = total
        self.current = 0
        my_txt = "Seconds passed: " + str(self.current) 
        super().__init__(text = my_txt)

    def start(self):
        Clock.schedule_interval(self.change, 1)

    def restart(self, total, **kwargs):
        self.done = False
        self.total = total
        self.current = 0
        self.text = "Seconds passed:" + str(self.current)
        self.start()

    def change(self, dt):
        self.current += 1
        self.text = "Seconds passed: " + str(self.current)
        if self.current >= self.total:
            self.done = True
            return False

