# Minesweeper
A simple minesweeper game in Python
The game is run in terminal

## Instructions

To start, you need to run the python file in your terminal:

    python3 minesweeper.py

You will see the mine field you need to make safe
To choose a square, use 0-indexed coordinates, separated by a space (i.e the top-left square is 0 0)
The game will show you which square you chose with a '?' sign and prompt you with an action that you'd like to take (**r**eveal the square, plant a **m**ine or **n**o action (choose another square))
- **R**evealing the square will show you how many mines are adjacent (including corners) to this square. '-' sign means there are no mines around it
- Planting a **M**ine will mark a square with an 'm' sign representing a mine, however it is not confirming if the mine exists on this square. If there is already a mine marked on this square, it will remove it.
- **N**o action will prompt you to enter another coordinate

The game will continue until there are no squares left take action with.

## Other

### Current implementation can:

 - Reveal squares
 - Place/remove mines
 - Safe checks for coordinate values
 - Auto reveal neighboring squares if the current one has no mines near it
 - Reveal neighboring squares if there are enough mines marked around current square
 - Limit number of mines placed
 - Print filled in grid for debugging purposes

### Future updates:

- GUI !!!

### Personalisation

- If you'd like to set your own size of the minefield and number of mines, change *grid_width*, *grid_height* and *grid_mines* variables