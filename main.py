import numpy as np
from typing import Tuple

from data_structs.heap import Heap
from user_inputs import UserInputs
from data_structs.sort_with_pivot import PivotSort


def get_user_input() -> Tuple[int, int, np.array]:
    user_input_interface = UserInputs()
    n = user_input_interface.get_user_n_length()
    k = user_input_interface.get_user_k_value(n)
    n_array = user_input_interface.fill_array_with_n_numbers(n)
    return n, k, n_array

def main(run_user_input: bool = True, args: Tuple[int, int, np.array] = None) -> None:
    n, k, n_array = get_user_input() if run_user_input else args
    print(n_array)

    heap_handler = Heap()
    pivot_handler = PivotSort()

    print("#" * 30)
    print(f"Starting first algorithm:")
    heap_array, pivot_array = n_array, n_array
    algo_a_comp_counter = heap_handler.build_min_heap(heap_array)
    k_smallest_array = []
    for i in range(k):
        heap_array, smallest_number, heap_extract_min_iteration_counter = heap_handler.heap_extract_min(heap_array)
        algo_a_comp_counter += heap_extract_min_iteration_counter
        k_smallest_array.append(smallest_number)
    print(f"The k smallest elements are: {k_smallest_array}")
    print(f"The numbers of comparisons for this sort were: {algo_a_comp_counter}")
    print("#" * 30)
    print(f"Starting second algorithm:")
    the_k_smallest, randomize_select_counter = pivot_handler.randomized_select(pivot_array, 0, len(pivot_array) - 1, k, 0)
    algo_b_comp_counter = pivot_handler.quicksort(pivot_array, 0, k, randomize_select_counter)
    print(f"The k smallest elements are: {pivot_array[0:k]}")
    print(f"The numbers of comparisons for this sort were: {algo_b_comp_counter}")
    print("#" * 30)


if __name__ == '__main__':
    main()
