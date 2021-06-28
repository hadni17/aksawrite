from pathlib import WindowsPath
from tkinter import * 
from tkinter import Widget, font
from tkinter.constants import N, W
from typing import Text
import tkinter.font as font
import AI
import numpy as np
import time
from PIL import Image, ImageTk, ImageDraw

model = AI.load_ai()


window = Tk()
window.title("Aksawrite")
myFont = font.Font(family='Roboto',size=12)

load = Image.open("logo.png")
load = load.resize((305, 141), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(load)
header = Label(window,image=photo,borderwidth=0)
header.pack(side='top')
header.place(x=680,y = 60)

img = Image.new(mode="1", size=(450, 450), color=255)
tkimage = ImageTk.PhotoImage(img)
canvas = Label(window, image=tkimage,borderwidth=0)
canvas.pack()
canvas.place(x=50,y=60)
draw = ImageDraw.Draw(img)
last_point = (0, 0)

# prediction = StringVar()
# label = Label(window, textvariable=prediction)

def draw_image(event):
    global last_point, tkimage,prediction
    window.bind("<B1-Motion>", draw_image)
    current_point = (event.x, event.y)
    draw.line([last_point, current_point], fill="black", width=20)
    last_point = current_point
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()
    canvas.place(x=50,y=60)
    # img_temp = img.resize((28, 28))
    # img_temp = np.array(img_temp)
    # img_temp = img_temp.flatten()
    # output = model.predict([img_temp])
    # if(output[0] == 0):
    #     prediction.set("ha")
    #     print (output)
    # elif(output[0] == 1):
    #     prediction.set("na")
    #     print (output)
    # elif(output[0] == 2):
    #     prediction.set("ca") 
    #     print (output)  
    # elif(output[0]==3):
    #     prediction.set("ra")
    #     print (output)
    # elif(output[0] == 4):
    #     prediction.set("ba")
    #     print (output) 
    # elif(output[0] == 5):
    #     prediction.set("ka") 
    #     print (output)
    # elif(output[0] == 6):
    #     prediction.set("ga")
    #     print (output) 
    
    # label.pack()
    # label.place(x=50,y=60)

def start_draw(event):
    global last_point
    last_point = (event.x, event.y)

def reset_canvas():
    global tkimage, img, draw
    img = Image.new(mode="1", size=(450, 450), color=255)
    draw = ImageDraw.Draw(img)
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()
    canvas.place(x=50,y=60)

btn=Button(window,text="clear",width=15,bg="#FFA800", fg="white",borderwidth=0, command=reset_canvas)
btn.place(x=50,y=520)
btn['font'] = myFont

btn=Button(window,text="Submit",width=15,bg="#FFA800",borderwidth=0, fg="white")
btn.place(x=356,y=520)
btn['font'] = myFont



#create dataset

ha = 0
na = 0
ca = 0
ra = 0
ba = 0
ka = 0
ga = 0
###########
da = 5
dha = 0
ja = 0
la = 0
ma = 0
nga = 0
nya = 0
pa = 0
sa = 0
ta = 0
tha = 0
wa = 0
ya = 0

def save_image(event):
    global ha,na,ca,ra,ba,ka,ga, da,dha,ja,la,ma,nga,nya,pa,sa,ta,tha,wa,ya
    img_temp = img.resize((28, 28))
    if(event.char == "h"):
        img_temp.save(f"ha/{ha}.png")
        ha += 1
    elif(event.char == "n"):
        img_temp.save(f"na/{na}.png")
        na += 1
    elif(event.char == "c"):
        img_temp.save(f"ca/{ca}.png")
        ca += 1
    elif(event.char == "r"):
        img_temp.save(f"ra/{ra}.png")
        ra += 1
    elif(event.char == "b"):
        img_temp.save(f"ba/{ba}.png")
        ba += 1
    elif(event.char == "k"):
        img_temp.save(f"ka/{ka}.png")
        ka += 1
    elif(event.char == "g"):
        img_temp.save(f"ga/{ga}.png")
        ga += 1
    elif(event.char == "d"):
        img_temp.save(f"da/{da}.png")
        da += 1
    elif(event.char == "x"):
        img_temp.save(f"dha/{dha}.png")
        dha += 1
    elif(event.char == "j"):
        img_temp.save(f"ja/{ja}.png")
        ja += 1
    elif(event.char == "l"):
        img_temp.save(f"la/{la}.png")
        la += 1
    elif(event.char == "m"):
        img_temp.save(f"ma/{ma}.png")
        ma += 1
    elif(event.char == "z"):
        img_temp.save(f"nga/{nga}.png")
        nga += 1


window.bind("<B1-Motion>", draw_image)
window.bind("<ButtonPress-1>", start_draw)
window.bind("<Key>", save_image)


# label.pack()
# label.place(x=50,y=60)


window.geometry("1200x600")
window.configure(bg='#F8F7F7')
window.mainloop()