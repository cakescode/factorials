import sys
import os
sys.setrecursionlimit(10000005)
sys.set_int_max_str_digits(100000000)
loop_limit = 1000000

def factorial(x): # func that factors an input using recursion
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def loop_factorial(x=1): # func to run factorial() in a limited loop
    for x in range(loop_limit):
        print(f'{x + 1}! = {factorial(x + 1)}\n')

def reverse_factorial(): # func to find source for a factorial using brute force
    file_name = 'factorial.txt' # file used to input factorial (terminal has input limit)
    if not os.path.isfile(file_name): # if file doesnt exist, make the file and exit
        file = open(file_name, 'w')
        file.write('')
        file.close()
        print('file created, please input factorial in factorial.txt')
        exit()
    with open(file_name, 'r') as file: # read file to make y = whats in the file
        try: 
            y = file.readlines()
            print('file opened successfully')
            print('reading lines in factorial.txt')
        finally: 
            file.close()
            print('factorial.txt closed')
    print(f'loaded {len(y)} lines from file') # debug: make sure it only loads 1 line
    if len(y) != 1: # if more or less than one line, exit program
        print('factorial.txt must have 1 entry (integer) to input')
        exit()
    y = [int(line.strip()) for line in y] # convert str in list to int in list
    print('searching...')
    y = ''.join(map(str, y)) # convert int in list to int
    for x in range(loop_limit): # loop 1 to loop_limit or until factorial source is found
        if factorial(x) == int(y):
            print(f'{x}! = {y}') # print factorial source
            exit()
    # if loop_limit is reached and no source is found, prints the following
    print('could not find factorial source! please expand search radius')

loop_factorial()
# reverse_factorial()