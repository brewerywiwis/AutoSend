from sendMessage import wait, send
from avg import avg

total = []


def findTime(n):  # find average time which is used by send message
    for i in range(n):
        print("Round{}:".format(i))
        a = wait.count(message)
        t = float(str(a).split(":")[2])
        total.append(t)
        print(total)
        print(avg(total))


if __name__ == '__main__':  # main
    message = send.run("ECHO %message%").strip().decode("utf-8")
    # findTime(10)
    a = wait.count(message)
    print(float(str(a).split(":")[2]))
