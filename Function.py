from datetime import datetime, timedelta
import time
import pyautogui as pg
import os
import keyboard
import subprocess
from statistics import mean


class benchmark:
    def count(message):  # count time for send message
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

    def find_time(n):  # find average time which is used by send message
        total = []
        for i in range(n):
            print("Round{}:".format(i))
            a = benchmark.count(message)
            t = float(str(a).split(":")[2])
            total.append(t)
        return mean(total)


class Send:
    def run(command):  # check message from cmd
        output = subprocess.check_output(command, shell=True)
        return output

    def send_message(message, n, d, r):  # send message
        os.system("echo Hello")  # check program
        print(datetime.now())  # check program
        print("message = " + message)  # check program
        op = open("C:\\Users\\brewd\\PycharmProjects\\SendLine\\Location.txt",
                  "r")  # instead of dir with your location file
        line = op.readline().strip()
        while line:
            if "@" in line:
                word = line[line.find("(") + 1:-1].split(",")
                x1 = int(word[0][word[0].find("=") + 1:].strip())
                y1 = int(word[1][word[1].find("=") + 1:].strip())
                print("x={},y={}".format(x1, y1))  # check x,y position on screen
                if line[0] == "S":
                    pg.click(button="left", x=x1, y=y1)
                    time.sleep(1.5)
                elif line[0] == "D":
                    pg.click(button="left", clicks=2, x=x1, y=y1)
                    time.sleep(1.5)
            elif "input" in line:
                for j in range(r):
                    for i in range(n):
                        keyboard.write("{}".format(message + (message[-1] * i)))
                        pg.press("enter")
                        #time.sleep(d)
                    for i in range(n - 2, -1, -1):
                        keyboard.write("{}".format(message + (message[-1] * i)))
                        pg.press("enter")
                        #time.sleep(d)
                break
            line = op.readline().strip()
        os.system("echo Process complete!")
        op.close()
