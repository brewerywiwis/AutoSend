import time
from threading import Thread
import keyboard
import pyautogui as pg

database = []
state = "wait"


def record():
    def thread_run():
        global state
        while state == "wait":
            time.sleep(0.1)
            if state == "end":
                break

    global state
    keyboard.on_press(check_key, suppress=True)
    t1 = Thread(target=thread_run())
    t1.start()
    t1.join()
    state = "wait"


# check location of mouse
def check_key(call):
    global g_state
    g_state = "start"
    sm = str(call)
    key = sm[sm.find("(") + 1: sm.find(" ")].lower()
    p = pg.position()
    if key == "s":
        database.append(f"S@{p}")
        print(f"Add {p} completely.")
    elif key == "d":
        database.append(f"D@{p}")
        print(f"Add {p} completely.")
    elif key == "esc":
        global state
        keyboard.unhook_all()
        op = open("C:\\Users\\brewd\\PycharmProjects\\SendLine\\Location.txt", "w")
        for i in database:
            op.write(f"{i}\n")
        op.write("input\n")
        op.close()
        state = "end"
        print("Complete record!")
    else:
        pass


if __name__ == "__main__":
    seq = "*********************"
    while True:
        cmd = input("Please input command: ").strip().lower()
        if cmd == "clean":
            database = []
            op = open("C:\\Users\\brewd\\PycharmProjects\\SendLine\\Location.txt", "w")
            op.write("")
            op.close()
            print(seq,"Clean database successfully!!!",seq,sep="\n")
        elif cmd == "record":
            record()
        elif cmd == "exit":
            print(seq, "THANK YOU, GOOD BYE.", seq, sep="\n")
            break
        elif cmd == "view":
            op = open("C:\\Users\\brewd\\PycharmProjects\\SendLine\\Location.txt", "r")
            line = op.readline().strip()
            print(seq)
            while line:
                print(line)
                line = op.readline().strip()
            print(seq)
        elif cmd == "help":
            print(seq, "Command Available:\n\
                Clean\n\
                Record\n\
                View\n\
                Exit", seq, sep="\n")
        else:
            print("******pls input the correct command or Help******")
