import random as random
import vpython as vp

class PathFinder:
    def __init__(self):
        self.pathStack = []
        self.solved = False

    grid = [
            [
                [
                    1, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
            ],
            [
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
            ],
            [
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
            ],
            [
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
            ],
            [
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 0
                ],
                [
                    0, 0, 0, 0, 1
                ],
            ]
        ]
    def setSeed(self):
        num = input("Enter a number to seed the maze (ex. 1124): ")
        random.seed(num)

    #create a random maze based on the seed given in self.setSeed()
    def createMaze(self):
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    rand = random.random()
                    if rand > 0.5:
                        self.grid[i][j][k] = 1
                    else:
                        self.grid[i][j][k] = 0
            self.grid[0][0][0] = 1
            self.grid[4][4][4] = 1

    def printMaze(self):
        if self.solved:
            print("----Solved Maze----\n")
        else:
            print("----Maze----\n")
        for i in self.grid:
            for j in i:
                print(j)
            print("\n")

    def printSolution(self):
        print("----Solution Path----\n")
        for i in self.pathStack:
            print(i)
        print("\n")

    def solveMaze(self):
        if self.findPath(0, 0, 0):
            self.printSolution()
            print("Found the exit!\n")
            self.solved = True
            return True
        else:
            print("Exit not found... :(\n")

    def findPath(self, level, row, col):
        if level > 4 or level < 0 or row > 4 or row < 0 or col > 4 or col < 0:
            return False
        if self.grid[level][row][col] == 0:
            return False
        if self.grid[level][row][col] == 2:
            return False
        if level == 4 and row == 4 and col == 4:
            return True
        self.grid[level][row][col] = 2
        if (self.findPath(level + 1, row, col) or
            self.findPath(level - 1, row, col) or
            self.findPath(level, row + 1, col) or
            self.findPath(level, row - 1, col) or
            self.findPath(level, row, col + 1) or
            self.findPath(level, row, col - 1)):
                self.pathStack.append("(" + str(level) + ", " + str(row) + ", " + str(col) + ")")
                return True
        else:
            return False

    #use vpython to visualize the maze in 3D
    def drawMaze(self):
        colorGradient = .2
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    if self.grid[i][j][k] == 2:
                        self.grid[i][j][k] = vp.box(pos=vp.vector(i - 2, j - 2, k - 2),
                                                    size=vp.vector(0.5, 0.5, 0.5),
                                                    color=vp.vector(0, colorGradient, 0),
                                                    opacity=0.6)
                        colorGradient += .04
                    else:
                        self.grid[i][j][k] = vp.box(pos=vp.vector(i - 2, j - 2, k - 2),
                                                    size=vp.vector(0.5, 0.5, 0.5),
                                                    color=vp.vector(1, 1, 1),
                                                    opacity=0.2)

        #color the start box blue
        self.grid[0][0][0] = vp.box(pos=vp.vector(-2, -2, -2),
                                    size=vp.vector(0.5, 0.5, 0.5),
                                    color=vp.vector(0, 0, 1))

        #color the end box red
        self.grid[4][4][4] = vp.box(pos=vp.vector(2, 2, 2),
                                    size=vp.vector(0.5, 0.5, 0.5),
                                    color=vp.vector(1, 0, 0))

        vp.scene.title = "Solution Path"
        vp.scene.caption = "Maze Status: Solved\n\nLegend:\n Blue: Maze start\n Red: Maze exit\n Green: Path (increases in brightness as path approaches maze exit)\n White: Unused spaces/barriers\n\nInstructions:\n Use shift + mouse to reposition camera\n Use ctrl + mouse to rotate camera\n Scroll to zoom in/out"
        vp.scene.camera.pos = vp.vector(0, 6, -7)
        vp.scene.camera.axis = vp.vector(0, 1.5, 1.725)
        vp.scene.camera.rotate(angle=3.14159, axis=vp.vector(0, 0, 1))
        vp.scene.background = vp.color.gray(luminance=0.1)