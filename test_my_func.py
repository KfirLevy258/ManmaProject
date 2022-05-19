import pytest
import numpy as np

from main import main
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
        first, second = main(run_user_input=False, args=(n, k, help_funcs_and_consts.get_random_array(n)))
        print()
        assert np.array_equal(first, second)
