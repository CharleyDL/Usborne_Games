import sys

from os import system
from termios import tcgetattr, tcsetattr, TCSADRAIN
from tty import setraw


def clean_exit() -> None:
    """Exit the program"""
    system("clear")
    exit()


def get_menu_action() -> str:
    """Get the user menu action"""
    fd = sys.stdin.fileno()
    old_settings = tcgetattr(fd)
    try:
        setraw(sys.stdin.fileno())
        while True:
            key = sys.stdin.read(1)
            if key in ["1", "2", "3"]:
                return key
    finally:
        tcsetattr(fd, TCSADRAIN, old_settings)


def end_game() -> str:
    """Get the user menu action"""
    fd = sys.stdin.fileno()
    old_settings = tcgetattr(fd)
    try:
        setraw(sys.stdin.fileno())
        while True:
            key = sys.stdin.read(1)
            if key in ["q", "Q"]:
                clean_exit()
    finally:
        tcsetattr(fd, TCSADRAIN, old_settings)
