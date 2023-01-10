from tkinter import *
import time

# Determines if square is on board and legal to move to
def legal(poss, pred, sq, walls):
    x = poss[1]
    y = poss[0]
    if x > sq - 1 or x < 0 or y > sq - 1 or y < 0:
        return False
    elif f"{y} {x}" in pred.keys():
        return False
    elif poss in walls:
        return False
    else:
        return True


class Board:
    def __init__(self, sq, canvas, c_d):
        self.sq = sq  # Number of Squares for board dimensions
        self.grid = []  # Holds the Rectangle Widgets from board
        self.canvas = canvas  # Canvas where the grid of widgets will be placed
        self.c_d = c_d  # Dimension of the Canvas
        self.pred = {}  # Holds predecessors of nodes to form Path
        self.start = [0, 0]  # initialize the position of the start node
        self.goal = [self.sq-1, self.sq-1]  # initialize the position of the end node
        self.pos = self.start  # initialize position at the starting point
        self.path = []  # list to save the path of function
        self.stack = []  # where the nodes are inserted into during search algorithm
        self.walls = []  # ALl the walls where the path cannot go
        self.build()  # builds grid of squares and places it onto the canvas

    def build(self):
        sq_b = self.c_d / self.sq
        for i in range(self.sq):
            row = []
            for j in range(self.sq):
                row.append(
                    self.canvas.create_rectangle(i * sq_b, j * sq_b, (i + 1) * sq_b, (j + 1) * sq_b, fill='white',
                                                 tag=f"{j} {i}"))
            self.grid.append(row)
        self.canvas.itemconfig(self.grid[self.goal[1]][self.goal[0]], fill='red')
        self.canvas.itemconfig(self.grid[self.start[1]][self.start[0]], fill='green')

    def get_path(self):

        key = f"{self.pos[0]} {self.pos[1]}"
        square = self.pred[key]
        if square == self.start:
            self.canvas.itemconfig(self.grid[self.goal[1]][self.goal[0]], fill='red')
            for i in self.path:
                self.canvas.itemconfig(self.grid[i[1]][i[0]], fill='green')
                self.canvas.update()
                time.sleep(0.01)
            self.canvas.itemconfig(self.grid[self.start[1]][self.start[0]], fill='green')
        else:
            self.path.append(square)
            self.pos = square
            self.get_path()

    def DFS(self):
        while self.pos != self.goal:
            for i in ["up", "right", "down", "left"]:
                x = self.pos[1]
                y = self.pos[0]
                if i == "up":
                    y -= 1
                elif i == "right":
                    x += 1
                elif i == "down":
                    y += 1
                elif i == "left":
                    x -= 1
                elif i == "top right":
                    x += 1
                    y -= 1
                elif i == "bottom right":
                    y += 1
                    x += 1
                elif i == "bottom left":
                    y += 1
                    x -= 1
                elif i == "top right":
                    y -= 1
                    x += 1
                if legal([y, x], self.pred, self.sq, self.walls):
                    self.pred[f"{y} {x}"] = self.pos
                    self.stack.append([y, x])
                    self.canvas.itemconfig(self.grid[x][y], fill='blue')
                    self.canvas.update()

            a = self.stack.pop()
            self.pos = a
            time.sleep(0.01)
        else:
            self.get_path()

    def BFS(self):
        while self.pos != self.goal:
            for i in ["up", "right", "down", "left"]:
                x = self.pos[1]
                y = self.pos[0]
                if i == "up":
                    y -= 1
                elif i == "right":
                    x += 1
                elif i == "down":
                    y += 1
                elif i == "left":
                    x -= 1
                elif i == "top right":
                    x += 1
                    y -= 1
                elif i == "bottom right":
                    y += 1
                    x += 1
                elif i == "bottom left":
                    y += 1
                    x -= 1
                elif i == "top right":
                    y -= 1
                    x += 1
                if legal([y, x], self.pred, self.sq, self.walls):
                    self.pred[f"{y} {x}"] = self.pos
                    self.stack.append([y, x])
                    self.canvas.itemconfig(self.grid[x][y], fill='blue')
                    self.canvas.update()

            a = self.stack.pop(0)
            self.pos = a
            time.sleep(0.01)
        else:
            self.get_path()

    def a_star(self):
        # Returns the shortest distance from current node to goal node
        def find_h(coord):
            # Current node's coordinates
            x_coord = coord[1]
            y_coord = coord[0]

            # Goal node's coordinates
            goal_x = self.goal[1]
            goal_y = self.goal[0]

            # return the Manhattan distance between the two nodes
            return abs(y_coord - goal_y) + abs(goal_x - x_coord)

        # Returns the number of moves it took to get to node
        def find_g(coord):
            if coord == self.start:
                return 1
            else:
                return 1 + find_g(self.pred[f"{coord[0]} {coord[1]}"])

        # Returns F-Value used for priority sorting
        def find_f(coord):
            return find_g(coord) + find_h(coord)

        # Determines if node is legal to add to queue
        def legal(poss):
            x = poss[1]
            y = poss[0]
            if x > self.sq - 1 or x < 0 or y > self.sq - 1 or y < 0:
                return False
            elif f"{y} {x}" in self.pred.keys():
                return False
            elif poss in self.walls:
                return False
            else:
                return True

        ##### FIND NODE TO ADD

        def add_nodes():
            for i in ["up", "top right", "right", "bottom right", "down", "bottom left", "left", "top left"]:
                x = self.pos[1]
                y = self.pos[0]
                if i == "up":
                    y -= 1
                elif i == "right":
                    x += 1
                elif i == "down":
                    y += 1
                elif i == "left":
                    x -= 1
                elif i == "top right":
                    x += 1
                    y -= 1
                elif i == "bottom right":
                    y += 1
                    x += 1
                elif i == "bottom left":
                    y += 1
                    x -= 1
                elif i == "top right":
                    y -= 1
                    x += 1
                if legal([y, x]):
                    self.pred[f"{y} {x}"] = self.pos
                    self.stack.append([[y, x], find_f([y, x])])

        # Returns index of element from list with smallest F-Value
        def find_min_f(L):
            f_values = [i[1] for i in L]
            small = min(f_values)
            return f_values.index(small)

        # Pops smallest F and sets that to current pos
        def pop_min():
            new_node = self.stack.pop(find_min_f(self.stack))
            node = new_node[0]
            self.pos = node
            self.canvas.itemconfig(self.grid[self.pos[1]][self.pos[0]], fill='blue')
            self.canvas.update()

        # Calls the algorithm until the goal is found
        while self.pos != self.goal:
            add_nodes()
            pop_min()
            time.sleep(0.01)
        else:
            self.get_path()

    def set_goal_pos(self, event):
        try:
            new_goal = event.widget.find_withtag("current")
        except:
            pass
        else:
            self.canvas.itemconfig(new_goal, fill='red')
            new_pos = self.canvas.gettags(new_goal)
            self.canvas.itemconfig(self.grid[self.goal[1]][self.goal[0]], fill='white')
            self.goal = [int(new_pos[0]), int(new_pos[1])]

    def set_start_pos(self, event):
        try:
            new_start = event.widget.find_withtag("current")
        except:
            pass
        else:
            self.canvas.itemconfig(new_start, fill='green')
            new_pos = self.canvas.gettags(new_start)
            self.canvas.itemconfig(self.grid[self.start[1]][self.start[0]], fill='white')
            self.start = [int(new_pos[0]), int(new_pos[1])]
            self.pos = [int(new_pos[0]), int(new_pos[1])]

    def reset_board(self):
        # Make the Board all White
        for i in range(self.sq):
            for j in range(self.sq):
                self.canvas.itemconfig(self.grid[i][j], fill='white')

        # Make Start and Goal squares their respective colors
        self.canvas.itemconfig(self.grid[self.goal[1]][self.goal[0]], fill='red')
        self.canvas.itemconfig(self.grid[self.start[1]][self.start[0]], fill='green')

        # Reinitialize variables
        self.pos = self.start
        self.stack = []
        self.path = []
        self.pred = {}

        # Add walls back
        for i in self.walls:
            self.canvas.itemconfig(self.grid[i[1]][i[0]], fill='gray')


    # Add walls to the Grid
    def add_walls(self, event):
        x = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        y = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
        for i in range(self.sq):
            for j in range(self.sq):
                x_1, y_1, x_2, y_2 = self.canvas.coords(self.grid[i][j])
                if x > x_1 and x < x_2 and y > y_1 and y < y_2:
                    self.canvas.itemconfig(self.grid[i][j], fill='gray')
                    self.walls.append([j, i])

    def clear_walls(self):
        for i in self.walls:
            self.canvas.itemconfig(self.grid[i[1]][i[0]], fill='white')
        self.walls = []