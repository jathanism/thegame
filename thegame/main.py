#!/usr/bin/env python

# main.py - Kivy sample app

import kivy
kivy.require('1.0.6') 

from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='Hello, World!')

if __name__ == '__main__':
    MyApp().run()
