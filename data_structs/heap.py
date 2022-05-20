from typing import Tuple

import numpy as np

class Heap:
    comp_counter = 0

    @staticmethod
    def parent(i) -> int:
        return int(i / 2)

    @staticmethod
    def left(i) -> int:
        return 2 * i

    @staticmethod
    def right(i) -> int:
        return (2 * i) + 1

    def min_heapify(self, a: np.array, i: int) -> None:
        left = self.left(i)
        right = self.right(i)
        if left < len(a) and a[left] < a[i]:
            smallest = left
        else:
            smallest = i
        if right < len(a) and a[right] < a[smallest]:
            smallest = right
        self.comp_counter += 2
        if smallest is not i:
            a[smallest], a[i] = a[i], a[smallest]
            self.min_heapify(a, smallest)

    def build_min_heap(self, a: np.array) -> None:
        heap_size = len(a)
        self.comp_counter = 0
        for i in range(int(heap_size / 2), -1, -1):
            self.min_heapify(a, i)

    def heap_extract_min(self, a: np.array) -> Tuple[np.array, int]:
        smallest = a[0]
        a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
        a = a[:-1]
        self.min_heapify(a, 0)
        return a, smallest
