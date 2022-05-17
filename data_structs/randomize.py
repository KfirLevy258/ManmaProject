import random
from typing import Tuple

import numpy as np

from support_functions import exchange


class Randomize:

    @staticmethod
    def partition(a: np.array, p: int, r: int) -> Tuple[int, np.array]:
        x = a[r]
        i = p - 1
        for j in range(p, r - 1):
            if a[j] <= x:
                i = i + 1
                a = exchange(a, j, i)
        a = exchange(a, i + 1, r)
        return i + 1, a

    def randomized_partition(self, a: np.array, p: int, r: int) -> Tuple[int, np.array]:
        i = random.randrange(p, r)
        a = exchange(a, r, i)
        return self.partition(a, p, r)

    def randomized_select(self, a: np.array, p: int, r: int, i: int) -> int:
        if p == r:
            return a[p]
        q, a = self.randomized_partition(a, p, r)
        k = q - p + 1
        if i == k:
            return a[q]
        elif i < k:
            return self.randomized_select(a, p, q - 1, i)
        else:
            return self.randomized_select(a, p + 1, r, i - k)

