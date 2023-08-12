from dotenv import load_dotenv
load_dotenv()
import easyocr
from supabase import create_client, Client
import os
reader = easyocr.Reader(["en", 'en'], gpu=False)
import PIL
from PIL import ImageDraw
x = input("Enter the Path of the file : ")
im = PIL.Image.open(x)
im

bounds = reader.readtext(x)
bounds

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url,key)

def draw_boxes(image, bounds, color='yellow',width=8):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0,p1,p2,p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3], fill=color, width=width)
    return image

draw_boxes(im,bounds)

im.save(x)

len(bounds)
li = []

for i in bounds:
    li.append(i[1])
    print(i[1])

f=open(x)

d1 = supabase.table("Detect").insert({"Scanned Data":li}).execute()
assert len(d1.data) > 0

