import numpy as np
from typing import Union, List, Tuple

import help_funcs_and_consts


class UserInputs:
    """
    This class is in charge of all user inputs for our main func
    """

    @staticmethod
    def _validate_user_input(user_input: str, type_of_valid_input: any, valid_values: List = None) -> Tuple[any, bool]:
        """
        This function validates the user input is in a specific type and in the list of valid values.
        :param user_input: the input for the user
        :param type_of_valid_input: the type the input should be in
        :param valid_values: list of all the possible values
        :return: input in the type format and bool if the input is valid
        """
        try:
            user_input_to_int = type_of_valid_input(user_input)
            return user_input_to_int, user_input_to_int in valid_values if valid_values is not None else True
        except ValueError:
            return user_input, False

    def _get_input_until_valid(self, msg: str, valid_type: any, valid_values: List = None) -> any:
        """
        This func helps us to get input from user until the input is valid.
        :param msg: the msg to print to the screen for the user
        :param valid_type: the type the input should be in
        :param valid_values: the optional values for the user
        :return: the value of the user, in the required type
        """
        while True:
            user_input = input(msg)
            user_input, valid_input = self._validate_user_input(user_input, valid_type, valid_values)
            if valid_input:
                break
            print(f"'{user_input}' is not valid input! Please retry.")
        return user_input

    def get_user_n_length(self) -> int:
        """
        Get from user the value for 'n' parameter
        :return: n value
        """
        return self._get_input_until_valid(
            msg="Please enter your 'n_length' array length:\n",
            valid_type=int,
        )

    def fill_array_with_n_numbers(self, n_length: int) -> np.array:
        """
        This function asks the user how to fill the array
        :param n_length: the size of the array
        :return: fill array with n values
        """
        user_input = self._get_input_until_valid(
            msg="Would you like to enter the values for the array or you want them to generate automatically?\n"
                "1 - To fill the array with random numbers in range [0 - 999]\n"
                "2 - To enter your own values\n",
            valid_type=int,
            valid_values=[1, 2]
        )
        match user_input:
            case 1:
                # This case the user want all random numbers
                return help_funcs_and_consts.get_random_array(n_length)
            case 2:
                # This case the user want to fill the array himself
                # Creating a new array at the required size
                array_to_return = np.empty(n_length, dtype=int)
                # Asks the user for input until we fill the array
                for iteration in range(n_length):
                    user_input = self._get_input_until_valid(
                        msg=f"Enter the {iteration + 1} number:\n",
                        valid_type=int,
                    )
                    array_to_return[iteration] = user_input
                return array_to_return
        # Just a nice easter-egg
        help_funcs_and_consts.MamanException("You broke the system, you shouldn't got this far")

    def get_user_k_value(self, n_length: int) -> int:
        """
        Get from user the value for 'k' parameter
        :param n_length: the length of the array, we want to make sure k is in the array
        :return: k value
        """
        return self._get_input_until_valid(
            msg="Please enter your 'k' number:\n",
            valid_type=int,
            valid_values=[i for i in range(n_length + 1)]
        )
