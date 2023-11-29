# This program is ment to be an experiment to learn how to use Tkinter so that I can make my programs GUI based
# Author: Atticus Blunt
# Date Started: Nov 28 2023

import tkinter as tk
import random
import time

# Define a class for the Clicker Game
class ClickerGame:
    # Constructor to initialize the game
    def __init__(self, root):
        # Store the root window
        self.root = root
        # Set the window title
        self.root.title("Random Clicker Game")

        # Set the size of the window
        self.root.geometry("1200x800")

        # Initialize variables
        self.click_count = 0
        self.current_dice = 4
        self.upgrade_dice_cost = 80
        self.clicks_per_second = 0
        self.upgrade_clicks_per_second_cost = 400
        self.rollNumber = None

        # Create and configure label to display click count
        self.click_label = tk.Label(root, text="Clicks: 0", font=("Helvetica", 16))
        self.click_label.place(x=50, y=20)

        # Create click button
        self.click_button = tk.Button(root, text=f"Current Dice: d{self.current_dice}", command=self.on_click)
        self.click_button.place(x=50, y=50)

        # Create roll label
        self.roll_label = tk.Label(root, text=f"Rolled: {self.rollNumber}", font=("Helvetica", 16))
        self.roll_label.place(x=170, y=20)

        # Create upgrade dice button lable
        self.upgrade_dice_button_label = tk.Label(root, text="Upgrade Dice?", font=("Helvetica", 16))
        self.upgrade_dice_button_label.place(x=50, y=100)

        # Create upgrade dice button
        self.upgrade_dice_button = tk.Button(root, text=f"Cost: {self.upgrade_dice_cost}", command=self.on_click_button)
        self.upgrade_dice_button.place(x=50, y=130)

        # Create clicks per second label
        self.upgrade_clicks_per_second_label = tk.Label(root, text=f"Clicks Per Second: {self.clicks_per_second}", font=("Helvetica", 16))
        self.upgrade_clicks_per_second_label.place(x=240, y=100)

        # Create upgrade clicks per second button
        self.upgrade_clicks_per_second_button = tk.Button(root, text=f"Cost: {self.upgrade_clicks_per_second_cost}", command=self.on_click_second_button)
        self.upgrade_clicks_per_second_button.place(x=240, y=130)

    # Event handler for the click button
    def on_click(self):
        # Update click count and label text
        self.rollNumber = random.randint(1,self.current_dice)
        self.roll_label.config(text=f"Rolled: {self.rollNumber}")

        self.click_count += self.rollNumber
        self.click_label.config(text=f"Clicks: {self.click_count}")

    # Event handler for the upgrade dice button
    def on_click_button(self):
        # check if the user can afford the upgrade
        if self.click_count >= self.upgrade_dice_cost:
            # change variables
            self.current_dice += 2
            self.click_count -= self.upgrade_dice_cost
            self.upgrade_dice_cost = round(self.upgrade_dice_cost * 2.15)

            # update the labels/buttons
            self.click_label.config(text=f"Clicks: {self.click_count}")
            self.click_button.config(text=f"Current Dice: d{self.current_dice}")
            self.upgrade_dice_button.config(text=f"Cost: {self.upgrade_dice_cost}")

    # Event handler for the upgrade clicks per second button
    def on_click_second_button(self):
        if self.click_count >= self.upgrade_clicks_per_second_cost:
            # change variables
            self.clicks_per_second += 1
            self.click_count -= self.upgrade_clicks_per_second_cost
            self.upgrade_clicks_per_second_cost = round(self.upgrade_clicks_per_second_cost * 3.75)

            # update the labels/buttons
            self.click_label.config(text=f"Clicks: {self.click_count}")
            self.upgrade_clicks_per_second_label.config(text=f"Clicks Per Second: {self.clicks_per_second}")
            self.upgrade_clicks_per_second_button.config(text=f"Cost: {self.upgrade_clicks_per_second_cost}")



        # Function that goes off every second
        def each_second():
            # Do the clicks per second thing
            self.click_count += self.clicks_per_second
            self.click_label.config(text=f"Clicks: {self.click_count}")

            # Schedule the function to be called again after 1000 milliseconds (1 second)
            self.root.after(1000, each_second)

        # Set up the counter for each second
        self.root.after(1000, each_second)

# Main program entry point
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

    # Create an instance of the ClickerGame class
    clicker_game = ClickerGame(root)

    # Start the Tkinter event loop
    root.mainloop()
