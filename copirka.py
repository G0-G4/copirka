from pynput import keyboard
import win32clipboard
import time

win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
controller = keyboard.Controller()
for i in range(3):
    print(i)
    time.sleep(1)
controller.type(data)
