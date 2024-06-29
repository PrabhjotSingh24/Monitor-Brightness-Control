from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw
import screen_brightness_control as sbc
from math import floor
def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image
state = sbc.set_brightness(floor(sbc.get_brightness()[0]), no_return=False)[0]

def set_state(v):
    def inner(icon, item):
        global state
        state = v
        if v<101: 
           sbc.fade_brightness(v,logarithmic=True,interval=0.0001,increment=5) 
        else:
            icon.stop()
    return inner

def get_state(v):
    def inner(item):
        return state == v
    return inner

# Let the menu items be a callable returning a sequence of menu
# items to allow the menu to grow
icon('test', create_image(64,64,'black','white'), menu=menu(lambda: (
    item(
        'Brightness %d' % i,
        set_state(i),
        checked=get_state(i),
        radio=True)
    for i in range(0,106,5)))).run()