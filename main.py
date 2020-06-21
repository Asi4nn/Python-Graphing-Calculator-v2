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

from math import sin, cos


class GraphPlot(RelativeLayout):
    def __init__(self, **kwargs):
        super(GraphPlot, self).__init__(**kwargs)
        self.graph = Graph(xlabel="x", ylabel="y", x_ticks_minor=5, x_ticks_major=25, y_ticks_major=1,
                           y_grid_label=True, x_grid_label=True, x_grid=True, y_grid=True,
                           xmin=-0, xmax=50, ymin=-1, ymax=10, draw_border=False)
        # graph.size = (1200, 400)
        # self.graph.pos = self.center

        self.plot = MeshLinePlot(color=[1, 1, 1, 1])
        x = 0
        self.plot.points = []
        while x < 100:
            try:
                self.plot.points.append((x, 1/(x)))
            except ZeroDivisionError:
                pass

            x += 0.01
        #self.plot.points = [(x, cos(x/10)) for x in range(0, 101)]
        self.add_widget(self.graph)

        self.graph.add_plot(self.plot)


class GraphingCalculatorApp(App):
    def build(self):
        scroll_view = ScrollView()
        grid_layout = GridLayout(cols=1, padding=20, spacing=20, size_hint_y=None)
        grid_layout.bind(minimum_size=grid_layout.setter('size'))
        graph = GraphPlot(size_hint_y=None, height=500)
        label = Label(text="Hello World!", size_hint_y=None)
        grid_layout.add_widget(label)
        grid_layout.add_widget(graph)
        scroll_view.add_widget(grid_layout)

        # return grid_layout
        return scroll_view


if __name__ == '__main__':
    VectorCalculatorApp().run()
