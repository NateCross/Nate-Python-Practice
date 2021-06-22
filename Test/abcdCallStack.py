def a():
    global penis
    penis += 1
    print('a() starts ' + str(penis))
    b()
    d()
    print('a() returns')


def b():
    print('b() starts')
    c()
    print('b() returns')


def c():
    print('c() starts')
    print('c() returns')


def d():
    print('d() starts')
    print('d() returns')


penis = 5
a()
print(penis)
