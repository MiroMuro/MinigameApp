from tkinter import *
from PIL import ImageTk, Image
import random
root = Tk()
root.title("Main Screen")
root.iconbitmap("e:/taustakuva_d2n_icon.ico")
root.geometry("400x400")

def create_minesweeper_grid(event=None):
    cell_width = canvas.winfo_width() / 10
    cell_height = canvas.winfo_height()/ 10
    print(canvas.winfo_width(),canvas.winfo_height())
    print(cell_width,cell_height)
    for i in range(31):
        x = i * cell_width
        canvas.create_line(x,0,x,canvas.winfo_height())
        y = i * cell_height
        canvas.create_line(0,y,canvas.winfo_width(),y)
    create_minesweeper_bombs(canvas)

def create_minesweeper_bombs(canvas):
    cellamount = 10
    coordinates=[]
    r_ids = []
    for i in range(cellamount):
        x = random.randrange(0,600,60)
        y = random.randrange(0,600,60)
        coord = (x,y)
        coordinates.append(coord)
    for coord in coordinates:
        x = coord[0]
        y = coord[1]
        rectangle_id = canvas.create_rectangle(x,y,x+60,y+60,fill="red")
        r_ids.append(rectangle_id)
    for xd in r_ids:
        print(canvas.coords(xd))
        print(canvas.itemcget(xd,"fill"))
    return
def check_nearby_bombs():
    
    return

def create_bomb_locations(cellamount):
    #Cell amount = 100

    return
def open():
    top =Toplevel()
    top.title("Minesweeper")
    top.geometry("700x700")
    global canvas
    topLabel = Label(top, text="Minesweeper")
    topLabel.grid(row=0,column=0,columnspan=3)
    #The borders add 3 pixels to all sides somehow. So the canvas is 594x594
    canvas = Canvas(top, width=594, height=594,borderwidth=1,relief="solid")
    canvas.grid(row=1,column=1)
    #Bind the canvas to the create_minesweeper_grid function
    canvas.bind("<Configure>", create_minesweeper_grid)
    #canvas.bind("<Configure>", create_minesweeper_bombs)



btn = Button(root, text="Open minesweeper",command=open)
btn.grid(row=0,column=0)
btn2 = Button(root, text="Coords",command=create_minesweeper_bombs)
btn2.grid(row=0,column=1)
root.mainloop()