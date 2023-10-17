import pyautogui
from PIL import ImageGrab, ImageOps
import time


# print("Place the mouse at the top-left corner of the game area and press Enter.")
# input()  # Wait for Enter to be pressed
# x1, y1 = pyautogui.position()  # Grab the mouse x, y position

# print("Place the mouse at the bottom-right corner of the game area and press Enter.")
# input()
# x2, y2 = pyautogui.position()

# game_explorasi = (x1, y1, x2, y2)
# print(game_explorasi)

game_area_bottom = (337, 585, 630, 698) #(x1, y1, x2, y2)

def capture_screen(bounding_box):
    return ImageOps.grayscale(ImageGrab.grab(bounding_box))         
 
def is_obstacle(data):
    avg_brightness = sum(data) / len(data)
    threshold = avg_brightness * 0.90  # You'll need to experiment with this
    
    for pixel in data:
        if pixel < threshold:
            return True
    return False

while True:
    image_bottom = capture_screen(game_area_bottom)
    image_data_bottom = list(image_bottom.getdata())

    if is_obstacle(image_data_bottom):
        pyautogui.press('space') # Jump

    time.sleep(0.01)                       