"""
Write a function that takes a list value as an argument and returns a string with all the items separated
by a comma and a space, with and inserted before the last item.
For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.
Be sure to test the case where an empty list [] is passed to your function.
"""
import sys

inputList = []
keyboardInput = ''
listIndex = 0

print('Enter "q" to quit.')
while True:
    print('Enter list item #{0}: '.format(str(listIndex)))  # Pycharm says this is the format to use, and use I shall
    keyboardInput = input()
    if keyboardInput == 'q':
        break
    inputList.append(keyboardInput)
    listIndex += 1

try:
    inputList[0]  # for checking if inputList is empty
    for i in inputList:
        if inputList.index(i) == len(inputList) - 1:  # Check if 'i' is at the last element of the list
            print('and ' + i)
            sys.exit()
        print(i, end=', ')

except IndexError:
    print("List is empty. Try again!")
