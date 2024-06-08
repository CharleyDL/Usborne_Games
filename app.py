#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By   : Charley ∆. Lebarbier
# Date Created : June 2024
# Licence      : CC BY-NC-ND 4.0
# ==============================================================================
"""
    This application uses the games from the Usborne books, adapting the BASIC 
    code into a python version.
 
    https://usborne.com/browse-books/features/computer-and-coding-books/

    GO BACK TO 80'S! ENJOY THE GAMES!

    Original code and rights belong to Usborne Publishing. This program is based
    on the original code provided in the book, which is copyrighted material
    owned by Usborne Publishing.

    Adaptations of the original code are allowed under the terms of the
    Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
    License (CC BY-NC-ND 4.0). You may download and share this program with
    others, but you may not modify it or use it for commercial purposes.
    Please credit Usborne Publishing as the original source of the code.

    For any enquiries regarding the original material, please contact Usborne
    Publishing, and for any enquiries regarding this adaptation, please contact 
    the author.
"""
# ==============================================================================

import time

import utils.functions as fct

from os import system
from terminaltexteffects.effects.effect_blackhole import Blackhole


def animated_header() -> None:
    system("clear")

    with open("./asset/app_header.txt", "r") as f:
        effect = Blackhole(f.read())
        with effect.terminal_output() as out:
            for frame in effect:
                out.print(frame)
    time.sleep(1)

def static_header() -> None:
    system("clear")

    with open("./asset/app_header.txt", "r") as f:
        print(f.read())



if __name__ == "__main__":
    animated_header()

    static_header()
    print(
    """
    1. Select a Game
    2. Language (Not available yet)
    """
    )

    choice_menu = fct.get_menu_action()
    if choice_menu == "1":
        print("HEHE WELCOME TO THE 80'S GAMES!")
    else:
        print("Language is not available yet.")