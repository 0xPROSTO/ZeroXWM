import os
import shutil


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fclear():
    print("\033[H\033[J", end="")


def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except OSError:
        return 0
