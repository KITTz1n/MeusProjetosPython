import pyautogui as py
import random
import time

time.sleep(5)   

mensagens = ["vamo querer!","desumilde!"]

for i in range(5):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press("enter")