nav_lines = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

class CorruptedNav:

    def __init__(self, nav_lines):
        self.nav_lines = nav_lines
        self.chunks = ["{}", "()", "[]", "<>"]
        self.opening_chars = [chunk[0] for chunk in self.chunks]
        self.closing_chars = [chunk[1] for chunk in self.chunks]
        self.error_mapping = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137
        }


    def find_total_syntax_error(self):
        incorrect_closing_chars = []
        for line in self.nav_lines.splitlines():
            incorect_closing_char = self.find_incorrect_closing(line)
            if incorect_closing_char:
                incorrect_closing_chars.append(incorect_closing_char)
    
        total_syntax_error = 0
        for closing_char in incorrect_closing_chars:

            total_syntax_error += self.error_mapping[closing_char]
        
        return total_syntax_error
    
    def find_incorrect_closing(self, line):
        
        chunks_present = True

        while chunks_present:
            for chunk in self.chunks:
                line = line.replace(chunk, "")

            # exit loop if there are no more chunks remaining
            chunks_present = any(chunk in line for chunk in self.chunks)

        for idx, current_symbol in enumerate(line):
            # exit loop once last symbol is reached
            if idx+1 == len(line):
                break

            next_symbol = line[idx + 1]

            if current_symbol in self.opening_chars and next_symbol in self.closing_chars:
                return next_symbol
        
        return None
        
nav_system = CorruptedNav(nav_lines)

print(nav_system.find_total_syntax_error())