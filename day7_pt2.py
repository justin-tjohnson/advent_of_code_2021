crab_positions = [16,1,2,0,4,2,7,1,2,14]


def calculate_movement_map(crab_positions):
    # creates map between number of crab movements and fuel used
    movement_map = {0: 0}
    for crap_pos in range(min(crab_positions), max(crab_positions)+1):
        # no fuel if number of moves is 0
        if crap_pos == 0:
            continue
    
        movement_map[crap_pos] = movement_map[crap_pos-1] + crap_pos
    return movement_map

def calculate_least_fuel(crab_positions, movement_map):
    #calculates postions that all crabs move to that uses the least fuel
    crab_fuel_map = {}
    for aligned_pos in range(min(crab_positions), max(crab_positions)+1):
        crab_fuel_list = [movement_map[abs(aligned_pos-crab_position)] for crab_position in crab_positions]
        crab_fuel_map[aligned_pos] = sum(crab_fuel_list)
        
    return min(crab_fuel_map.values())

movement_map = calculate_movement_map(crab_positions)
least_fuel = calculate_least_fuel(crab_positions, movement_map)

print(least_fuel)