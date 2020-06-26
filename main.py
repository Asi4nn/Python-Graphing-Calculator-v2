from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy_garden.graph import Graph, MeshLinePlot

from math import sin, cos, tan
from float_rounder import *


class GraphPlot(RelativeLayout):
    def __init__(self, **kwargs):
        super(GraphPlot, self).__init__(**kwargs)
        self.y_range = 10
        self.x_range = 10
        self.range_multiplier = [2, 2.5, 2]
        self.graph = Graph(xlabel="x", ylabel="y",
                           x_ticks_major=self.x_range/2,
                           y_ticks_major=self.y_range/2,
                           y_grid_label=True, x_grid_label=True, x_grid=True, y_grid=True,
                           xmin=-self.x_range, xmax=self.x_range, ymin=-self.y_range, ymax=self.y_range, draw_border=False)
        # graph.size = (1200, 400)
        # self.graph.pos = self.center

        self.plot = MeshLinePlot(color=[1, 1, 1, 1])
        x = -self.x_range
        self.plot.points = []
        while x < self.x_range:
            try:
                self.plot.points.append((x, sin(x)))
            except ZeroDivisionError:
                pass

            x += self.x_range / 100
        self.add_widget(self.graph)

        self.graph.add_plot(self.plot)


    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            # for whatever reason, the definition of scrollup and scrolldown are reversed
            if touch.button == 'scrollup':
                self.zoomOut()
            elif touch.button == 'scrolldown':
                self.zoomIn()


    def zoomIn(self):
        print(self.x_range)
        self.x_range = multiplyByFloat(self.x_range, 1/self.range_multiplier[0])
        self.y_range = multiplyByFloat(self.y_range, 1/self.range_multiplier[0])
        self.range_multiplier.insert(0, self.range_multiplier[2])
        del self.range_multiplier[-1]
        self.update()


    def zoomOut(self):
        print(self.x_range)
        self.x_range = multiplyByFloat(self.x_range, self.range_multiplier[0])
        self.y_range = multiplyByFloat(self.y_range, self.range_multiplier[0])
        self.range_multiplier.append(self.range_multiplier[0])
        self.range_multiplier.remove(self.range_multiplier[0])
        self.update()


    def update(self):
        self.remove_widget(self.graph)
        self.graph = Graph(xlabel="x", ylabel="y",
                           x_ticks_major=self.x_range/2,
                           y_ticks_major=self.y_range/2,
                           y_grid_label=True, x_grid_label=True, x_grid=True, y_grid=True,
                           xmin=-self.x_range, xmax=self.x_range, ymin=-self.y_range, ymax=self.y_range, draw_border=False)
        self.plot = MeshLinePlot(color=[1, 1, 1, 1])
        x = -self.x_range
        self.plot.points = []
        while x < self.x_range:
            try:
                self.plot.points.append((x, sin(x)))
            except ZeroDivisionError:
                pass

            x += self.x_range / 100
        self.add_widget(self.graph)

        self.graph.add_plot(self.plot)


class GraphingCalculatorApp(App):
    def build(self):
        grid_layout = GridLayout(cols=1, padding=20, spacing=20, size_hint_y=None)
        grid_layout.bind(minimum_size=grid_layout.setter('size'))
        graph = GraphPlot(size_hint_y=None, height=500)
        label = Label(size_hint_y=None, text='Python Graphing Calculator')
        grid_layout.add_widget(label)
        grid_layout.add_widget(graph)

        return grid_layout


if __name__ == '__main__':
    GraphingCalculatorApp().run()
