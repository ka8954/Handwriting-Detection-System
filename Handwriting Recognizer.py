import easyocr

reader = easyocr.Reader(["en", 'en'], gpu=False)
import PIL
from PIL import ImageDraw

im = PIL.Image.open(r"D:\Downloads\Files\nr.jpg")
im

bounds = reader.readtext(r'D:\Downloads\Files\nr.jpg')
bounds

def draw_boxes(image, bounds, color='yellow',width=8):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0,p1,p2,p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3], fill=color, width=width)
    return image

draw_boxes(im,bounds)

im.save(r"D:\Downloads\Files\nr.jpg")

len(bounds)

for i in bounds:
    print(i[1])

f=open(r"D:\Downloads\Files\nr.jpg", mode='a', encoding="utf-8")

for i in bounds:
    print(i[1])
    f.write(i[1])
