#!/usr/bin/env python

# paint.py - Kivy paint app

import kivy
kivy.require('1.5.1')

from random import random
from kivy.app import App
from kivy.interactive import InteractiveLauncher
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print touch
        color = (random(), random(), random())
        with self.canvas:
            Color(*color)
            d = 30.
            Ellipse(pos=(touch.x -d / 2, touch.y - d /2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        print touch
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        parent = Widget()
        painter = MyPaintWidget()
        clear_button = Button(text='Clear')
        parent.add_widget(painter)
        parent.add_widget(clear_button)

        def clear_canvas(obj):
            painter.canvas.clear()

        clear_button.bind(on_release=clear_canvas)

        return parent

if __name__ == '__main__':
    MyPaintApp().run()
    #i = InteractiveLauncher(MyPaintApp())
    #i.run()
