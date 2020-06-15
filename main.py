from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from random import randint

class VectorCalculator(Widget):
    pass


class VectorCalculatorApp(App):
    def build(self):
        return VectorCalculator()


if __name__ == '__main__':
    VectorCalculatorApp().run()
