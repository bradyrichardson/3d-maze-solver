import vpython as vp
from pathfinder import *

maze = PathFinder()

maze.setSeed()
maze.createMaze()
maze.printMaze()
if (maze.solveMaze()):
    maze.printMaze()
    maze.drawMaze()
