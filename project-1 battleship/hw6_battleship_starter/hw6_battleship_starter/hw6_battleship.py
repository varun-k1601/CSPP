"""
15-110 Hw6 - Battleship Project
Name:
AndrewID:
"""

import hw6_battleship_tests as test
from random import randint

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
#5 [Check6-1] & #3 [Check6-2] & #3 [Hw6] & #4 [Hw6]
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"] = 10
    data["cols"] = 10
    data["board_size"] = 500
    data["temporary_ship"] = []
    data["computer"] = emptyGrid(data["rows"], data["cols"])
    data["player"] = emptyGrid(data["rows"], data["cols"])
    data["computer_ships"] = 5
    data["player_ships"] = 0
    data['computer'] = addShips(data["computer"], data["computer_ships"])
    data['winner'] = None
    data['max_turns'] = 50
    data['turns_completed'] = 0
    return data


'''
makeView(data, userCanvas, compCanvas)
#6 [Check6-1] & #2 [Check6-2] & #3 [Hw6]
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data, canvas = userCanvas, grid = data['player'], showShips=True)
    drawGrid(data, canvas = compCanvas, grid = data['computer'], showShips=False)

    drawShip(data, userCanvas, data['temporary_ship'])
    drawGameOver(data, userCanvas)
    drawGameOver(data, compCanvas)
    return


'''
keyPressed(data, events)
#5 [Hw6]
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    if event.keysym == 'Return' and data['winner'] is not None:
        makeModel(data)


'''
mousePressed(data, event, board)
#5 [Check6-2] & #1 [Hw6] & #3 [Hw6]
Parameters: dict mapping strs to values ; mouse event object ; str
Returns: None
'''
def mousePressed(data, event, board):
    if data['winner'] is None:
        cell = getClickedCell(data, event)
        if cell is not None:
            row, col = cell
            if board == "user":
                clickUserBoard(data, row, col)
            elif board == "comp" and data['player_ships'] == 5:
                runGameTurn(data, row, col)

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
#1 [Check6-1]
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid=[]
    for _ in range(rows):
        row=[]
        for _ in range(cols):
            row.append(EMPTY_UNCLICKED)
        grid.append(row)
    return grid


'''
createShip()
#2 [Check6-1]
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row_num=randint(1,8)
    col_num=randint(1,8)
    horizontal=randint(0,1)
    ship=[]
    if horizontal==0:
        ship.append([row_num-1,col_num])
        ship.append([row_num,col_num])
        ship.append([row_num+1,col_num])
    else:
        ship.append([row_num,col_num-1])
        ship.append([row_num,col_num])
        ship.append([row_num,col_num+1])
    return ship


'''
checkShip(grid, ship)
#3 [Check6-1]
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    if len(ship)!=3:
        return False
    for row,col in ship:
        if grid[row][col]!=EMPTY_UNCLICKED:
            return False
    return True


'''
addShips(grid, numShips)
#4 [Check6-1]
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count=0
    while(count<numShips):
        ship=createShip()
        if checkShip(grid,ship):
            for row,col in ship:
                grid[row][col]=SHIP_UNCLICKED
            count+=1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
#6 [Check6-1] & #1 [Hw6]
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    rows = data['rows']
    cols = data['cols']
    width = data['board_size'] // cols
    height = data['board_size'] // rows
    for row in range(rows):
        for col in range(cols):
            x_start = col * width
            x_end = (col + 1) * width
            y_start = row * height
            y_end = (row + 1) * height

            if grid[row][col] == SHIP_UNCLICKED and showShips:
                fill_color = "yellow"
            elif grid[row][col] == EMPTY_CLICKED:
                fill_color = "white"
            elif grid[row][col] == SHIP_CLICKED:
                fill_color = "red"
            else:
                fill_color = "blue"

            canvas.create_rectangle(x_start, y_start, x_end, y_end, fill=fill_color, outline='black')


### WEEK 2 ###

'''
isVertical(ship)
#1 [Check6-2]
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    sorted_ship = sorted(ship)
    current_row = sorted_ship[0][0]
    current_col = sorted_ship[0][1]
    for i in range(3):
        if current_row != sorted_ship[i][0] or current_col != sorted_ship[i][1]:
            return False
        current_row += 1
    return True


'''
isHorizontal(ship)
#1 [Check6-2]
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    sorted_ship = sorted(ship)
    current_row = sorted_ship[0][0]
    current_col = sorted_ship[0][1]
    for i in range(3):
        if current_row != sorted_ship[i][0] or current_col != sorted_ship[i][1]:
            return False
        current_col += 1
    return True


'''
getClickedCell(data, event)
#2 [Check6-2]
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    rows = data['rows']
    cols = data['cols']
    width = data['board_size'] // cols
    height = data['board_size'] // rows
    X_click, Y_click = event.x, event.y

    if 0 <= X_click//width < data['cols'] and 0 <= Y_click//height < data['rows']:
        return [Y_click//height, X_click//width]
    else:
        return None


'''
drawShip(data, canvas, ship)
#3 [Check6-2]
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    cols = data['cols']
    rows = data['rows']
    width = data['board_size'] // cols
    height = data['board_size'] // rows
    for row, col in ship:
        x_start = col * width
        x_end = (col + 1) * width
        y_start = row * height
        y_end = (row + 1) * height

        canvas.create_rectangle(x_start, y_start, x_end, y_end, fill="white", outline='black')


'''
shipIsValid(grid, ship)
#4 [Check6-2]
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    return checkShip(grid, ship) and (isVertical(ship) or isHorizontal(ship))


'''
placeShip(data)
#4 [Check6-2]
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if data['player_ships'] >= 5:
        print('You have placed all your ships!! Now start playing')
        return None
    player_board = data['player']
    temp_ship = data['temporary_ship']

    if shipIsValid(player_board, temp_ship):
        for row,col in temp_ship:
            player_board[row][col] = SHIP_UNCLICKED
        data['player_ships'] += 1
    else:
        print('Invalid ship. Please click the cells consecutively and try again.')

    data['temporary_ship'] = []


'''
clickUserBoard(data, row, col)
#4 [Check6-2]
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["player_ships"] >= 5:
        print("You have placed all your ships!! Now start playing")
        return None
    temp_ship = data['temporary_ship']

    if [row, col] not in temp_ship:
        temp_ship.append([row, col])
    else:
        temp_ship.remove([row, col])
    
    if shipIsValid(data['player'], temp_ship):
        placeShip(data)


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
#1 [Hw6] & #3 [Hw6]
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board[row][col] == EMPTY_UNCLICKED:
        board[row][col] = EMPTY_CLICKED
    elif board[row][col] == SHIP_UNCLICKED:
        board[row][col] = SHIP_CLICKED


'''
runGameTurn(data, row, col)
#1 [Hw6] & #2 [Hw6] & #4 [Hw6]
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    computer = data['computer']
    player = data['player']
    if computer[row][col] == EMPTY_CLICKED or computer[row][col] == SHIP_CLICKED:
        return None
    else:
        updateBoard(data, computer, row, col, "user")
    
    if isGameOver(computer):
        data['winner'] = "player"
    row, col = getComputerGuess(player)
    updateBoard(data, player, row, col, "comp")
    if isGameOver(player):
        data['winner'] = "computer"
    data['turns_completed'] += 1
    if data['turns_completed'] == data['max_turns']:
        data['winner'] = "draw"


'''
getComputerGuess(board)
#2 [Hw6]
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    while(True):
        row_num = randint(0, 9)
        col_num = randint(0, 9)
        if board[row_num][col_num] == SHIP_UNCLICKED or board[row_num][col_num] == EMPTY_UNCLICKED:
            return [row_num, col_num]


'''
isGameOver(board)
#3 [Hw6]
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == SHIP_UNCLICKED:
                return False
    return True


'''
drawGameOver(data, canvas)
#3 [Hw6] & #4 [Hw6] & #5 [Hw6]
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if data['winner'] is not None:
        message = ""
        if data['winner'] == "player":
            message = "You won!! Congrats"
        elif data['winner'] == "computer":
            message = "Over!! You lost"
        elif data['winner'] == 'draw':
            message = "Draw"
        
        x = data["board_size"] // 2
        y = data["board_size"] // 2

        canvas.create_rectangle(0, 200, 500, 300, fill="white", outline="black")
        canvas.create_text(x, y, text=message + '\nPress Enter to play again', font=("Arial", 30), fill="black")



### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    test.week1Tests()

    ## Uncomment these for Week 2 ##
 
    print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()


    ## Uncomment these for Week 3 ##

    print("\n" + "#"*15 + " WEEK 3 TESTS " +  "#" * 16 + "\n")
    test.week3Tests()


    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
