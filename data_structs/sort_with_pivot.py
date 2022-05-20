import random

import numpy as np


class PivotSort:
    comp_counter = 0

    def partition(self, p: int, r: int, a: np.array) -> int:
        pivot = a[r]
        ptr = p
        for i in range(p, r):
            if a[i] <= pivot:
                a[i], a[ptr] = a[ptr], a[i]
                ptr += 1
            self.comp_counter += 1
        a[ptr], a[r] = a[r], a[ptr]
        return ptr

    def randomized_partition(self, a: np.array, p: int, r: int) -> int:
        i = random.randrange(p, r)
        a[i], a[r] = a[r], a[i]
        return self.partition(p, r, a)

    def randomized_select(self, a: np.array, p: int, r: int, i: int, comp_counter: int) -> int:
        if p == r:
            return a[p]
        q = self.randomized_partition(a, p, r)
        k = q - p + 1
        if i == k:
            return a[q]
        elif i < k:
            return self.randomized_select(a, p, q - 1, i, comp_counter)
        else:
            return self.randomized_select(a, q + 1, r, i - k, comp_counter)

    def quicksort(self, a: np.array, p: int, r: int) -> None:
        if p < r:
            q = self.partition(p, r, a)
            self.quicksort(a, p, q - 1)
            self.quicksort(a, q + 1, r)
