import tkinter as tk
import random

def roll_dice():
    for _ in range(10):  # Roll 10 times quickly
        dice_number.set(str(random.randint(1, 6)))
        root.update()
        root.after(100)  # Wait 0.1 seconds
    # Final number
    dice_number.set(str(random.randint(1, 6)))

root = tk.Tk()
root.title("Rolling Dice")

dice_number = tk.StringVar(value="🎲")

tk.Label(root, textvariable=dice_number, font=("Arial", 50)).pack(pady=20)
tk.Button(root, text="Roll Dice", command=roll_dice, font=("Arial", 16)).pack()

root.mainloop()
