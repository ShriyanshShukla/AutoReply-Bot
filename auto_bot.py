from ai import ai
import pyautogui
import pyperclip
import time

pyautogui.click(1250, 1050)
time.sleep(1)

while True:
    pyautogui.moveTo(677, 233)
    pyautogui.dragTo(1872, 915, duration=1.0, button='left')

    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(673,850)
    time.sleep(1)
    
    text = pyperclip.paste()
    sender = text.split('\n')
    n = len(sender)

    if 'Shriyansh' in sender[n-1]:
        continue

    pyperclip.copy(ai(text))
    pyautogui.click(825, 960)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(1842, 954)