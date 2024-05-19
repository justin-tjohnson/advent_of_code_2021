depths_string ="""199
200
208
210
200
207
240
269
260
263"""

def number_of_times_list_element_increases(depths):
    statuses = 0
    for index in range(len(depths)):

        if index == 0:
            continue
            
        elif depths[index] > depths[index-1]:
            statuses += 1

    return statuses

depths_list = depths_string.splitlines()

depths = [int(depth) for depth in depths_list]

window_sums = []

for index in range(len(depths)):

    if index < 2:
        continue
    
    window_sum = depths[index-2] + depths[index-1] + depths[index]
    window_sums.append(window_sum)


print(number_of_times_list_element_increases(window_sums))




