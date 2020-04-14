import string
import sys

if len(sys.argv) != 3 \
        or sys.argv[1].isnumeric() \
        or not sys.argv[2].isnumeric():
    print('ERROR')
    exit()

phrase = sys.argv[1]
result = [
    word.strip(string.punctuation)
    for word in phrase.split(' ')
    if len(word) > int(sys.argv[2])
]

print(result)
