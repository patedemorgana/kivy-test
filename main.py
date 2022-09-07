## Boilerplate code

# from kivy.app import App
# from kivy.lang import Builder


# GUI = Builder.load_file("screen.kv")

# class MyAppp(App):
    # def build(self):
    #     return GUI

## Boilerplate code

from kivy.app import App
from kivy.lang import Builder


GUI = Builder.load_file("screen.kv")

class MyApp(App):
    def build(self):
        return GUI

MyApp().run