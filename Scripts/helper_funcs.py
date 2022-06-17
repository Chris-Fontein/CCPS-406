from textwrap3 import wrap
WIDTH = 80
def print_text(text):
    split = text.split("\n")
    for line in split:
        print("\n".join(wrap(line, WIDTH)))