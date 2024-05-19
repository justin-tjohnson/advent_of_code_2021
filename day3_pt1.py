sub_params_string = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

sub_params_list = sub_params_string.splitlines()


def find_gamma_and_epsilon(sub_params_list):
    num_of_bits = len(sub_params_list[0])
    qty_of_numbers = len(sub_params_list)

    gamma = ""
    epsilon = ""

    for i in range(num_of_bits):

        num_of_1_bits = sum([int(number[i]) for number in sub_params_list])
        num_of_0_bits = qty_of_numbers - num_of_1_bits

        if num_of_1_bits > num_of_0_bits:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return gamma, epsilon

def find_power_consumption(gamma, epilson):

    return int(gamma, 2) * int(epilson, 2)




gamma, epilson =  find_gamma_and_epsilon(sub_params_list)

print(find_power_consumption(gamma, epilson))





