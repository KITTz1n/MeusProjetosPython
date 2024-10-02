import pyautogui as py
import random
import time

time.sleep(5)   

mensagens = ["Estudar!","Vamos Estudar!"]

for i in range(25):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press("enter")