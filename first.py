import pyautogui as ag
import time
import pyperclip

#https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga
#time.sleep(2)
ag.PAUSE = 0.3

ag.click(1185,17,clicks=1)
ag.click(1185,17,clicks=1)
ag.click(281,452,clicks=2)

time.sleep(0.5)

ag.click(400,452,clicks=1)
ag.press('enter')
ag.press('enter')
pyperclip.copy('iai mariana ')
ag.hotkey('ctrl','v')
ag.write('Como voce esta indo no trabalho? ')
time.sleep(3)
ag.click(1055,61)
ag.click(650,404)
time.sleep(2)
ag.click(1344,134)
ag.click(1228,47)
ag.moveTo(1100,72)

