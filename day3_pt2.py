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


def find_oxygen_or_c02_rating(sub_params_list, rating_type):
    num_of_bits = len(sub_params_list[0])

    remaining = sub_params_list

    for i in range(num_of_bits):

        num_of_1_bits = sum([int(number[i]) for number in remaining])
        num_of_0_bits = len(remaining) - num_of_1_bits

        if rating_type == 'oxygen':
            #most common
            determinator = "1" if num_of_1_bits >= num_of_0_bits else "0"
        else:
            #least common
            determinator = "0" if num_of_1_bits >= num_of_0_bits else "1"

        remaining = [number for number in remaining if determinator == number[i]]

        if len(remaining) == 1:
            return remaining[0]


def find_life_support(oxygen, c02):

    return int(oxygen, 2) * int(c02, 2)


oxygen_result = find_oxygen_or_c02_rating(sub_params_list, "oxygen")
c02_result = find_oxygen_or_c02_rating(sub_params_list, "c02")

print(find_life_support(oxygen_result, c02_result))





