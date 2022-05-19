from typing import Tuple

import numpy as np

class Heap:
    @staticmethod
    def parent(i) -> int:
        return int(i / 2)

    @staticmethod
    def left(i) -> int:
        return 2 * i

    @staticmethod
    def right(i) -> int:
        return (2 * i) + 1

    def min_heapify(self, a: np.array, i: int, comp_counter: int) -> int:
        left = self.left(i)
        right = self.right(i)
        if left < len(a) and a[left] < a[i]:
            smallest = left
            comp_counter += 1
        else:
            comp_counter += 1
            smallest = i
        if right < len(a) and a[right] < a[smallest]:
            smallest = right
            comp_counter += 1
        if smallest is not i:
            a[smallest], a[i] = a[i], a[smallest]
            comp_counter += self.min_heapify(a, smallest, comp_counter)
        return comp_counter

    def build_min_heap(self, a: np.array) -> int:
        heap_size = len(a)
        comp_counter = 0
        for i in range(int(heap_size / 2), -1, -1):
            comp_for_iteration = self.min_heapify(a, i, 0)
            comp_counter += comp_for_iteration
        return comp_counter

    def heap_extract_min(self, a: np.array) -> Tuple[np.array, int, int]:
        smallest = a[0]
        a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
        a = a[:-1]
        comp_counter = self.min_heapify(a, 0, 0)
        return a, smallest, comp_counter

