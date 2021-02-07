import time
import pyautogui
import keyboard
import PySimpleGUI as ps

# consider using python 3.7 for some libraries

#pysimplegui setup
GUITitle = "CSGO Clicker"
ps.theme("DarkGreen3")
layout = [
    [ps.Text(text="Waiting for hotkey",key="-Text-")],
    [ps.Button("Set Hotkey")]
]
window = ps.Window(GUITitle, layout, finalize=True)

#program setup
key = "up"
firePoint = (pyautogui.size()[0] / 2 + 1, pyautogui.size()[1] / 2 + 1)
keyDown = False
running = True

while running:
    event, values = window.read(timeout=0.1)
    if(event == ps.WINDOW_CLOSED):
        running = False
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

window.close()