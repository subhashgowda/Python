# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 22:28:25 2019

@author: subha
"""

import pyttsx3

engine = pyttsx3.init()
say = input('enter')
engine.say(say)
engine.say("Im bored")

engine.runAndWait()