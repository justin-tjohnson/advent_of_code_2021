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

depths_list = depths_string.splitlines()

depths = [int(depth) for depth in depths_list]


statuses = 0

for index in range(len(depths)):

    if index == 0:
        continue
        
    elif depths[index] > depths[index-1]:
        statuses += 1

print(statuses)

