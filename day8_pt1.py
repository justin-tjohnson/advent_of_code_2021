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
        self.number_map = {
            0: 5,
            1: 2,
            2: 5,
            3: 5,
            4: 4,
            5: 5,
            6: 6,
            7: 3,
            8: 7,
            9: 6
        }
        self.unique_numbers = (1,4,7,8)
        self.unique_number_map = {
            number:qty for (number,qty) in self.number_map.items() if number in self.unique_numbers
        }

        self.signal_patterns, self.output_values = self.format_raw_inputs()

    def format_raw_inputs(self):
        signal_patterns = []
        output_values = []
        for line in input_code.splitlines():
            split_by_delimiter = line.split("|")
            signal_patterns.append(split_by_delimiter[0])
            output_values.append(split_by_delimiter[1])
        return signal_patterns, output_values

    def find_unique_digits(self):

        unique_digit_code_map = {}

        unique_digit_qty_map = {unique_number:0 for unique_number in self.unique_numbers}

        for output_value in self.output_values:

            output_value_stripped = output_value.strip()
            current_output_values = output_value_stripped.split(" ")

            for unique_number in self.unique_numbers:
                unique_digit_code_map[unique_number] = [
                    output_value for output_value in current_output_values if len(output_value) == self.number_map[unique_number]
                ]

            for unique_number, codes in unique_digit_code_map.items():
                if codes:
                    unique_digit_qty_map[unique_number] += len(codes)
        return unique_digit_qty_map

    def unique_digit_occurences(self):
        unique_digit_qtys = self.find_unique_digits()

        return sum(unique_digit_qtys.values())



decode_signal_patterns = DecodeSignalPatterns(input_code)

final_count = decode_signal_patterns.unique_digit_occurences()
print(final_count)