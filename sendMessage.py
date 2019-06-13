from datetime import datetime, timedelta
import time
import pyautogui as pg
import os
import keyboard
import subprocess


class wait:
    def count(message): #count time for send message
        start_time = time.monotonic()
        exec("mes = message\nsend.sendMessage(mes)")
        end_time = time.monotonic()
        return timedelta(seconds=end_time - start_time)

    def wait_time(wtime):
        sec1 = wtime[0] * 3600 + wtime[1] * 60 + wtime[2]
        cur = [float(i) for i in str(datetime.today().time()).split(":")]
        sec2 = cur[0] * 3600 + cur[1] * 60 + cur[2]
        while sec2 < sec1:
            cur = [float(i) for i in str(datetime.today().time()).split(":")]
            sec2 = cur[0] * 3600 + cur[1] * 60 + cur[2]
        print("Arrived!")


class send:
    def run(command): #check message from cmd
        output = subprocess.check_output(command, shell=True)
        return output

    def sendMessage(message): #send message
        os.system("echo Hello") #check program
        print(datetime.now()) #check program
        print("message = " + message) #check program
        op = open("C:\\Users\\brewd\\PycharmProjects\\SendLine\\Location", "r") #instead of dir with your location file
        line = op.readline().strip()
        while line:
            if "Point" in line:
                point = line.split(":")
                word = point[1][point[1].find("(") + 1:-1].split(",")
                x1 = int(word[0][word[0].find("=") + 1:].strip())
                y1 = int(word[1][word[1].find("=") + 1:].strip())
                #print("x={},y={}".format(x1, y1)) #check x,y position on screen
                pg.click(button="left", x=x1, y=y1)
                time.sleep(1.07)
            elif "input" in line:
                keyboard.write("{}".format(message))
                pg.press("enter")
                break
            line = op.readline().strip()
        op.close()
