import time
import pyautogui
import keyboard
import PySimpleGUI as ps

# consider using python 3.7 for some libraries

#pysimplegui setup
GUITitle = "CSGO Clicker"
ps.theme("DarkGreen3")
textBackground = "gray10"
layout = [
    [ps.Text(text="Set a hotkey by pressing the button.",key="-Text-", size=(50,1),font=("default", 15, "bold"), background_color=textBackground)],
    [ps.Button("Set Hotkey", size=(10,1), font=("default", 12, "bold"))]
]
window = ps.Window(GUITitle, layout, finalize=True)

#program setup
key = "up"
firePoint = (pyautogui.size()[0] / 2 + 1, pyautogui.size()[1] / 2 + 1)
keyDown = False
running = True

#gets the initial hotkey
event, values = window.read()
if(event == ps.WINDOW_CLOSED):
        running = False
elif(event == "Set Hotkey"):
    window["-Text-"].update("Press key")
    window.Finalize()
    key = keyboard.read_key()
print(key)

#the program
window["-Text-"].update("Press hotkey after placing your crosshair")
while running:
    event, values = window.read(timeout=0.1)
    if(event == ps.WINDOW_CLOSED):
        running = False
    elif(event == "Set Hotkey"):
        window["-Text-"].update("Press key")
        window.Finalize()
        key = keyboard.read_key()
    
    print("not listening")

    if(keyboard.is_pressed(key) and keyDown == False):
        window["-Text-"].update("Watching the crosshair")
        event, values = window.read(timeout=0.1)
        if(event == ps.WINDOW_CLOSED):
            running = False
        keyDown = True
        initialPixel = pyautogui.screenshot().getpixel(firePoint)
        while pyautogui.screenshot().getpixel(firePoint) == initialPixel and running:
            print("listening")
            time.sleep(0.01)
            if(keyboard.is_pressed(key) and keyDown == False):
                keyDown = True
                break
            elif(not keyboard.is_pressed(key)):
                keyDown = False
        else:
            pyautogui.click()
        window["-Text-"].update("Press hotkey after placing your crosshair")

    elif(not keyboard.is_pressed(key)):
        keyDown = False

    time.sleep(0.01)

window.close()