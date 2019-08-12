from Function import Send

if __name__ == '__main__':  # main
    # message = send.run("ECHO %message%").strip().decode("utf-8")
    # findTime(10)
    # a = wait.count(message)
    message = input("Message: ").strip()
    number = int(input("Number: ").strip())
    delay = float(input("Delay: ").strip())
    round = int(input("Round: ").strip())
    Send.send_message(message, number, delay, round)
    # print(float(str(a).split(":")[2]))
