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
import requests

GUI = Builder.load_file("screen.kv")

class MyApp(App):
    def build(self):
        return GUI
    def on_start(self):
        self.pegar_imagem("cachorro1")
    def pegar_imagem(self, cachorro):
        link = "https://dog.ceo/api/breeds/image/random"
        request = requests.get(link)
        print(request.json())
        

MyApp().run()