def collatz(num, steps):
    print(str(num) + ' - ' + str(steps))
    if num == 1:
        return

    steps += 1

    if num % 2 == 0:
        collatz(int(num / 2), steps)
    else:
        collatz(num * 3 + 1, steps)


print('Enter a number: ')
collatz(int(input()), 0)
