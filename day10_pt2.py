
nav_lines = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
(((({<>}<{<{<>}{[]{[]{} 
{<[[]]>}<{[{[{[]{()[[[]
<{([{{}}[<[[[<>{}]]]>[]]"""

class CorruptedNav:

    def __init__(self, nav_lines):
        self.nav_lines = nav_lines
        self.chunks = ["{}", "()", "[]", "<>"]
        self.opening_chars = [chunk[0] for chunk in self.chunks]
        self.closing_chars = [chunk[1] for chunk in self.chunks]
        self.error_mapping = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4
        }

    def find_midele_score(self):

        all_scores = []
        for line in self.nav_lines.splitlines():
            line_is_incomplete, cleaned_line = self.is_line_incomplete(line)
            if line_is_incomplete:
                # print(cleaned_line)
                total_score = self.find_line_score(cleaned_line)
                all_scores.append(total_score)
        all_scores.sort()
        middleIndex = int((len(all_scores) - 1)/2)

        return all_scores[middleIndex]

    def find_line_score(self, cleaned_line):
        chars_to_complete = []

        cleaned_line = cleaned_line[::-1]
        total_score = 0
        for symbol in cleaned_line:
            matching_symbol = [chunk.replace(symbol, "") for chunk in self.chunks if symbol in chunk][0]
            total_score *= 5
            total_score += self.error_mapping[matching_symbol]

            chars_to_complete.append(matching_symbol)
    
        return total_score

    def is_line_incomplete(self, line):
        
        chunks_present = True

        while chunks_present:
            for chunk in self.chunks:
                line = line.replace(chunk, "")

            # exit loop if there are no more chunks remaining
            chunks_present = any(chunk in line for chunk in self.chunks)

        # remove empty spaces
        line = line.replace(" ", "")

        for idx, current_symbol in enumerate(line):
            # exit loop once last symbol is reached
            if idx+1 == len(line):
                break

            next_symbol = line[idx + 1]

            if current_symbol in self.opening_chars and next_symbol in self.closing_chars:
                return False, line
        
        return True, line
        
nav_system = CorruptedNav(nav_lines)

print(nav_system.find_midele_score())