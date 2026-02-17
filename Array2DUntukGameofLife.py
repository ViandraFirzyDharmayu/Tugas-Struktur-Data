class Array2D:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._data = Array(rows)
        for i in range(rows):
            self._data[i] = Array(cols)

    def numRows(self):
        return self._rows

    def numCols(self):
        return self._cols

    def __getitem__(self, index):
        row, col = index
        return self._data[row][col]

    def __setitem__(self, index, value):
        row, col = index
        self._data[row][col] = value

    def clear(self, value):
        for i in range(self._rows):
            self._data[i].clearing(value)
