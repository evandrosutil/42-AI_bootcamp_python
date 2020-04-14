import string
import sys

if len(sys.argv) != 3:
    print('ERROR')
    exit()
phrase = sys.argv[1]
for i in phrase:
    if i.isdigit():
        print('ERROR')
        exit()
try:
    length = int(sys.argv[2])
except ValueError:
    print('ERROR')
    exit()

result = [
    word.strip(string.punctuation)
    for word in phrase.split(' ')
    if len(word) > length
]

print(result)
