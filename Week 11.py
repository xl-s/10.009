# -*- coding: utf-8 -*-
"""
Created on Mon Apr 8 07:53:11 2019

@author: Xu Liang

Week 11 Problem Set
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
	
# Cohort Sessions 1
class Application1(Screen):

	def alternate(self, instance, touch):
		if instance.text == "Programming is fun":
			instance.text = "It is fun to program"
		else:
			instance.text = "Programming is fun"


# Cohort Sessions 2
class Application2(Screen):
    def detect(self, instance, touch):
    	if abs(touch.dx) > abs(touch.dy):
    		if touch.dx < 0:
    			instance.text = "Slide Left"
    		else:
    			instance.text = "Slide Right"
    	else:
    		if touch.dy < 0:
    			instance.text = "Slide Down"
    		else:
    			instance.text = "Slide Up"


# Cohort Sessions 3
class Application3(Screen):
	pass


# Cohort Sessions 4
class Application4(Screen):
	pass


class Application(ScreenManager):
	pass


class MenuBar(BoxLayout):
	pass


class ButtonScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.lay = GridLayout(cols=2)

	def addButs(self, num):
		for i in range(num):
			self.lay.add_widget(Button())
		self.add_widget(self.lay)


class Week11App(App):
	title = '👌👀👌👀👌👀👌👀👌👀 good shit go౦ԁ sHit👌 thats ✔ some good👌👌shit right👌👌there👌👌👌 right✔there ✔✔if i do ƽaү so my self 💯 i say so 💯 thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ💯 👌👌 👌НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ👌 👌👌 👌 💯 👌 👀 👀 👀 👌👌Good shit'
	def build(self):
		return MenuBar()


if __name__ == "__main__":
	Week11App().run()