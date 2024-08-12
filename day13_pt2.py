raw_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

import copy

class Paper:
    def __init__(self, raw_input):
        self.coordinates, self.folds = self.format_input(raw_input)
        self.initial_grid = self.create_initial_grid()
        self.folded_grid = self.create_folds_in_paper()
    
    def format_input(self, raw_input):
        coordinates = []
        folds = []
        for line in raw_input.splitlines():
            if "," in line:
                line_list = line.split(",")
                coordinates.append([int(number) for number in line_list])
            if "fold" in line:
                fold_type = "x" if "x" in line else "y"

                folds.append((fold_type, int(line.split("=")[-1])))
                
                
        return coordinates, folds

    def create_initial_grid(self):
        # Grid represented by row or rows

        x_coordinates = [coordinate[0] for coordinate in self.coordinates]
        y_coordinates = [coordinate[1] for coordinate in self.coordinates]

        self.x_max = max(x_coordinates)
        self.y_max = max(y_coordinates)

        row = [0]*(self.x_max+1)
        grid = [row]*(self.y_max+1)

        for coordinate in self.coordinates:
            (x_coordinate, y_coordinate) = coordinate
            local_row = copy.deepcopy(grid[y_coordinate])
            local_row[x_coordinate] = 1      
            grid[y_coordinate]= local_row
        
        return grid

    @staticmethod
    def add_two_rows_together(row1, row2):

        new_row = []

        for idx, row1_value in enumerate(row1):
            row2_value = row2[idx]
            
            new_value = 1 if (row1_value + row2_value > 0 ) else 0
            new_row.append(new_value)
        
        return new_row
        
    def create_folds_in_paper(self):

        local_grid = copy.deepcopy(self.initial_grid)

        for fold in self.folds:
            fold_line_id = fold[1]

            y_max = len(local_grid) - 1
            x_max = len(local_grid[0]) - 1


            if "y" in fold:
                fold_range = list(range(fold[1]+1, y_max+1))

                for folded_row_id in fold_range:
                    row_id_to_update = 2*fold_line_id-folded_row_id
                    
                    # need to allow for page overhang
                    if row_id_to_update < 0:
                        new_row = local_grid[folded_row_id]
                        local_grid = new_row.extend(local_grid)
                    else:

                        local_grid[row_id_to_update] = self.add_two_rows_together(
                            local_grid[folded_row_id],
                            local_grid[row_id_to_update]
                        )

                del local_grid[fold_line_id:fold_range[-1]+1]  

            # x fold
            else:
                
                fold_range = list(range(fold[1]+1, x_max+1))
                
                for folded_column_id in fold_range:

                    column_id_to_update = 2*fold_line_id-folded_column_id
                    

                    for row_id, row in enumerate(local_grid):
                        # if the fold isn't placed exactly in the middle,
                        # the edge fo the page could overhand.  Need to account 
                        # for this case
                        if column_id_to_update < 0:
                            # add new row to left of grid
                            new_row = row[folded_column_id]
                            new_row = new_row.extend(row)
                        
                        else:
                            row[column_id_to_update] = 1 if (row[folded_column_id]+row[column_id_to_update])>0 else 0
                        
                        local_grid[row_id] = row

                
                # now delete columns that were folded
                for idx, row in enumerate(local_grid):
                    del row[fold_line_id:fold_range[-1]+1]
                    local_grid[idx] = row

        return local_grid

    def count_folded_dots(self):
        dot_count = 0
        for row in self.folded_grid:
            dot_count += row.count(1)

        return dot_count

    
paper_instance = Paper(raw_input)

formatted_answer = ""

for row in paper_instance.folded_grid:
    row = ["." if value == 0 else "#" for value in row ]
    row_str = "".join(row)
    formatted_answer += row_str + "\n"

print(formatted_answer)
