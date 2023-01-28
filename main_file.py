from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

sm = MDScreenManager()

def next(button):
   sm.transition.derection = "right"
   sm.current = "Screen2"

def back(button):
   sm.transition.derection = "left"
   sm.current = "Screen1"

class Screen1(Screen):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      label = MDLabel(text = "Screen1")
      main_layout = BoxLayout(
         orientation = "vertical"
      )

      btn = MDRaisedButton(
         text = "Next",
         font_size = "40sp",
         on_press = next,
         pos_hint = {"center_x": 0.5}
      )
      main_layout.add_widget(label)
      main_layout.add_widget(btn)
      self.add_widget(main_layout)

class Screen2(Screen):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      label = MDLabel(text = "Screen2")
      main_layout = BoxLayout(
         orientation = "vertical"
      )

      btn2 = MDRaisedButton(
         text = "Back",
         font_size = "40sp",
         on_press = back,
         pos_hint = {"center_x": 0.5}
      )
      main_layout.add_widget(label)
      main_layout.add_widget(btn2)
      self.add_widget(main_layout)

class MyApp(MDApp):
   def build(self):
      sm.add_widget(Screen1(name = 'Screen1'))
      sm.add_widget(Screen2(name = "Screen2"))
      return sm



MyApp().run()
