import sys
from time import sleep


def ft_progress(listy):
    for num in listy:
        yield num


listy = range(1000)
ret = 0
total = max(listy) + 1
bar_length = 30
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    completed = int(round(bar_length * elem / float(total)))
    percent = round(100 * elem / float(total), 1)
    bar = '=' * completed + '>' + ' ' * (bar_length - completed)
    sys.stdout.write(
        f'\rETA: {(total-elem)*0.01:.2f}s '
        f'[{percent:3.0f}%] [{bar}] '
        f'{elem}/{total} | elapsed time {elem*0.01:.2f}s'
    )
    sys.stdout.flush()
    sleep(0.01)
print()
print(ret)
