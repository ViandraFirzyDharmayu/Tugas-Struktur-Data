class Array:
    def __init__(self, size):
        assert size > 0, "Size harus > 0"
        self._size = size
        self._elements = [None] * size

    def length(self):
        return self._size

    def __getitem__(self, index):
        assert 0 <= index < self._size, "Index di luar batas"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert 0 <= index < self._size, "Index di luar batas"
        self._elements[index] = value

    def clearing(self, value):
        for i in range(self._size):
            self._elements[i] = value

    def __iter__(self):
        return iter(self._elements)
