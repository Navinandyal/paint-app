from tkinter import *
from tkinter import Scale
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab
window = Tk()
window.state("zoomed")
window.title("Paint app")
#variables
eraser_c="white"
pen_c="black"

#Canvas
canvas = Canvas(window,bg="white",bd=5,relief=GROOVE, width=1500, height=660)
canvas.place(x=13,y=100)

#Function
def canvas_color():
    global eraser
    c=colorchooser.askcolor()
    canvas.configure(bg=c[1])
    eraser_c=c[1]

def saved():
    file_name = filedialog.asksaveasfilename(defaultextension=".jpg")
    x=window.winfo_rootx + canvas.winfo_x()
    y=window.winfo_rooty + canvas.winfo_y()

    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(file_name)
    messagebox.showinfo("Paint Notification","Image Is Saved As"+str(file_name))

def eraser():
    global pen_c
    pen_c=eraser_c

def clear():
    canvas.delete("all")

def paint(event):
    x1,y1 = (event.x-2),(event.y-2)
    x2,y2 = (event.x+2),(event.y+2)
    canvas.create_oval(x1,y1,x2,y2,fill=pen_c,outline=pen_c,width=pen_size.get())

canvas.bind("<B1-Motion>",paint)

def select_color(col):
    global pen_c
    pen_c = col

#Frame
color_frame=LabelFrame(window,text="Color",relief=RIDGE,bg="white",width=50,font=("arial",15,"bold"))
color_frame.place(x=10,y=10,width=425,height=60)

tool_frame=LabelFrame(window,text="Tool",relief=RIDGE,bg="white",width=50,font=("arial",15,"bold"))
tool_frame.place(x=440,y=10,width=195,height=60)

pen_size=LabelFrame(window,text="Size",relief=RIDGE,bg="white",width=50,font=("arial",15,"bold"))
pen_size.place(x=640,y=10,width=185,height=70)

#Color
colors=["#FF0000","#008000","#FFC0CB","#FFA500","#FFFF00","#008000","#0000FF","#A52A2A","#FFFFFF","#000000","#808080","#87CEEB"]

#Button
i=j=0
for c in colors:
    Button(color_frame,bd=3,bg=c,relief=RIDGE,width=3,command=lambda col= c:select_color(col) ).grid(row=j,column=i,padx=1)
    i=i+1

#Tool_Button
canvas_color_b1 =Button(tool_frame,text="canvas",bd=4,bg="white",command=canvas_color,relief=RIDGE)
canvas_color_b1.grid(row=0,column=0,padx=2)

save_b2 = Button(tool_frame,text="save",bd=4,bg="white",command=saved,relief=RIDGE)
save_b2.grid(row=0,column=1,padx=2)

eraser_b3 = Button(tool_frame,text="eraser",bd=4,bg="white",command=eraser,relief=RIDGE)
eraser_b3.grid(row=0,column=2,padx=2)

clear_b4 = Button(tool_frame,text="clear",bd=4,bg="white",command=clear,relief=RIDGE)
clear_b4.grid(row=0,column=3,padx=2)

#Pen and Eraser Size
pen_size = Scale(pen_size,orient=HORIZONTAL,from_=0,to=50,length=170)
pen_size.set(1)
pen_size.grid(row=0,column=0)

window.mainloop()