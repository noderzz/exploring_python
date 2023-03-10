import pyautogui
import time
import keyboard

while True:
    # Hold down the right arrow key for 30 seconds
    pyautogui.keyDown('right')
    for i in range(30):
        time.sleep(1)
        if keyboard.is_pressed('esc'):
            break
    pyautogui.keyUp('right')
    if keyboard.is_pressed('esc'):
        break
    
    # Hold down the left arrow key for 30 seconds
    pyautogui.keyDown('left')
    for i in range(30):
        time.sleep(1)
        if keyboard.is_pressed('esc'):
            break
    pyautogui.keyUp('left')
    if keyboard.is_pressed('esc'):
        break
