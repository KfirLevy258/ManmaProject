from data_structs.heap import Heap
from user_inputs import UserInputs
from data_structs.sort_with_pivot import Randomize

if __name__ == '__main__':
    # user_input_interface = UserInputs()
    # n = user_input_interface.get_user_n_length()
    # k = user_input_interface.get_user_k_value(n)
    # n_array = user_input_interface.fill_array_with_n_numbers(n)
    # print(n_array)

    n = 10
    k = 3
    n_array = [190, 508, 733, 154, 149, 596, 236, 270, 669, 538]

    heap_handler = Heap()
    randomize = Randomize()

    heap_array, s = n_array, n_array
    heap_comp_counter = heap_handler.build_min_heap(heap_array)
    for i in range(k):
        heap_array, heap_extract_min_iteration_counter = heap_handler.heap_extract_min(heap_array)
        heap_comp_counter += heap_extract_min_iteration_counter

    print(heap_comp_counter)
    print(heap_array)

    # randomize_array, the_k_smallest_number, randomize_comp_counter = randomize.randomized_select(n_array, 0, len(n_array) - 1, k, 0)
    # print(randomize_array)
    # print(the_k_smallest_number)
    # print(randomize_comp_counter)

