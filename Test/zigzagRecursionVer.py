import time, sys


def printStuff(indent, indentIncreasing):
    print(' ' * indent, end='')
    print('********')
    time.sleep(0.1)

    if indentIncreasing:
        indent += 1
        if indent == 20:
            indentIncreasing = False

    else:
        indent -= 1
        if indent == 0:
            indentIncreasing = True

    printStuff(indent, indentIncreasing)


try:
    printStuff(0, True)
except KeyboardInterrupt:
    sys.exit()
