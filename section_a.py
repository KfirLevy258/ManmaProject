from user_inputs import UserInputs

if __name__ == '__main__':
    user_input_interface = UserInputs()
    n = user_input_interface.get_user_n_length()
    k = user_input_interface.get_user_k_value(n)
    n_array = user_input_interface.fill_array_with_n_numbers(n)
    print(n_array)

