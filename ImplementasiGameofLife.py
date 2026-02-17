class GameOfLife:
    def __init__(self, rows, cols):
        self.grid = Array2D(rows, cols)

    def setAlive(self, row, col):
        self.grid[row, col] = 1

    def isAlive(self, row, col):
        return self.grid[row, col] == 1

    def countNeighbors(self, row, col):
        directions = [-1, 0, 1]
        count = 0
        for dr in directions:
            for dc in directions:
                if dr == 0 and dc == 0:
                    continue
                r = row + dr
                c = col + dc
                if 0 <= r < self.grid.numRows() and 0 <= c < self.grid.numCols():
                    if self.grid[r, c] == 1:
                        count += 1
        return count

    def nextGeneration(self):
        newGrid = Array2D(self.grid.numRows(), self.grid.numCols())

        for r in range(self.grid.numRows()):
            for c in range(self.grid.numCols()):
                alive = self.isAlive(r, c)
                neighbors = self.countNeighbors(r, c)

                if alive:
                    if neighbors == 2 or neighbors == 3:
                        newGrid[r, c] = 1
                    else:
                        newGrid[r, c] = 0
                else:
                    if neighbors == 3:
                        newGrid[r, c] = 1
                    else:
                        newGrid[r, c] = 0

        self.grid = newGrid

    def display(self):
        for r in range(self.grid.numRows()):
            for c in range(self.grid.numCols()):
                print("■" if self.grid[r, c] == 1 else ".", end=" ")
            print()
        print()
