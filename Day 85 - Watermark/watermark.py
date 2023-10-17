import tkinter as tk
from tkinter import ttk, filedialog, Canvas, NW, PhotoImage
from PIL import Image, ImageTk

file = file2 = None

def watermark():
    if file and file2:
        logo_image = Image.open(file2).convert("RGBA")
        background_image = Image.open(file).convert("RGBA")

        logo_width, logo_height = logo_image.size
        background_width, background_height = background_image.size

        if logo_width > background_width or logo_height > background_height:
            logo_image.thumbnail((background_width, background_height))

        logo_x = 0
        logo_y = 0
        background_image.paste(logo_image, (logo_x, logo_y), mask=logo_image)
        background_image.show()

def open_file():
    global file
    file = filedialog.askopenfilename(initialdir='panda.jpg')
def open_filelogo():
    global file2
    file2 = filedialog.askopenfilename(initialdir='wwf.jpg')


window = tk.Tk()
window.attributes('-transparentcolor', '#f0f0f0')
window.title("Water Mark App")
window.geometry('800x600')

label = ttk.Label(window, text="Select the image", font=("Arial", 25))
label.pack()

button1 = ttk.Button(window, text="Select Image", command=open_file)
button1.pack()

button2 = ttk.Button(window, text="Select Image Logo", command=open_filelogo)
button2.pack()

button3 = ttk.Button(window, text="Show image with watermark", command=watermark)
button3.pack()

window.mainloop()
