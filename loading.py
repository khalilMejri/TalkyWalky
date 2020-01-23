from PIL import Image, ImageTk
import tkinter as tk
import time

IMAGE_PATH = './imgs/11.png'
WIDTH, HEIGTH = 700, 500

screen = tk.Tk()
screen.geometry('{}x{}'.format(WIDTH, HEIGTH))

canvas = tk.Canvas(screen, width=WIDTH, height=HEIGTH)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize(
    (WIDTH, HEIGTH), Image.ANTIALIAS))
# Keep a reference in case this code is put in a function.
canvas.background = img
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Put a tkinter widget on the canvas.
# button = tk.Button(screen, text="Start")
# button_window = canvas.create_window(10, 10, anchor=tk.NW, window=button)

screen.after(2500, screen.destroy)
screen.mainloop()
if True:
    import login
