import numpy as np


class ArrayConsts:
    """
    Class of consts
    """
    MIN_DEFAULT_VALUE = 0
    MAX_DEFAULT_VALUE = 999


class MamanException(Exception):
    """
    A general exception for this project
    """
    def __init__(self, msg: str):
        super(MamanException, self).__init__(msg)


def get_random_array(array_size: int) -> np.array:
    """
    This function will return an array with random numbers in the range of ArrayConsts
    :param array_size: the size of the array
    :return: array of random numbers
    """
    return np.random.randint(ArrayConsts.MIN_DEFAULT_VALUE, ArrayConsts.MAX_DEFAULT_VALUE,
                             size=array_size)


def padding() -> None:
    """
    Just padding for butty
    """
    print()
    print("#" * 50)
    print()
