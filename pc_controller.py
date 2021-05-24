import os 

import pyautogui

# @returns PIL image
def get_screen():
    screenshot = pyautogui.screenshot()
    return screenshot

def pc_off():
    os.system('shutdown -s')
    