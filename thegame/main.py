#!/usr/bin/env python

# main.py - Kivy sample app

import kivy
kivy.require('1.0.6') 

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class MyApp(App):
    def build(self):
        parent = Widget()
        message = Label(text='', font_size='75sp')
        btn = Button(text='Hello, World!')
        parent.add_widget(btn)
        parent.add_widget(message)

        def update_message(self, *args, **kwargs):
            msg = "YOU WIN!"
            print msg
            message.text = msg

        def clear_message(self, *args, **kwargs):
            message.text = ''

        btn.bind(on_press=clear_message, on_release=update_message)
        return parent


if __name__ == '__main__':
    MyApp().run()
