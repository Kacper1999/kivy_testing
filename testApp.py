from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


class Manager(ScreenManager):
    def update(self):
        self.ids.screen2.ids.patient_name.text = self.ids.screen1.ids.patient_name.text
        self.ids.screen2.ids.patient_surname.text = self.ids.screen1.ids.patient_surname.text


class Screen1(Screen, Widget):
    pass


class Screen2(Screen, Widget):
    pass


class Screen3(Screen):
    pass


class testApp(App):
    def build(self):
        self.title = "Noughts and Crosses"
        return Manager()


if __name__ == "__main__":
    testApp().run()
