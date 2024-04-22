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
    for i in range(10):
        x = i * cell_width
        canvas.create_line(x,0,x,canvas.winfo_height())
        y = i * cell_height
        canvas.create_line(0,y,canvas.winfo_width(),y)
    create_minesweeper_bombs(canvas)

def create_minesweeper_bombs(canvas):
    cellamount = 10
    coordinates=[]
    r_ids = []
    #Create 10 random coordinates
    for i in range(cellamount):
        x = random.randrange(0,600,60)
        y = random.randrange(0,600,60)
        coord = (x,y)
        coordinates.append(coord)
    #Draw the bomb rectangles
    for coord in coordinates:
        x = coord[0]
        y = coord[1]
        rectangle_id = canvas.create_rectangle(x,y,x+60,y+60,fill="red")
        r_ids.append(rectangle_id)
    #List bomb rectangle coordinates and colors
    bomb_coords = []
    for xd in r_ids:
        bomb_coords.append(canvas.coords(xd))
        #print(canvas.coords(xd))
        #print(canvas.itemcget(xd,"fill"))
    create_minesweeper_numbers(bomb_coords)
    return
def create_minesweeper_numbers(bomb_coordinates):
    cell_width = canvas.winfo_width() / 10
    cell_height = canvas.winfo_height()/ 10
   # print(bomb_coordinates)
    for x in range(10):
        for y in range(10):
            number_coord = [x*cell_width,y*cell_height,x*cell_width+cell_width,y*cell_height+cell_height]
            for bomb in bomb_coordinates:
                if bomb == number_coord:
                    canvas.create_text(x*cell_width+30,y*cell_height+30,text="B",font=("Helvetica", 16))
                    break
            else:
                r_id = canvas.create_rectangle(x*cell_width,y*cell_height,x*cell_width+cell_width,y*cell_height+cell_height,fill="green")
                bomb_amount = check_nearby_bombs(canvas.coords(r_id),bomb_coordinates)
                canvas.create_text(x*cell_width+30,y*cell_height+30,text=f"{bomb_amount}",font=("Helvetica", 16))
            
def check_nearby_bombs(coords, bomb_coords):
    
    x,y,x2,y2 = coords
    bomb_amount = 0
    if x == 0 and y == 0:
        print("TOP LEFT")
        nearby_tiles = [
            #next to right
            [x+60,y,x2+60,y2],
            #below
            [x,y+60,x2,y2+60],
            #right bottom
            [x+60,y+60,x2+60,y2+60]
            ]
        print("Nearby tiles: ",nearby_tiles)
        print("Bomb coords: ",bomb_coords)
        for bomb in bomb_coords:
            if bomb in nearby_tiles:
                bomb_amount += 1
                print("BOMB Here t-left")

    elif x == 0 and y == 540:
        print("BOTTOM LEFT")
        nearby_tiles = [
            #above
            [x,y-60,x2,y2-60],
            #right,
            [x+60,y,x2+60,y2],
            #top right
            [x+60,y-60,x2+60,y2-60]
        ]        
        for bomb in bomb_coords:
            if bomb in nearby_tiles:
                bomb_amount += 1
                print("BOMB Here b-left")

    elif x == 540 and y == 0:
        print("TOP RIGHT")
        nearby_tiles = [
            #left
            [x-60,y,x2-60,y2],
            #below
            [x,y+60,x2,y2+60],
            #bottom left
            [x+60,y-60,x2+60,y2-60],
        ]
        for bomb in bomb_coords:
            if bomb in nearby_tiles:
                bomb_amount += 1
                print("BOMB Here t-right")
                
    elif x == 540 and y == 540:
        print("BOTTOM RIGHT")
        nearby_tiles = [
            #left
            [x-60,y,x2-60,y2],
            #aobe
            [x,y-60,x2,y2-60],
            #top left
            [x-60,y-60,x2-60,y2-60],
        ]
        for bomb in bomb_coords:
            if bomb in nearby_tiles:
                bomb_amount += 1
                print("BOMB Here b-right")
    return bomb_amount

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