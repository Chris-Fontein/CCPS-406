'''Useful functions for anywhere in the game'''
from time import sleep
#pip install textWrap3
from textwrap3 import wrap

WIDTH = 80

def print_text(text = ""):
    '''Print out the text given with proper formatting'''
    if not text:
        print()
        sleep(0.1)
        return

    split = text.split("\n")
    for line in split:
        para_lines = wrap(line, WIDTH)
        for para_line in para_lines:
            print(para_line)
            sleep(0.1)


