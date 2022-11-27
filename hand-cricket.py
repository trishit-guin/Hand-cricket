import random

l = [1, 2, 3, 4, 5, 6]
a = random.choice(l)


def toss():
    ch = input("odd or even")
    if ch in "evenEVEN":
        n = int(input("enter your number: "))
        print("computer's number", a)
        if (n + a) % 2 == 0:

            bat_ball = input("enter bat or ball: ")
            if bat_ball == "bat":
                bat()
            else:
                ball()
        else:
            q = ["bat", "ball"]
            com_ch = random.choice(q)
            print("computer chose to", com_ch)
            if com_ch == "bat":
                ball()
            else:
                bat()
    elif ch in "oddODD":
        n = int(input("enter your number: "))
        print("computer chose", a)
        if (n + a) % 2 != 0:
            bat_ball = input("enter bat or ball: ")
            if bat_ball == "bat":
                bat()
            else:
                ball()
        else:
            q = ["bat", "ball"]
            com_ch = random.choice(q)
            print("computer chose to", com_ch)
            if com_ch == "bat":
                ball()
            else:
                bat()


p1 = 0


def bat():
    global p1

    while True:
        n1 = int(input("enter your shot: "))
        n2 = random.choice(l)
        print("computer threw", n2)
        if n1 != n2:
            p1 = p1 + n1
        else:
            print("you are out and computer's target is =>", p1 + 1)
            s_ball()
            break


p2 = 0


def ball():
    global p2

    while True:
        n3 = int(input("throw your ball: "))
        n4 = random.choice(l)
        print("computer hits", n4)
        if n3 != n4:
            p2 = p2 + n4
        else:
            print("you took wicket and your target is =>", p2 + 1)
            s_bat()
            break


def s_bat():
    global p1

    while True:
        n5 = int(input("enter your shot: "))
        n6 = random.choice(l)
        print("computer threw", n6)
        if n5 != n6:
            p1 = p1 + n5
            if p1 >= p2 + 1:
                print("you win")
                break
        else:
            print("computer wins")
            break


def s_ball():
    global p2

    while True:
        n7 = int(input("Throw your ball: "))
        n8 = random.choice(l)
        print("computer threw", n8)
        if n7 != n8:
            p2 = p2 + n8
            if p2 >= p1 + 1:
                print("computer wins")
                break
        else:
            print("you took a wicket")
            print("you win")
            break


toss()