from src.interface.Sequence import Sequence

class Array_seq(Sequence):
    def __init__(self) -> None:
        self.A = []
        self.size = 0

    def __len__(self) -> int:
        return self.size
    
    def __iter__(self):
        yield from iter(self.A)

    def build(self, X) -> None:
        self.A = [a for a in X]
        self.size = len(X)

    def get_at(self, i: int):
        return self.A[i]
    
    def set_at(self, i, x):
        self.A[i] = x

    def _copy_forward(self, i, n, A, j):
        for k in range(n):
            A[j + k] = self.A[i + k]

    def _copy_backward(self, i, j):
        ...

    def insert_at(self, i, x):
        n = len(self)
        A = [None] * (self.size + 1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - i, A, i + 1)
        self.build(A)

    def delete_at(self, i):
        n = len(self)
        A = [None] * (self.size - 1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)

    def insert_last(self, x):
        self.insert_at(self.size, x)

    def delete_last(self):
        return self.delete_at(self.size - 1) 