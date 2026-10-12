import time
import os

RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
RESET = '\u001b[0m'
HOME = '\u001b[H'
ERASE_ALL = '\u001b[1J'


def flag():
    for i in range(6):
        if i in [0, 5]:
            print(f'{RED}{"   " * 10}{RESET}')     #первая и последняя строки флага красного цвета
        elif i in [1, 4]:
            print(f'{WHITE}{"   " * 10}{RESET}')     #2 и 5 строки флага белые
        else:
            print(f'{BLUE}{"   " * 10}{RESET}')     #две центральные строки флага синие


def draw_uzor():
    height = 5     #высота узора
    width = 9     #условная ширина узора
    center = width // 2     #местоположение вершины узора
    colors = [84, 69, 226, 15]
    for color in colors:
        print(f'{ERASE_ALL}{HOME}')
        COLOR = f'\u001b[48;5;{color}m'     #текущий цвет узора
        print(f'{' ' * (center * 2 * width - 1)}{COLOR}{'   '}{RESET}')     #рисовка вершины узора
        for line in range(height):
            skip = [1] + [1 + 2 ** i for i in range(1,height)]     #задание пробелов между ветвями узора
            print(f'{' ' * (center * 2 * width - (2 ** line + 1) - int(skip[line]//2))}{COLOR}{' ' * (2 ** line + 1)}{RESET}{' ' * skip[line]}{COLOR}{' ' * (2 ** line + 1)}{RESET}')
        time.sleep(2)


def animation():
    bar_width = 4
    for proc in range(1, bar_width+1):
        bar = '#' * 25 *proc + '-' * 25 * (bar_width - proc)
        print(f'[{bar}] {proc*25}%')
        time.sleep(2)
        os.system("clean")
        print(f'{HOME}')


def file_process():
    file = open('C:/Users/kuzmi/Desktop/sequence.txt')
    greater_5 = []     #список чисел > 5
    less_5 = []     #список чисел < 5 и >= 0
    for i in file:
        if float(i) > 5:
            greater_5.append(i)
        elif 0 <= float(i) < 5:
            less_5.append(i)
    file.close()
    print(f'{BLUE}{' ' * int(len(greater_5) / (len(greater_5) + len(less_5)) * 100)}{RESET}')
    print(f'{RED}{' ' * int(len(less_5) / (len(greater_5) + len(less_5)) * 100)}{RESET}')


print(f'{ERASE_ALL}{HOME}')   
flag()
time.sleep(2)
print(f'{ERASE_ALL}{HOME}')
draw_uzor()
print(f'{ERASE_ALL}{HOME}')
animation()
print(f'{ERASE_ALL}{HOME}')
file_process()