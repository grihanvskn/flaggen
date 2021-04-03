from tkinter import *
import PIL
import requests


tk = Tk()
canvas = Canvas(tk, width = 1280, height = 720)
canvas.pack()
tk.update()
def stripesv(count, colour1, colour2):
    for i in range(count):
        if i % 2:
            canvas.create_rectangle(1280 // count * i, 0, 1280 // count * (i + 1), 720, fill=colour1,
                                             outline="")
        else:
            canvas.create_rectangle(1280 // count * i, 0, 1280 // count * (i + 1), 720, fill=colour2,
                                             outline="")
def stripesh(count, colour1, colour2):
    for i in range(count):
        if i % 2:
            canvas.create_rectangle(0, 720 // count * i, 1280, 720 // count * (i + 1), fill=colour1,
                                             outline="")
        else:
            canvas.create_rectangle(0, 720 // count * i, 1280, 720 // count * (i + 1), fill=colour2,
                                             outline="")

def tricoleurv(colour1, colour2, colour3):
    canvas.create_rectangle(0, 0, 1280 // 3, 720, fill=colour1, outline="")
    canvas.create_rectangle(1280 // 3, 0, 1280 // 1.5, 720, fill=colour2, outline="")
    canvas.create_rectangle(1280 // 1.5, 0, 1280, 720, fill=colour3, outline="")

def tricoleurh(colour1, colour2, colour3):
    canvas.create_rectangle(0, 0, 1280, 720 // 3, fill=colour1, outline="")
    canvas.create_rectangle(0, 720 // 3, 1280, 720 // 1.5, fill=colour2, outline="")
    canvas.create_rectangle(0, 720 // 1.5, 1280, 720, fill=colour3, outline="")

def duocolgrid(colour1, colour2):
    canvas.create_rectangle(0, 0, 1280 // 2, 720 // 2, fill=colour1, outline="")
    canvas.create_rectangle(1280 // 2, 720 // 2, 1280, 720, fill=colour1, outline="")
    canvas.create_rectangle(0, 720 // 2, 1280 // 2, 720, fill=colour2, outline="")
    canvas.create_rectangle(1280 // 2, 0, 1280, 720 // 2, fill=colour2, outline="")

def anarquia(colour1, colour2):
    canvas.create_polygon([0, 720, 0, 0, 1280, 0], fill = colour1, outline="")
    canvas.create_polygon([0, 720, 1280, 0, 1280, 720], fill=colour2, outline="")

def anarquia_reve(colour1, colour2):
    canvas.create_polygon([0, 720, 0, 0, 1280, 720], fill = colour1, outline="")
    canvas.create_polygon([0, 0, 1280, 720, 1280, 0], fill=colour2, outline="")




tk.update()
a = input()