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
    heap_handler = Heap()
    algo_a_comp_counter = heap_handler.build_min_heap(heap_array)
    k_smallest_array = np.empty(k, dtype=int)
    for i in range(k):
        heap_array, smallest_number, heap_extract_min_iteration_counter = heap_handler.heap_extract_min(heap_array)
        algo_a_comp_counter += heap_extract_min_iteration_counter
        k_smallest_array[i] = smallest_number
    return k_smallest_array, algo_a_comp_counter


def second_algo(k: int, pivot_array: np.array) -> Tuple[np.array, int]:
    pivot_handler = PivotSort()
    the_k_smallest, randomize_select_counter = pivot_handler.randomized_select(pivot_array, 0, len(pivot_array) - 1, k, 0)
    algo_b_comp_counter = pivot_handler.quicksort(pivot_array, 0, k - 1, randomize_select_counter)
    return pivot_array[0:k], algo_b_comp_counter


def main(run_user_input: bool = True, args: Tuple[int, int, np.array] = None) -> Union[None, Tuple[np.array, np.array]]:
    """
    This is the main func of this project.
    IMPORTANT - This func can be call either way by the user (which means we will ask the user to insert some data) or
    in cli mode for debug use.
    :param run_user_input: rather to run as "ui" or as "cli". default True, so we will use user input
    :param args: if we want to run as cli, sends the args for the func
    :return: if run in cli mode, the arrays of the k the smallest objects, from each algorithm's
    """
    n, k, n_array = get_user_input() if run_user_input else args
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

    if not run_user_input:
        return k_smallest_array_heap, k_smallest_array_pivot


if __name__ == '__main__':
    main()
