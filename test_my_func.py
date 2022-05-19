import pytest
import numpy as np

from main import main
import help_funcs_and_consts


class TestMyFunc:

    @pytest.fixture(params=[8, 50, 100])
    def k(self, request) -> int:
        return request.param

    @pytest.fixture(params=[100, 200, 500, 1000])
    def n(self, request) -> int:
        return request.param

    def test_my_func(self, n, k):
        print()
        print(f"n: {n}, k: {k}")
        first, second = main(run_user_input=False, args=(n, k, help_funcs_and_consts.get_random_array(n)))
        print()
        assert np.array_equal(first, second)
