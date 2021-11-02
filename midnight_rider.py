# Midnight Rider

import random
import sys
import textwrap
import time
import midnight_rider_text

# A text-based game of intrigue and illusion

# CONSTANTS
MAX_FUEL = 50
MAX_TOFU = 3
MAX_HUNGER = 50

class Game:
    """Represent our game engine
    Attribute:
        done: describes if the game is
            finished or not - bool
        distance_travelled: describe the distance that we've travelled so far this game,
            in units
        amount_of_tofu: how much tofu we have left in our inventory
            agents_distance: describes the distance between the player and the agents
        fuel: describes the amount of fuel remaining
            starts off at 50
        hunger: describes how hungry our player is which is represented from 0-50,
            if a number reaches beyond 50, it's game over
    """
    def __init__(self):
        self.done = False
        self.distance_travelled = 0
        self.amount_tofu = MAX_TOFU
        self.agents_distance = -20
        self.fuel = MAX_FUEL
        self.hunger = 0


    def introduction(self) -> None:
        """Print the introduction text"""
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect."""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    def show_choices(self) -> None:
        """Show the user their choices"""
        time.sleep(1)
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choice(self) -> None:
        """Gets the user's choice and changes
        the environment"""
        # Get the user's response
        user_choice = input().strip(",.?!").lower()

        # Based on their choice, change the attributes
        # of the class



        agents_distance_now = random.randrange(7, 15)

        # TODO: Implement quick travelling
        if user_choice == "a":
            # Consume one tofu IF and ONLY we have at least ONE available
            if self.amount_tofu > 0:
                self.amount_tofu -= 1
                self.hunger = 0
                # Give the player some feedback
                # TODO: Add text to midnight_rider_text.py
                print(midnight_rider_text.EAT_TOFU)
            else:
                # Tell the player they do not have tofu
                print(midnight_rider_text.NO_TOFU)
        if user_choice == "b":
            # Move the player
            player_distance_now = random.randrange(3, 8)
            self.distance_travelled += player_distance_now

            # Move agents
            self.agents_distance += agents_distance_now - player_distance_now

            # Burn fuel
            self.fuel -= random.randrange(5, 10)

            # Give player feedback
            print(f"------!!!")
            print(f"------You travelled {player_distance_now}kms.\n")
        elif user_choice == "c":

    def upkeep(self) -> None:
        """ Give the user reminders of hunger""""""
        pass

            # Move the player
            player_distance_now = random.randrange(10, 16)
            self.distance_travelled += player_distance_now
            # Move agents
            self.agents_distance += agents_distance_now - player_distance_now
            # Burn fuel
            self.fuel -= random.randrange(5, 11)
            # Give player feedback
            print(f"------ZOOOOOOOOOOOOOM!!!")
            print(f"------You travelled {player_distance_now}kms.\n")
        elif user_choice == "d":
            self.fuel = MAX_FUEL

        if user_choice == "d":

            self.fuel = MAX_FUEL

            # Decide how far the agents go
            self.agents_distance += random.randrange(6, 15)

            # Give the user feedback
            print(midnight_rider_text.REFUEL)
        elif user_choice == "e":

            print("---Status Check---")
            print(f"Distance Travelled: {self.distance_travelled} units")
            print(f"Fuel remaining: {self.fuel} 50 litres")
            print(f"Tofu Pieces Left: {self.amount_tofu}")
            print(f"Agent's Distance:{abs(self.agents_distance)} units behind")
            print("------")
            time.sleep(2)
        elif user_choice == "q":
            self.done = True

def main() -> None:
    game = Game()   # starting a new game
    # game.introduction()

    while not game.done:
        game.upkeep() 
        game.show_choices()
        game.get_choice()
        # TODO: Check win/lose conditions




if __name__ == "__main__":
    main()