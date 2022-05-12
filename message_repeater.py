#!/bin/python
import pyautogui as gui
import time

number = int(input("number of message : "))
message = input("what is your message : ")

time.sleep(2)

for i in range(number):
    gui.typewrite(message)
    gui.press('ENTER')
    #time.sleep(1)