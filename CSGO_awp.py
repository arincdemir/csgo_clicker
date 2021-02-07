import time
import pyautogui
import keyboard
import PySimpleGUI as ps

## consider using python 3.7 for some libraries

key = "up"
firePoint = (pyautogui.size()[0] / 2 + 1, pyautogui.size()[1] / 2 + 1)
keyDown = False

#comment comment feature comment
#main comment comment main

while True:
    print("not listening")
    if(keyboard.is_pressed(key) and keyDown == False):
        keyDown = True
        initialPixel = pyautogui.screenshot().getpixel(firePoint)
        while pyautogui.screenshot().getpixel(firePoint) == initialPixel:
            print("listening")
            time.sleep(0.01)
            if(keyboard.is_pressed(key) and keyDown == False):
                keyDown = True
                break
            elif(not keyboard.is_pressed(key)):
                keyDown = False
        else:
            pyautogui.click()
    elif(not keyboard.is_pressed(key)):
        keyDown = False

    time.sleep(0.01)

    def mainFunc():
        pass
