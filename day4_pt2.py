number_genetator = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1"""


raw_boards = """22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

raw_board = raw_boards.splitlines()

class BingoBoards:
    def __init__(self, raw_boards, drawn_numbers):
        self.raw_boards = raw_boards
        self.drawn_numbers = drawn_numbers.split(",")


        self.formatted_boards = []
        self.boolean_board = []
        self.winning_boards = []
        self.format_boards()
        self.initialize_boolean_board()
    
    def format_boards(self):
        # format raw string bingo boards into list of bingo boards. 
        # Each individual board is formatted as list of lists.

        # For example, for the following board:
        #   1 2 3 
        #   1 3 1
        #   2 3 4
        # 
        # Would be formatted as this:
        # [ ["1", "2", "3"], ["1", "3", "1"], ["2", "3", "4"] ]

        individual_board = []

        raw_boards_list = raw_boards.splitlines()
        for index, row in enumerate(raw_boards_list):
            row_stripped = row.strip()
            row_with_comma_delimiter = row_stripped.replace("  ", ",").replace(" ", ",")
            row_list = row_with_comma_delimiter.split(",")

            is_empty_line = row_with_comma_delimiter == ""
            
            # empty line indicates start of a new individual board
            if is_empty_line:
                self.formatted_boards.append(individual_board)
                individual_board = []
                continue

            # add row to individual_list board since since row is still apart of the board
            individual_board.append(row_list)
            
            # last row of raw_boards string.  Append final individual board
            if index + 1 == len(raw_boards_list) and not is_empty_line:
                self.formatted_boards.append(individual_board)

    def scan_individual_board_for_bingo(self, bingo_board):
        # scan through rows
        for row in bingo_board:
            if all(row):
                return True
        
        # scan through columns
        for index in range(len(bingo_board[0])):
            if all(row[index] for row in bingo_board):
                return True
        
        return False
            
    
    def scan_boards_for_bingo(self):
        #scan through each bingo board
        for bingo_board_id, bingo_board in enumerate(self.boolean_board):
            # stop checkinb board if it has already won
            if self.winning_boards[bingo_board_id]:
                continue
            board_status = self.scan_individual_board_for_bingo(bingo_board)
            if board_status:
                return board_status, bingo_board_id
            
        return False, None
    
    def initialize_boolean_board(self):
        for bingo_board in self.formatted_boards:
            individual_board = []
            for row in bingo_board:
                boolean_row = [False for _ in row]
                individual_board.append(boolean_row)
            self.boolean_board.append(individual_board)
            self.winning_boards.append(False)
        
    def update_boolean_board(self, matching_bingo_coodinates, drawn_number):

        for matching_bingo_coodinate in matching_bingo_coodinates:

            bingo_id = matching_bingo_coodinate[0]
            row_id = matching_bingo_coodinate[1]
            col_id = matching_bingo_coodinate[2]

            self.boolean_board[bingo_id][row_id][col_id] = True

    def find_matching_numbers(self, drawn_number):

        matching_bingo_coodinates = []

        for bingo_id, bingo_board in enumerate(self.formatted_boards):

            for row_id, row in enumerate(bingo_board):

                for col_id, col_val in enumerate(row):

                    if drawn_number == col_val:
                        matching_bingo_coodinates.append([bingo_id, row_id, col_id])
        
        return matching_bingo_coodinates

    def tally_up_final_score(self, winning_bingo_board_id, last_drawn_number):

        winning_bingo_board = self.formatted_boards[winning_bingo_board_id]
        winning_boolean_board = self.boolean_board[winning_bingo_board_id]

        sum_unmarked = 0

        for row_id, row in enumerate(winning_boolean_board):
            for col_id, col_val in enumerate(row):
                if not col_val:
                    sum_unmarked += int(winning_bingo_board[row_id][col_id])
        
        return sum_unmarked * int(last_drawn_number)

    def determine_winning_board(self):

        for drawn_number in self.drawn_numbers:
            matching_bingo_coodinates = self.find_matching_numbers(drawn_number)

            if matching_bingo_coodinates:
                self.update_boolean_board(matching_bingo_coodinates, drawn_number)

            winning_board, bingo_board_id = self.scan_boards_for_bingo()

            if winning_board:
                print(drawn_number, self.winning_boards)
                print(self.boolean_board)
                self.winning_boards[bingo_board_id] = winning_board

            
            if all(self.winning_boards):
                break
        
        if all(self.winning_boards):
            final_score = self.tally_up_final_score(bingo_board_id, drawn_number)
            return final_score
            
        

bingo_boards = BingoBoards(raw_boards, number_genetator)
print(f"The final score is {bingo_boards.determine_winning_board()}")
