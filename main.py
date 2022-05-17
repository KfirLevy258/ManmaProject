import logging
import numpy as np
from typing import List, Union, Tuple

import Consts


class MamanException(Exception):
    def __init__(self, msg: str):
        super(MamanException, self).__init__(msg)


class UserInputs:
    @staticmethod
    def _validate_user_input(user_input: str, type_of_valid_input: any, valid_values: List = None) -> Tuple[any, bool]:
        try:
            user_input_to_int = type_of_valid_input(user_input)
            return user_input_to_int, user_input_to_int in valid_values if valid_values is not None else True
        except ValueError:
            return user_input, False

    def _get_input_until_valid(self, msg: str, valid_type: any, valid_values: List = None) -> int:
        while True:
            user_input = input(msg)
            user_input, valid_input = self._validate_user_input(user_input, valid_type, valid_values)
            if valid_input:
                break
            print(f"'{user_input}' is not valid input! Please retry.")
        return user_input

    def fill_array_with_n_numbers(self, n: int) -> Union[np.array]:
        user_input = self._get_input_until_valid(
            msg="Would you like to enter the values for the array or you want them to generate automatically?\n"
                "1 - To fill the array with random numbers in range [0 - 999]\n"
                "2 - To enter your own values\n",
            valid_type=int,
            valid_values=[1, 2]
        )
        match user_input:
            case 1:
                return np.random.randint(Consts.ArrayConsts.MIN_DEFAULT_VALUE, Consts.ArrayConsts.MAX_DEFAULT_VALUE,
                                         size=n)
            case 2:
                array_to_return = np.empty(n, dtype=np.int8)
                for iteration in range(n):
                    user_input = self._get_input_until_valid(
                        msg=f"Enter the {iteration + 1} number:\n",
                        valid_type=int,
                    )
                    array_to_return[iteration] = user_input
                return array_to_return
        MamanException("Ypu broke the system, you shouldn't got this far")

    def get_user_k_value(self) -> int:
        return self._get_input_until_valid(
            msg="Please enter your 'k' number:\n",
            valid_type=int,
        )


def section_a(n: int, k: int) -> np.array:
    input()


if __name__ == '__main__':
    u = UserInputs()
    print(u.fill_array_with_n_numbers(2))
    # print(fill_array_with_n_numbers(10))