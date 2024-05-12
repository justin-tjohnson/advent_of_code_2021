input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


class HydroThermalVents:

    def __init__(self, input):
        self.input = input
        self.formatted_input = []
        self.board_diagram = []
        self.no_line_indicator = 0

        self.read_raw_input()
        self.create_board_diagram()
    
    def read_raw_input(self):
        for line in self.input.splitlines():
            formatted_line_string = line.replace(" -> ", ",")
            formatted_line_list = formatted_line_string.split(",")
            formatted_line_list_int = [int(coordinate) for coordinate in formatted_line_list]
            self.formatted_input.append(formatted_line_list_int)

    def find_line_coordinates(self, x1, y1, x2, y2): 
        zero_length_line = y1 == y2 == x1 == x2
        is_horizontal = y1 == y2
        is_vertical = x1 == x2
        is_diagonal = abs(x2-x1) == abs(y2-y1)

        if zero_length_line:
            # zero line length, will not draw on board
            return None
        
        elif is_diagonal:
            # not going anything with this for now but suspect I will during pt2
            # so setting up functionality prematurely
            return None
            drawn_coordinates = []
            y_coordinates = list(range(y1, y2))
            x_coordinates = list(range(x1, x2))

            # x and y coordinate list have to be the same length by definition so only looping throughx
            drawn_coordinates = [[x_coordinates[i], y_coordinates[i]] for i in range(len(x_coordinates))]


        elif is_vertical:
            y_coordinates = [y1, y2]
            y_coordinate_iter = list(range(min(y_coordinates), max(y_coordinates)+1))
            drawn_coordinates = [[x1, y_coordinate] for y_coordinate in y_coordinate_iter]

        elif is_horizontal:
            x_coordinates = [x1, x2]
            x_coordinates_iter = list(range(min(x_coordinates), max(x_coordinates)+1))
            drawn_coordinates = [[x_coordinate, y1] for x_coordinate in x_coordinates_iter]

        return drawn_coordinates

    
    def draw_line_on_board(self, drawn_coordinates):
        for drawn_coordinate in drawn_coordinates:
            # unpack coordinates
            x_coordinate = drawn_coordinate[0]
            y_coordinate = drawn_coordinate[1]

            current_val = self.board_diagram[y_coordinate][x_coordinate]

            if current_val == self.no_line_indicator:
                self.board_diagram[y_coordinate][x_coordinate] = 1
    
            elif isinstance(current_val, int):
                self.board_diagram[y_coordinate][x_coordinate] += 1
            
            # don't expect this condition to ever get flagged but putting it here anyway:
            else:
                raise ValueError(
                    f"Board value with a value of {current_val} and type {type(current_val)}" 
                    f" at coodinate [{x_coordinate}, {y_coordinate}] is not recognized. Must "
                    "be an int"
                )

    def create_board_diagram(self):

        #initialize board.  x coordinate are only assigned in 0 and 2 index, and y are only asigned in 1 and 3 indexes
        x_coordinates = [int(line[0]) for line in self.formatted_input] + [int(line[2]) for line in self.formatted_input]
        y_coordinates = [int(line[1]) for line in self.formatted_input] + [int(line[3]) for line in self.formatted_input]
        
        x_range = max(x_coordinates) - min(x_coordinates)
        y_range = max(y_coordinates) - min(y_coordinates)
        add_1_to_x_if_0_present = 0
        add_1_to_y_if_0_present = 0

        if 0 in (max(x_coordinates), min(x_coordinates)):
            add_1_to_x_if_0_present = 1
        
        if 0 in (max(y_coordinates), min(y_coordinates)):
            add_1_to_y_if_0_present = 1

        # adding 1 since 0 index still counts as a position on the diagram
        rows = [self.no_line_indicator]*(x_range + add_1_to_x_if_0_present)
        self.board_diagram = [rows[:] for _ in range(y_range + add_1_to_y_if_0_present)]


        for x1,y1,x2,y2 in self.formatted_input:
            drawn_coordinates = self.find_line_coordinates(x1, y1, x2, y2)

            if drawn_coordinates:
                self.draw_line_on_board(drawn_coordinates)
    
    def calculate_intersecting_lines(self):
        intersecting_lines = 0
        for row in self.board_diagram:
            interscting_points = [point for point in row if point > 1]
            intersecting_lines += len(interscting_points)
        
        return intersecting_lines

hydro_thermal_instance = HydroThermalVents(input)

print(hydro_thermal_instance.calculate_intersecting_lines())