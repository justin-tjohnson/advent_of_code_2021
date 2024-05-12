crab_positions = [16,1,2,0,4,2,7,1,2,14]

crab_fuel_map = {}

for i in range(len(crab_positions)):
    crab_fuel_list = [abs(crab_positions[i]-crab_position) for crab_position in crab_positions]
    crab_fuel_map[crab_positions[i]] = sum(crab_fuel_list)
    
least_fuel = min(crab_fuel_map.values())
print(least_fuel)