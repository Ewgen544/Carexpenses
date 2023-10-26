from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class CarexpensesApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Carexpenses", halign="center")


CarexpensesApp().run()