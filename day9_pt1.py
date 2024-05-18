height_map = """2199943210
3987894921
9856789892
8767896789
9899965678"""


class HeightMap:
    def __init__(self, height_map):
        self.formatted_height_map = self.format_height_map(height_map)
    
    def format_height_map(self, height_map):

        formatted_height_map = []
        for line in height_map.splitlines():
            row = [int(number) for number in line]
            formatted_height_map.append(row)
        
        return formatted_height_map
    
    def find_surrounding_numbers(
            self, 
            row_pos, 
            col_pos,                     
            row_indexes,          
            col_indexes,
        ):
        
        # gather surrounding positions (only up down left and right)
        surrounding_positions = [
            (row_pos+1, col_pos),
            (row_pos-1, col_pos),
            (row_pos, col_pos+1),
            (row_pos, col_pos-1)
        ]

        # do not compare to surrounding positions that don't exist
        surrounding_positions = [
            pos for pos in surrounding_positions if pos[0] in row_indexes and pos[1] in col_indexes
        ]
        surrounding_numbers = [
            self.formatted_height_map[row_id][col_id] for (row_id, col_id) in surrounding_positions
        ]

        return surrounding_numbers

    def find_low_point_positions(self):
    
        low_points = []

        row_indexes = range(len(self.formatted_height_map))
        col_indexes = range(len(self.formatted_height_map[0]))
        
        for col_pos in range(len(self.formatted_height_map[0])):
            for row_pos in range(len(self.formatted_height_map)):
                
                current_number = self.formatted_height_map[row_pos][col_pos]
                
                surrounding_numbers = self.find_surrounding_numbers(
                    row_pos, 
                    col_pos,
                    row_indexes,
                    col_indexes
                )

                if all(
                    current_number<surrounding_number for surrounding_number in surrounding_numbers
                ):
                    low_points.append(current_number)
        
        return low_points
    
    def sum_risk_levels(self):
        low_points = self.find_low_point_positions()
        risk_levels = [low_point+1 for low_point in low_points]

        return sum(risk_levels)
    
height_map = HeightMap(height_map)

print(height_map.sum_risk_levels())