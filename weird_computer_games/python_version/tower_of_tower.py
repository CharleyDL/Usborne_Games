#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By   : Charley ∆. Lebarbier
# Date Created : June 2024
# Licence      : CC BY-NC-ND 4.0
# ==============================================================================
"""
    Tower of Terror
    Python version based on BASIC code from the book
    'WEIRD COMPUTER GAMES' from Usborne Publishing.

    https://usborne.com/browse-books/features/computer-and-coding-books/

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

import os
import sys
import random
import tty
import termios

from os import system
from terminaltexteffects.effects.effect_expand import Expand
from terminaltexteffects.effects.effect_middleout import MiddleOut

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                             '..', '..')))
import utils.functions as fct


class TowerOfTerror:

    def __init__(self) -> None:
        """Initialize the Tower of Terror game with default settings."""
        self.enemy = ["SKELETON", "GHOST", "HEADLESS AXEMAN"]
        self.hour = 9
        self.minute = 20
        self.room = 0
        self.floor = 0
        self.great_fear = 0
        self.pulse = 50
        self.trap = random.randint(1, 9)
        self.user_action = ""

    def encounter(self) -> int:
        """
        Simulate an encounter with an enemy.

        Returns:
            int: The strength of the encountered enemy.
        """
        enemy_type = random.randint(1, 3)
        enemy = self.enemy[enemy_type - 1]
        floor = self.room // 5
        strength = random.randint(1, 5) + floor + enemy_type * 2
        self.great_fear = 1

        with open(
            "./asset/games_header/weird_computer_header/tower_of_terror/encounter_header.txt", 
            "r",
        ) as f:
            content = f.read().replace("{enemy}", enemy)
            system("clear")
            print(content)

        ## -- Continue after reading the encounter
        choice_pres = self.get_game_action().lower()
        if choice_pres == "c":
            return strength

    def game_menu(self) -> None:
        """Display the game menu."""
        print(
            """
            1. Start
            2. Language (Not available yet)
            3. Exit
        """
        )

    def get_game_action(self) -> str:
        """
        Get the user's action from the game menu.

        Returns:
            str: The user's chosen action.
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            while True:
                key = sys.stdin.read(1)
                if key.lower() in ["g", "r", "q", "c"]:
                    return key
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def handle_input(self) -> None:
        """Handle user input to either retreat, go on, or quit."""
        print("RETREAT OR GO ON (R/G)")
        self.user_action = self.get_game_action().lower()

        if self.user_action == "q":  # - Quit the game
            fct.clean_exit()
        elif self.user_action == "r":  # - Retreat
            self.room -= 1
            self.pulse -= 5
            if self.room < 0:
                self.room = 0
        elif self.user_action == "g":  # - Go on
            ## - Random encounter an enemy or pursue
            if random.random() > 0.6:
                encounter = self.encounter()
                if self.great_fear == 1:
                    self.pulse += encounter * 2
                    self.pulse -= 1
                    self.room += 1
            else:
                self.room += 1

        ## - Update the time
        self.minute += random.randint(1, 3)
        if self.minute > 59:
            self.minute -= 60
            self.hour += 1

    def header_main_screen(self) -> None:
        """Display the main screen header."""
        with open(
            "./asset/games_header/weird_computer_header/tower_of_terror/tot_header.txt", 
            "r",
        ) as f:
            effect = MiddleOut(f.read())
            with effect.terminal_output() as out:
                for frame in effect:
                    out.print(frame)

    def status(self) -> None:
        """Print the current status of the game."""
        ## -- Update the floor
        self.floor = int(self.room / 5)

        print("   - STATUS -")

        if self.room == 30:  # - Check if game is won (room 30 reached)
            print("WELL DONE")
            print("\nQUIT (Q)")
            fct.end_game()
        elif self.hour == 12:  # - Check if midnight => Game Over
            print("IT'S MIDNIGHT! TOO LATE!")
            print("\nQUIT (Q)")
            fct.end_game()
        elif self.pulse > 150:  # - Check if pulse is too high => Game Over
            print("YOU HAVE GONE MAD AND LEAPT FROM A WINDOW!")
            print("\nQUIT (Q)")
            fct.end_game()
        elif self.floor == self.trap and random.random() > 0.5:  # - Check if trap door
            print("YOU FELL THROUGH A TRAP DOOR!")
            self.room -= 5
            self.pulse -= 10
        elif self.pulse < 40:  # - Adjust pulse rate
            self.pulse = 40
        else:
            ## -- Display the regular status and floor/room
            print(
                f"\n⧖ TIME : {self.hour}:{self.minute} PM\
                    ♥︎ PULSE RATE : {self.pulse} "
            )

            if self.floor == 0:
                print(f"\n\nYOU ARE ON THE GROUND FLOOR IN ROOM {self.room}")
            elif self.floor == 6:
                print(f"\n\nYOU ARE ON THE TOP FLOOR IN ROOM {self.room}")
            else:
                print(f"\n\nYOU ARE ON {self.floor} IN ROOM {self.room}")

    def story_command(self) -> None:
        """Display the game story and commands."""
        with open(
            "./asset/games_header/weird_computer_header/tower_of_terror/story_header.txt", 
            "r"
        ) as f:
            effect = Expand(f.read())
            with effect.terminal_output() as out:
                for frame in effect:
                    out.print(frame)

    def main_loop(self) -> None:
        """Run the main game loop."""

        ## -- Display the Main Screen and its menu (Start, Language, Exit)
        system("clear")
        self.header_main_screen()
        self.game_menu()

        ## -- User Choice : Start, Language, Exit
        choice_menu = fct.get_menu_action()
        if choice_menu == "1":
            ## -- Game story and command
            system("clear")
            self.story_command()

            ## -- User Choice : Quit or Continue
            choice_pres = self.get_game_action().lower()
            if choice_pres == "c":
                while True:
                    system("clear")
                    self.status()
                    self.handle_input()
            elif choice_pres == "q":
                fct.clean_exit()
        elif choice_menu == "2":
            pass  ## -- Language not available yet
        elif choice_menu == "3":
            fct.clean_exit()


if __name__ == "__main__":
    tot = TowerOfTerror()
    tot.main_loop()
