import itertools

input_code = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""



class DecodeSignalPatterns:
    def __init__(self, input_code):
        self.input_code = input_code
        self.signal_patterns, self.output_values, self.entire_lines = self.format_raw_inputs()
        self.all_possible_combinations = list(itertools.permutations(["a", "b", "c","d","e","f","g"]))

        # location is defined as the signals that correspond to the digit display as 
        # shown below
        #     0000
        #    5    1
        #    5    1
        #     6666
        #    4    2
        #    4    2
        #     3333
        self.signal_location_map = {
            0: [0,1,2,3,4,5],
            1: [1,2],
            2: [0,1,6,4,3],
            3: [0,1,6,2,3],
            4: [5,6,1,2],
            5: [0,5,6,2,3],
            6: [0,5,6,2,3,4],
            7: [0,1,2],
            8: [0,1,2,3,4,5,6],
            9: [0,1,6,5,2,3]

        } 

    def format_raw_inputs(self):
        signal_patterns = []
        output_values = []
        entire_lines = []
        for line in input_code.splitlines():
            split_by_delimiter = line.split("|")
            signal_patterns.append(split_by_delimiter[0])
            output_values.append(split_by_delimiter[1])
            entire_lines.append(line.replace("| ", ""))
        return signal_patterns, output_values, entire_lines
    

    def find_output_values_sum(self):

        output_numbers = []

        for idx, entire_line in enumerate(self.entire_lines):

            entire_line_stripped = entire_line.strip()
            current_entire_line = entire_line_stripped.split(" ")
    
            signal_combination = self.filter_by_possible_numbers(current_entire_line)
        
            output_value = self.output_values[idx]
            output_value_stripped = output_value.strip()
            current_output_values = output_value_stripped.split(" ")

            output_number_list = self.find_output_numbers(current_output_values, signal_combination)
            output_number_string = "".join([str(number) for number in output_number_list])
            output_numbers.append(int(output_number_string))

        return sum(output_numbers)

    def find_output_numbers(self, output_values, signal_combination):
        found_digits = []
        for output_value in output_values:
        
            for digit, location_map in self.signal_location_map.items():
                letter_map = [signal_combination[location] for location in location_map]

                output_value_found = all(letter in output_value for letter in letter_map) and len(output_value) == len(letter_map)

                if output_value_found:
                    found_digits.append(digit)
    
        return found_digits

    def check_for_possible_number(self, theoretical_position_map, signal_value):

        is_possible = False
        for digit, signal_map in theoretical_position_map.items():
            # to be a possible match, the length of the signal must match the theoretical signal value and all
            # letters must exist in both (order doesn't matter)
            is_possible = all(signal in signal_value for signal in signal_map) and len(signal_value) == len(signal_map)
            if is_possible:
                break

        return is_possible, digit
        

    def filter_by_possible_numbers(self, signal_values):

        for possible_combination in self.all_possible_combinations:
            theoretical_position_map = self.signal_location_map.copy()
    
            for digit, original_location_map in self.signal_location_map.items():
                original_location_map = self.signal_location_map[digit]
                signal_map = [possible_combination[location] for location in original_location_map]
                theoretical_position_map[digit] = signal_map
            # print(theoretical_position_map)

            is_possible_list = []
            matching_numbers = []
            for signal_value in signal_values:
                is_possible, digit = self.check_for_possible_number(theoretical_position_map, signal_value)
                
                if is_possible:
                    matching_numbers.append(digit)

                is_possible_list.append(is_possible)
            
            # there must be a match for all numbers 0 through nine with the signal configuration an d 
            # all signals must have a plausible matching number
            all_numbers_covered = all(number in matching_numbers for number in list(range(10)))
            if all(is_possible_list) and all_numbers_covered:
                return possible_combination

       
decode_signal_patterns = DecodeSignalPatterns(input_code)
final_count = decode_signal_patterns.find_output_values_sum()
print(final_count)