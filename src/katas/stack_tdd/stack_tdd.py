import array


class StackUnderflowException(LookupError):
    pass


class Stack:
    def __init__(self) -> None:
        self._size: int = 0
        self._elements: array = array.array('i', [0, 0])

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, element: int) -> None:
        if self._size == len(self._elements):
            self._elements.append(0)
        self._elements[self._size] = element
        self._size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise StackUnderflowException("Tried to pop an empty stack.")
        self._size -= 1
        element: int = self._elements[self._size]
        self._elements[self._size] = 0
        return element
