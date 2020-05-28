from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

Config.set("graphics", "width", "400")
Config.set("graphics", "height", "570")
Config.set("graphics", "borderless", "0")
Config.set("graphics", "resizable", "0")
Config.set("kivy", "window_icon", "nyc.ico")


class Manager(ScreenManager):
    pass


class ScreenOne(Screen, Widget):
    pass


class ScreenTwo(Screen, Widget):
    pass


class ScreenThree(Screen):
    pass


class kivyExampleApp(App):
    def build(self):
        self.title = "Noughts and Crosses"
        return Manager()


if __name__ == "__main__":
    kivyExampleApp().run()
