import numpy as np


class Heap:
    @staticmethod
    def parent(i) -> int:
        return int(i/2)

    @staticmethod
    def left(i) -> int:
        return 2 * i

    @staticmethod
    def right(i) -> int:
        return (2 * i) + 1

    def min_heapify(self, a: np.array, i: int) -> np.array:
        left = self.left(i)
        right = self.right(i)
        smallest = left if left < len(a) and a[left] < a[i] else i
        if right < len(a) and a[right] < a[smallest]:
            smallest = right
        if smallest is not i:
            temp = a[i]
            a[i] = a[smallest]
            a[smallest] = temp
            self.min_heapify(a, smallest)
        return a

    def build_min_heap(self, a: np.array) -> np.array:
        heap_size = len(a)
        for i in range(int(heap_size / 2), -1, -1):
            a = self.min_heapify(a, i)
        return a

    def heap_extract_min(self, a: np.array) -> np.array:
        a[0] = a[len(a) - 1]
        a = a[:-1]
        return self.min_heapify(a, 0)
