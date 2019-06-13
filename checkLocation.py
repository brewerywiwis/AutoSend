import keyboard
import pyautogui as pg
#check location of mouse
if __name__ == "__main__":
    while True:
        keyboard.wait('C')
        print(pg.position())