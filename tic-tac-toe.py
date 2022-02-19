import tkinter,time
import numpy as np
list = []
helper = []
root = tkinter.Tk()
root.title('Tic-tac-toe | by Smisch')
c = tkinter.Canvas(width=600,height=650,bg="aqua")
c.pack()

def boot():
    list.clear()
    helper.clear()
    list.append(["f",".","."])
    list.append([".",".","f"])
    list.append([".","f","."])
    c.delete("all")
    c.create_line(200,0,200,600,width=2)
    c.create_line(400,0,400,600,width=2)
    c.create_line(0,200,600,200,width=2)
    c.create_line(0,400,600,400,width=2)
    c.create_line(0,600,600,600,width=2)
    c.create_text(300,625,text="© 2022 Smisch",font="Roboto 10 bold")
    c.update()
def check(x,y,z):
    if 200 > x >= 0 and 0 <= y < 200 :
        if list[0][0] in ["x","o"]:
            pass
            return -1,-2,-1,-2
        else: 
            if z=="left":   list[0].insert(1,"x"); list[0].pop(0)
            elif z =="right": list[0].insert(1,"o"); list[0].pop(0)
            return 4,4,196,196
    elif 400 > x >= 0 and 0 <= y < 200 :
        if list[0][1] in ["x","o"]:
            pass
            return -1,-2,-1,-2
        else: 
            if z=="left":   list[0].insert(2,"x"); list[0].pop(1)
            elif z =="right": list[0].insert(2,"o"); list[0].pop(1)
            return 204,4,396,196
    elif 600 > x >= 0 and 0 <= y < 200 :
        if list[0][2] in ["x","o"]:
            pass
            return -1,-2,-1,-2
        else: 
            if z=="left":   list[0].insert(3,"x"); list[0].pop(2)
            elif z =="right": list[0].insert(3,"o"); list[0].pop(2)
            return 404,4,596,196

    elif 200 > x >= 0 and 200 <= y < 400 :
        if list[1][0] in ["x","o"]:
            pass
            return -1,-2,-1,-2
        else: 
            if z=="left":   list[1].insert(1,"x"); list[1].pop(0)
            elif z =="right": list[1].insert(1,"o"); list[1].pop(0)
            return 4,204,196,396
    elif 400 > x >= 0 and 200 <= y < 400 :
        if list[1][1] in ["x","o"]:
            pass
            return -1,-2,-1,-2
        else: 
            if z=="left":   list[1].insert(2,"x"); list[1].pop(1)
            elif z =="right": list[1].insert(2,"o"); list[1].pop(1)
            return 204,204,396,396
    elif 600 > x >= 0 and 200 <= y < 400 :
        if list[1][2] in ["x","o"]:
            pass
            return -1,-2,-1,-2
        else: 
            if z=="left":   list[1].insert(3,"x"); list[1].pop(2)
            elif z =="right": list[1].insert(3,"o"); list[1].pop(2)
            return 404,204,596,396


    elif 200 > x >= 0 and 400 <= y < 600 :
        if list[2][0] in ["x","o"]:
            pass
            return -1,-2,-1,-2
        else: 
            if z=="left":   list[2].insert(1,"x"); list[2].pop(0)
            elif z =="right": list[2].insert(1,"o"); list[2].pop(0)
            return 4,404,196,596
    elif 400 > x >= 0 and 400 <= y < 600 :
        if list[2][1] in ["x","o"]:
            pass
            return -1,-2,-1,-2
        else: 
            if z=="left":   list[2].insert(2,"x"); list[2].pop(1)
            elif z =="right": list[2].insert(2,"o"); list[2].pop(1)
            return 204,404,396,596
    elif 600 > x >= 0 and 400 <= y < 600 :
        if list[2][2] in ["x","o"]:
            pass
            return -1,-2,-1,-2
        else: 
            if z=="left":   list[2].insert(3,"x"); list[2].pop(2)
            elif z =="right": list[2].insert(3,"o"); list[2].pop(2)
            return 404,404,596,596

def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

def checkWin(board):
    #transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)

def checker():
    if checkWin(list) == "x":
        x_won()
    elif checkWin(list) == "o":
        o_won()
    if list[0].count(".") == 0 and list[1].count(".") == 0 and list[2].count(".") == 0:     
        if list[0].count("f") == 0 and list[1].count("f") == 0 and list[2].count("f") == 0: draw()
def x_won():
    c.delete("all")
    c.create_text(300,300,text="X  Won",font="Roboto 70 bold")
    c.create_text(300,625,text="© 2022 Smisch",font="Roboto 10 bold")
    c.update()
    time.sleep(5)
    boot()
def o_won():
    c.delete("all")
    c.create_text(300,300,text="O  Won",font="Roboto 70 bold")
    c.create_text(300,625,text="© 2022 Smisch",font="Roboto 10 bold")
    c.update()
    time.sleep(5)
    boot()
def draw():
    c.delete("all")
    c.create_text(300,300,text="DRAW",font="Roboto 70 bold")
    c.create_text(300,625,text="© 2022 Smisch",font="Roboto 10 bold")
    c.update()
    time.sleep(5)
    boot()
    
def x_type(event):
    if helper in [[],["o"]]:
        if len(helper) == 1:
            helper.clear()
        helper.append("x")     
        coords = check(event.x,event.y,"left")
        c.create_text(coords[0]+96,coords[1]+96,text="X",font="Roboto 192 bold",fill="RED")
        #c.create_rectangle(check(event.x,event.y,"left",),width=5)
        checker()
    

def o_type(event):
    if helper in [[],["x"]]:
        if len(helper) == 1:
            helper.clear()
        helper.append("o")
        coords = check(event.x,event.y,"right")
        c.create_text(coords[0]+96,coords[1]+96,text="O",font="Roboto 192 bold",fill="BLUE")
        #c.create_oval(check(event.x,event.y,"right"),width=5)
        checker()

boot()

c.bind('<Button-1>', x_type)
c.bind('<Button-3>', o_type)
c.mainloop()
