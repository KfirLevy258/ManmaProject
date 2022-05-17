import numpy as np


def exchange(array: np.array, first_index: any, second_index: any) -> np.array:
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp
    return array
