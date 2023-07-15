

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput

from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits

age = '7'
name = ''


class InstructionsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instructionsLbl = Label(text = txt_instruction)
        self.nextButton = Button(text = 'Start', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5})
        self.nextButton.on_press = self.next
        

        nameLabel = Label(text = 'Enter your name:', halign = 'right')
        self.nameInput = TextInput(multiline = False)

        ageLabel = Label(text = 'Enter your age:', halign = 'right')
        self.ageInput = TextInput(multiline = False)

        mainLayout = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        nameLayout = BoxLayout(size_hint=(0.8, None), height = '30sp')
        ageLayout = BoxLayout(size_hint=(0.8, None), height = '30sp')

        nameLayout.add_widget(nameLabel)
        nameLayout.add_widget(self.nameInput)

        ageLayout.add_widget(ageLabel)
        ageLayout.add_widget(self.ageInput)

        mainLayout.add_widget(instructionsLbl)
        mainLayout.add_widget(nameLayout)
        mainLayout.add_widget(ageLayout)
        mainLayout.add_widget(self.nextButton)
        

        self.add_widget(mainLayout)

    def next(self):
        global name
        global age
        name = self.nameInput.text
        age = self.ageInput.text
        self.manager.current = 'Screen 2'


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instructionsLbl = Label(text = txt_test1)
        self.nextButton = Button(text = 'Next', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5})
        self.nextButton.on_press = self.next

        resultLabel = Label(text = 'Enter the result:', halign = 'right')
        resultInput = TextInput(multiline = False)

        resultLayout = BoxLayout(size_hint=(0.8, None), height = '30sp')
        resultLayout.add_widget(resultLabel)
        resultLayout.add_widget(resultInput)

        mainLayout = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        mainLayout.add_widget(instructionsLbl)
        mainLayout.add_widget(resultLayout)
        mainLayout.add_widget(self.nextButton)

        self.add_widget(mainLayout)

    def next(self):
        self.manager.current = 'Screen 3'



class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instructionsLbl = Label(text = txt_test2)
        self.nextButton = Button(text = 'Next', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5})
        self.nextButton.on_press = self.next

        mainLayout = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        mainLayout.add_widget(instructionsLbl)
        mainLayout.add_widget(self.nextButton)

        self.add_widget(mainLayout)

    def next(self):
        self.manager.current = 'Screen 4'


class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instructionsLbl = Label(text = txt_test3)
        self.nextButton = Button(text = 'Finalize', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5})
        self.nextButton.on_press = self.next

        resultLabel = Label(text = 'Result:', halign = 'right')
        resultInput = TextInput(multiline = False)

        result2Label = Label(text = 'Result after rest:', halign = 'right')
        result2Input = TextInput(multiline = False)

        mainLayout = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        resultLayout = BoxLayout(size_hint=(0.8, None), height = '30sp')
        result2Layout = BoxLayout(size_hint=(0.8, None), height = '30sp')

        resultLayout.add_widget(resultLabel)
        resultLayout.add_widget(resultInput)

        result2Layout.add_widget(result2Label)
        result2Layout.add_widget(result2Input)

        mainLayout.add_widget(instructionsLbl)
        mainLayout.add_widget(resultLayout)
        mainLayout.add_widget(result2Layout)
        mainLayout.add_widget(self.nextButton)

        self.add_widget(mainLayout)
    
    def next(self):
        self.manager.current = 'Screen 5'
    

class FifthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.instructionsLbl = Label(text = '')

        mainLayout = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)

        mainLayout.add_widget(self.instructionsLbl)

        
        self.add_widget(mainLayout)

        self.on_enter = self.before

    def before(self):
        global name
        global age
        self.instructionsLbl.text = name + '-' + age








        

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstructionsScreen(name = 'Instructions'))
        sm.add_widget(SecondScreen(name = 'Screen 2'))
        sm.add_widget(ThirdScreen(name = 'Screen 3'))
        sm.add_widget(FourthScreen(name = 'Screen 4'))
        sm.add_widget(FifthScreen(name = 'Screen 5'))

        return sm

app = MyApp()
app.run()


