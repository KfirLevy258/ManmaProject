import random
from typing import Tuple

import numpy as np


class Randomize:

    @staticmethod
    def partition(p: int, r: int, a: np.array) -> Tuple[int, int]:
        pivot = a[r]
        ptr = p
        comp_counter = 0
        for i in range(p, r):
            if a[i] <= pivot:
                a[i], a[ptr] = a[ptr], a[i]
                comp_counter += 1
                ptr += 1
        a[ptr], a[r] = a[r], a[ptr]
        return ptr, comp_counter

    def randomized_partition(self, a: np.array, p: int, r: int) -> Tuple[int, int]:
        i = random.randrange(p, r)
        a[i], a[r] = a[r], a[i]
        return self.partition(p, r, a)

    def randomized_select(self, a: np.array, p: int, r: int, i: int, comp_counter: int) -> Tuple[int, int]:
        if p == r:
            return a[p], comp_counter
        q, temp_comp = self.randomized_partition(a, p, r)
        comp_counter = comp_counter + temp_comp
        k = q - p + 1
        if i == k:
            return a[q]
        elif i < k:
            return self.randomized_select(a, p, q - 1, i, comp_counter)
        else:
            return self.randomized_select(a, p + 1, r, i - k, comp_counter)

    def quicksort(self, a: np.array, p: int, r: int, comp_counter: int) -> Tuple[np.array, int]:
        if p < r:
            q, partition_counter = self.partition(p, r, a)
            _, right_counter = self.quicksort(a, p, q - 1, comp_counter)
            _, left_counter = self.quicksort(a, q + 1, r, comp_counter)
            comp_counter += partition_counter + right_counter + left_counter
        return a, comp_counter
