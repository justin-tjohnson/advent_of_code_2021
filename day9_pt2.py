# %%
height_map = """2199943210
3987894921
9856789892
8767896789
9899965678"""


class HeightMap:
    def __init__(self, height_map):
        self.formatted_height_map = self.format_height_map(height_map)
        self.row_indexes = range(len(self.formatted_height_map))
        self.col_indexes = range(len(self.formatted_height_map[0]))
    
    def format_height_map(self, height_map):

        formatted_height_map = []
        for line in height_map.splitlines():
            row = [int(number) for number in line]
            formatted_height_map.append(row)
        
        return formatted_height_map
    
    def find_surrounding_numbers(self, central_pos, excluding_pos=None):

        row_pos, col_pos = central_pos[0], central_pos[1]
        # gather surrounding positions (only up down left and right)
        surrounding_positions = (
            (row_pos+1, col_pos),
            (row_pos-1, col_pos),
            (row_pos, col_pos+1),
            (row_pos, col_pos-1)
        )

        if excluding_pos:
            surrounding_positions = tuple(
                (pos[0], pos[1]) for pos in surrounding_positions if pos not in excluding_pos
            )
   
        surrounding_number_map = {}
        for pos in surrounding_positions:
            if pos[0] in self.row_indexes and pos[1] in self.col_indexes:
                surrounding_number_map[pos] = self.formatted_height_map[pos[0]][pos[1]]

        return surrounding_number_map

    def find_low_point_positions(self):
    
        low_point_map = {}
        
        for col_pos in range(len(self.formatted_height_map[0])):
            for row_pos in range(len(self.formatted_height_map)):
                
                current_number = self.formatted_height_map[row_pos][col_pos]
                
                surrounding_number_map = self.find_surrounding_numbers((row_pos, col_pos))
                surrounding_numbers = list(surrounding_number_map.values())

                if all(
                    current_number<surrounding_number for surrounding_number in surrounding_numbers
                ):
                    low_point_map[(row_pos, col_pos)] = current_number
        
        return low_point_map
    
    def find_basin_numbers_from_low_point(self, low_point_position):

        if low_point_position == (4,6):
            pass

        # initial basin position to start searching from is just the low point
        basin_positions = [low_point_position]

        surrounding_number_map = self.find_surrounding_numbers(low_point_position)
        surrounding_number_maps = [surrounding_number_map]

        # keep searching until there aren't any more surrounding numbers
        while surrounding_number_maps:
    
            current_surr_number_maps = []
            for surrounding_number_map in surrounding_number_maps:
                
                for surr_pos, surr_number in surrounding_number_map.items():
                    # stop searching for additional surrounding numbers if 9 is reached
                    # i.e. end of basin
                    if surr_number == 9:
                        continue

                    if surr_pos not in basin_positions:
                        basin_positions.extend([surr_pos])
                    current_surr_number_maps.append(self.find_surrounding_numbers(surr_pos, excluding_pos=basin_positions))
            
            surrounding_number_maps = current_surr_number_maps.copy()

        return basin_positions


    def find_basins(self):

        low_point_map = self.find_low_point_positions()

        all_basin_lengths = []
        for low_point_pos in low_point_map.keys():
            basin_positions = self.find_basin_numbers_from_low_point(low_point_pos)
            all_basin_lengths.append(len(basin_positions))

        return all_basin_lengths

    def product_of_three_largest_basins(self):

        basin_sizes = self.find_basins()
        basin_sizes.sort(reverse=True)

        return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    
height_map = HeightMap(height_map)

print(height_map.product_of_three_largest_basins())
# %%
