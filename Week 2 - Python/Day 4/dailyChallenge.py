def tryExcept():
    try:
        res = 5 / 0
        print(res)
    except ZeroDivisionError:
        print("You cant divide by 0")

tryExcept()