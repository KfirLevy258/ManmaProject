import numpy as np
from typing import Tuple, Union

from data_structs.heap import Heap
from user_inputs import UserInputs
from help_funcs_and_consts import padding
from data_structs.sort_with_pivot import PivotSort


def get_user_input() -> Tuple[int, int, np.array]:
    """
    This function gets the values of n, k and n_array from the user
    :return: n and k ad int's and n_array which is array with n length
    """
    user_input_interface = UserInputs()
    n = user_input_interface.get_user_n_length()
    k = user_input_interface.get_user_k_value(n)
    n_array = user_input_interface.fill_array_with_n_numbers(n)
    return n, k, n_array


def first_algo(k: int, heap_array: np.array) -> Tuple[np.array, int]:
    """
    This function is performing the first algorithm
    :param k: the selected k
    :param heap_array: the array of numbers
    :return: the k smallest arrays and the comparisons counter
    """
    heap_handler = Heap()
    heap_handler.build_min_heap(heap_array)
    k_smallest_array = np.empty(k, dtype=int)
    for i in range(k):
        heap_array, smallest_number = heap_handler.heap_extract_min(heap_array)
        k_smallest_array[i] = smallest_number
    return k_smallest_array, heap_handler.comp_counter


def second_algo(k: int, pivot_array: np.array) -> Tuple[np.array, int]:
    """
    This function is performing the second algorithm
    :param k: the selected k
    :param pivot_array: the array of numbers
    :return: the k smallest arrays and the comparisons counter
    """
    pivot_handler = PivotSort()
    pivot_handler.randomized_select(pivot_array, 0, len(pivot_array) - 1, k, 0)
    pivot_handler.quicksort(pivot_array, 0, k - 1)
    return pivot_array[0:k], pivot_handler.comp_counter


def main() -> None:
    """
    This is the main func of this project.
    """
    n, k, n_array = get_user_input()
    # print(n_array)
    heap_array, pivot_array = n_array, n_array

    padding()
    print(f"Starting first algorithm:")
    k_smallest_array_heap, algo_a_comp_counter = first_algo(k, heap_array)
    print(f"The k smallest elements are: {k_smallest_array_heap}")
    print(f"The numbers of comparisons for this sort were: {algo_a_comp_counter}")
    padding()
    print(f"Starting second algorithm:")
    k_smallest_array_pivot, algo_b_comp_counter = second_algo(k, pivot_array)
    print(f"The k smallest elements are: {k_smallest_array_pivot}")
    print(f"The numbers of comparisons for this sort were: {algo_b_comp_counter}")
    padding()


if __name__ == '__main__':
    main()
