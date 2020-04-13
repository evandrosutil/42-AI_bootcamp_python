import sys

if len(sys.argv) > 2:
    print('ERROR')
    exit()

try:
    number = int(sys.argv[1])
except ValueError:
    print('ERROR')
    exit()

if number == 0:
    print("I'm Zero")
elif number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
