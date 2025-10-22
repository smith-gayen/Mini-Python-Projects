import itertools
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of image paths
image_paths = [
    r"C:\Users\Lenovo Gen\OneDrive\Pictures\Saved Pictures\my old memories\IMG-20240914-WA0030.jpg",
    r"C:\Users\Lenovo Gen\OneDrive\Pictures\Saved Pictures\my old memories\IMG-20240914-WA0035.jpg",
    r"C:\Users\Lenovo Gen\OneDrive\Pictures\Saved Pictures\my old memories\IMG-20240914-WA0018.jpg",
    r"C:\Users\Lenovo Gen\OneDrive\Pictures\Saved Pictures\my old memories\IMG-20240914-WA0026.jpg",
    r"C:\Users\Lenovo Gen\OneDrive\Pictures\Saved Pictures\my old memories\IMG-20240914-WA0055.jpg",
    r"C:\Users\Lenovo Gen\OneDrive\Pictures\Saved Pictures\my old memories\IMG-20240914-WA0025.jpg",
    r"C:\Users\Lenovo Gen\OneDrive\Pictures\Saved Pictures\my old memories\IMG-20240914-WA0031.jpg"
]

# Resize the images to 1080x1080
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

# Iterator for the images
slideshow = itertools.cycle(photo_images)

def update_image():
    photo_image = next(slideshow)  # Get the next image from the cycle
    label.config(image=photo_image)
    root.after(2000, update_image)  # Call update_image again after 3 seconds

def start_slideshow():
    update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()
