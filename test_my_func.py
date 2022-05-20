import pytest
import numpy as np

from main import main, first_algo, second_algo
import help_funcs_and_consts


class TestMyFunc:
    """
    This class is build to test this project via pytest modules
    """

    @pytest.fixture(params=[8, 50, 100])
    def k(self, request) -> int:
        """
        This fixture will return specific k we're checking from the k's list
        :return: one value of k from the k's list
        """
        return request.param

    @pytest.fixture(params=[100, 200, 500, 1000])
    def n(self, request) -> int:
        """
        This fixture will return specific n we're checking from the n's list
        :return: one value of n from the k's list
        """
        return request.param

    def test_my_func(self, n, k):
        """
        This function runs the main in cli mode for all the n and k options we need to check
        :param n: the specific n we're checking
        :param k: the specific k we're checking
        """
        print()
        print(f"n: {n}, k: {k}")
        n_array = help_funcs_and_consts.get_random_array(n)
        heap_array, pivot_array = n_array, n_array
        k_smallest_array_heap, algo_a_comp_counter = first_algo(k, heap_array)
        k_smallest_array_pivot_first, algo_b_comp_counter_first = second_algo(k, pivot_array)
        k_smallest_array_pivot_second, algo_b_comp_counter_second = second_algo(k, pivot_array)
        k_smallest_array_pivot_third, algo_b_comp_counter_third = second_algo(k, pivot_array)
        print(f"first algo comp numbers: {algo_a_comp_counter}")
        print(f"second algo comp numbers: {algo_b_comp_counter_first, algo_b_comp_counter_second, algo_b_comp_counter_third}")
        print()
        # Check that all three arrays are the same (from the same algorithm)
        assert np.array_equal(k_smallest_array_pivot_first, k_smallest_array_pivot_third) \
               and np.array_equal(k_smallest_array_pivot_first, k_smallest_array_pivot_second)
        # Check that these two arrays are the same (from different algorithms)
        assert np.array_equal(k_smallest_array_heap, k_smallest_array_pivot_first)
