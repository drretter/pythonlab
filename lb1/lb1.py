import time
import os

RED   = '\u001b[41m'
GREEN = '\u001b[42m'
BG_BLACK = '\u001b[40m'
BG_WHITE = '\u001b[47m'
RESET    = '\u001b[0m'


def flag(): #task 1
    h, w = 30, 50
    for y in range(h):
        for x in range(w):
            color = RED if (x - w * 0.45)**2 + (y - h / 2)**2 <= (h / 3)**2 else GREEN
            print(color + '  ', end='')
        print(RESET)


def pattern(n=3): #task 2
    pattern_block = [
        "111110",
        "100010",
        "101110",
        "101000",
        "101111"
    ]


    px = BG_BLACK + '  ' + RESET
    empty = BG_WHITE + '  ' + RESET
    for row in pattern_block:
        line = ''.join(px if ch == '1' else empty for ch in row * n)
        print(line)


def animation(): # task 3
    frame_small = [
        "       ",
        "       ",
        "  1 1  ",
        "  111  ",
        "   1   ",
        "       ",
        "       "
    ]

    frame_medium = [
        "       ",
        " 11 11 ",
        " 11111 ",
        "  111  ",
        "   1   ",
        "       ",
        "       "
    ]

    frame_large = [
        " 11 11 ",
        "1111111",
        "1111111",
        " 11111 ",
        "  111  ",
        "   1   ",
        "       "
    ]

    frames = [frame_small, frame_medium, frame_large, frame_medium]

    px = RED + '  ' + RESET
    empty = '  '

    print("\u001b[?25l", end="")

    for _ in range(5):
        for f in frames:
            os.system("cls")
            print("\u001b[H", end="")
            for row in f:
                print(''.join(px if ch == '1' else empty for ch in row))
            time.sleep(0.2)
        print("\u001b[?25h", end="")


def sequence(): # task 4
    file = open("sequence.txt", 'r')
    lines = [float(line.strip()) for line in file]
    file.close()
    
    half1 = lines[:125]
    half2 = lines[125:]
    
    sum1 = sum(abs(x) for x in half1)
    sum2 = sum(abs(x) for x in half2)

    total = sum1 + sum2

    percent1 = round(sum1 / total * 100, 2)
    percent2 = round(sum2 / total * 100, 2)

    print(f'Первые 125   : [{RED + "  " * int(percent1) + RESET}] {percent1}%')
    print(f'Последние 125: [{GREEN + "  " * int(percent2) + RESET}] {percent2}%')


def function(): # add task
    os.system("cls")

    h = 15
    orig_row = 17
    print("\u001b[1;1H y ^")

    for y in range(h, 0, -1):
        row = orig_row - y
        print(f"\u001b[{row};1H{y:2d} |")

    print(f"\u001b[{orig_row};1H 0 +{'-' * orig_row * 2}> x")
    x_labels = ' '.join(str(x) for x in range(h))
    print(f"\u001b[{orig_row + 1};5H{x_labels}")

    for x in range(h):
        y = 2 * x + 3
        if y <= h:
            row = orig_row - y
            col = 5 + x * 2
            print(f'\u001b[{row};{col}H{RED}*{RESET}')
    print(f"\u001b[{orig_row + 3};1H")

flag()
input("\nEnter для следующего задания...")
pattern(int(input("Введите число повторений узора: ")))
input("\nEnter для следующего задания...")
animation()
input("\nEnter для следующего задания...")
sequence()
input("\nEnter для следующего задания...")
function()