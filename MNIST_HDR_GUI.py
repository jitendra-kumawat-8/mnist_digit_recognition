from tkinter import *
import PIL
from PIL import Image, ImageDraw, ImageOps

def input_data():
    def save():
        root.destroy()
    def activate_paint(e):
        global lastx, lasty
        cv.bind('<B1-Motion>', paint)
        lastx, lasty = e.x, e.y


    def paint(e):
        global lastx, lasty
        x, y = e.x, e.y
        cv.create_line((lastx, lasty, x, y), width=20, smooth=True, capstyle=ROUND, splinesteps=30000)
        #  --- PIL
        draw.line((lastx, lasty, x, y), fill='black', width=20)
        lastx, lasty = x, y


    root = Tk()

    lastx, lasty = None, None



    cv = Canvas(root, width=200, height=200, bg='white')
    # --- PIL
    image1 = PIL.Image.new('L', (200, 200), 'white')
    draw = ImageDraw.Draw(image1)

    cv.bind('<1>', activate_paint)
    cv.pack(expand=YES, fill=BOTH)

    btn_save = Button(text="save", command=save)
    btn_save.pack()

    root.mainloop()
    image=image1.resize((28,28))
    image=ImageOps.invert(image)
    image.show()
    return(image)
input_data()
