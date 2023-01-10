from tkinter import ttk
from Classes import *

# Initialize the Tkinter Library
root = Tk()

# Function called when the Set Start Pos is pressed
def set_start():
    root.bind('<Button 1>', b.set_start_pos)
    root.bind('<B1-Motion>', nothing)


# Function called when the Set Goal Pos is pressed
def goal_point():
    root.bind('<Button 1>', b.set_goal_pos)
    root.bind('<B1-Motion>', nothing)


def add_walls():
    root.bind('<Button 1>', b.add_walls)
    root.bind('<B1-Motion>', b.add_walls)


# Function called when the Find Path button is pressed
def pathfind():
    if search_type.get() == "Breadth First Search":
        b.BFS()
    if search_type.get() == "Down First Search":
        b.DFS()
    if search_type.get() == "A Star":
        b.a_star()


# Python is weird and won't let me unbind the motion LOL
def nothing(event):
    return None

# Create and format Header Frame
header = ttk.Frame(root)
header.pack(pady=10)
header.config(width=600, height=100)

# Create and format Body Frame
body = ttk.Frame(root)
body.pack()
body.config()

# Create and insert Canvas into Body
canvas = Canvas(body, width=600, height=600, bg='black')
canvas.pack()

# Build the Board Object From Class
b = Board(25, canvas, 600)

# Create and place Footer Frame
footer = ttk.Frame(root)
footer.pack(side='bottom')
footer.config()

# Create and place right footer panel
foot_right = ttk.Frame(footer)
foot_right.pack(side='right')

# Create and place left footer panel
foot_left = ttk.Frame(footer)
foot_left.pack(side='left')

# Create and place middle footer panel
foot_mid = ttk.Frame(footer)
foot_mid.pack(padx=10)

# Create and place top middle footer panel
foot_mid_1 = ttk.Frame(foot_mid)
foot_mid_1.pack(side='top')

# Create and place bottom middle footer panel
foot_mid_2 = ttk.Frame(foot_mid)
foot_mid_2.pack(side='bottom')

# Create and place Path Button
path_butt = ttk.Button(header, text="Find Path", command=pathfind)
path_butt.pack(side="left", padx=5)

# Create and place the Change Start Pos Button
start_butt = ttk.Button(foot_left, text="Set Start Point", command=set_start)
start_butt.pack(side='top', padx=5)

# Create and place the Change Goal Pos Button
goal_butt = ttk.Button(foot_left, text="Set Goal Point", command=goal_point)
goal_butt.pack(side="bottom", padx=5)

# Create and place the Search Type Menu
search_type = StringVar()
menu = ttk.OptionMenu(header, search_type, "Search Type", "Down First Search", "Breadth First Search", "A Star")
menu.pack(side='left')

# Create and place the Reset Button
reset_butt = ttk.Button(header, text="RESET", command=b.reset_board)
reset_butt.pack(side='left')

# Create and place the Add Walls Button
wall_butt = ttk.Button(foot_right, text="Add Walls", command=add_walls)
wall_butt.pack(side='top')

# Create and place the Clear Walls Button
clear_wall_butt = ttk.Button(foot_right, text="Clear Walls", command=b.clear_walls)
clear_wall_butt.pack(side='bottom')

# Tkinter Loop (All Code Stays Above)
mainloop()
