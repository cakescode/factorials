import sys
import os
sys.setrecursionlimit(10000005)
sys.set_int_max_str_digits(100000000)
loop_limit = 1000000
file_name = 'factorial.txt' # file used to input factorial (terminal has input limit)

def factorial(x): # func that factors an input using recursion
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def loop_factorial(x=1): # func to run factorial() in a limited loop
    for x in range(loop_limit):
        print(f'{x + 1}! = {factorial(x + 1)}\n')

def file_check(): # func to check if file is present, and to read file to return val of y
    if not os.path.isfile(file_name): # if file doesnt exist, make the file and exit
        file = open(file_name, 'w')
        file.write('')
        file.close()
        print('file created, please input factorial in factorial.txt')
        exit()

def file_read(): # func to read file and use contents as input for reverse_factorial()
    with open(file_name, 'r') as file: # read file to make y = whats in the file
        try: 
            y = file.readlines()
            print(f'{file_name} opened successfully')
            print(f'reading lines in {file_name}')
        finally: 
            file.close()
            print(f'{file_name} closed')
    if len(y) != 1: # if more or less than one line, exit program
        print(f'{file_name} must have only 1 entry (integer) to input')
        exit()
    print(f'loaded {len(y)} line from file') # debug: make sure it only loads 1 line
    y = [int(line.strip()) for line in y] # convert str in list to int in list
    y = ''.join(map(str, y)) # convert int in list to int
    print('searching...')
    return y

def reverse_factorial(): # func to find source for a factorial using brute force
    file_check() # checks if factorial.txt (used to input factorial) exists, if not its created
    y = file_read() # returns input from factorial.txt as y
    for x in range(loop_limit): # loop 1 to loop_limit or until factorial source is found
        if factorial(x) == int(y):
            print(f'{x}! = {y}') # print factorial source
            exit()
    # if loop_limit is reached and no source is found, prints the following:
    print('could not find factorial source! please expand search radius (loop_limit)')

def max_factorial(x, y=0): # what have i done.....
    if y == x:
        return x
    else:
        return (x * max_factorial(x, y + 1)) ** x

# run only one or the other:

print(max_factorial(int(input('input value to break your computer: '))))
# print(factorial(int(input('input value to factor: '))))
# loop_factorial()
# reverse_factorial()
