import logging
import numpy as np
from typing import List, Union


class MamanException(Exception):
    def __init__(self, msg: str):
        super(MamanException, self).__init__(msg)


def validate_user_input(user_input: str, valid_values: List, type_of_valid_input: any) -> bool:
    try:
        user_input_to_int = type_of_valid_input(user_input)
        return user_input_to_int in valid_values
    except ValueError:
        return False


def fill_array_with_n_numbers(n: int) -> np.array:
    while True:
        user_answer = input("Would you like to enter the values for the array or you want them to generate automatically?\n"
                            "1 - To fill the array with random numbers in range [0 - 999]\n"
                            "2 - To enter your own values\n")
        if validate_user_input(user_answer, [1, 2], int):
            break
        print("Your answer is not valid, please retry")

    match user_answer:
        case


def section_a(n: int, k: int) -> np.array:
    input()

if __name__ == '__main__':
    fill_array_with_n_numbers(10)