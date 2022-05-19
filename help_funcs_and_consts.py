import numpy as np


class ArrayConsts:
    MIN_DEFAULT_VALUE = 0
    MAX_DEFAULT_VALUE = 999


class MamanException(Exception):
    def __init__(self, msg: str):
        super(MamanException, self).__init__(msg)


def get_random_array(array_size: int) -> np.array:
    return np.random.randint(ArrayConsts.MIN_DEFAULT_VALUE, ArrayConsts.MAX_DEFAULT_VALUE,
                             size=array_size)


def padding() -> None:
    print()
    print("#" * 50)
    print()
