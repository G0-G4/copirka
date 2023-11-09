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
print(data)
data = data.replace('\n', '')
for c in data:
    controller.type(c)
    time.sleep(0.01)