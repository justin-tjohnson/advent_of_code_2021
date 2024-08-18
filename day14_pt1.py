template = "NNCB"

pair_insertions = """CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

import copy

def most_common_minus_least_common(polymers):

    polymer_map = {}

    polymer_list = list(polymers)

    polymer_set = set(polymer_list)

    for polymer in polymer_set:
        polymer_qty = polymer_list.count(polymer)
        polymer_map[polymer] = polymer_qty
        
    max_polymer = max(polymer_map, key=polymer_map.get)
    min_polymer = min(polymer_map, key=polymer_map.get)


    return polymer_map[max_polymer] - polymer_map[min_polymer]

class PolymerFormula:

    def __init__(self, template, pair_insertions):
        self.template = template
        self.pair_insertion_map = self.format_pair_insertions(pair_insertions)

    @staticmethod
    def format_pair_insertions(pair_insertions):
        foramtted_pair_insertsions = {}
        for line in pair_insertions.splitlines():
            pair_key, pair_value = line.split(" -> ")
            foramtted_pair_insertsions[pair_key] = pair_value

        return foramtted_pair_insertsions
    

    def find_new_polymer(self, loop_number):

        current_polymer = copy.deepcopy(self.template)

        loops = list(range(1,loop_number+1))

        for _ in loops:
            new_polymer = copy.deepcopy(current_polymer)
            new_polymer_list = list(new_polymer)
            
            new_polymer_list_map = []
            for polymer in new_polymer_list:
                new_polymer_list_map.append((polymer, "unswapped"))


            # find replacements
            pair_replacements = []
            for pair_key, pair_value in self.pair_insertion_map.items():

                if pair_key in current_polymer:
                    pair_replacements.append((pair_key, pair_value))

            for pair_replacement in pair_replacements:

                index = 0
                while True:
                    (letter, letter_status) = new_polymer_list_map[index]


                    if index+1 == len(new_polymer_list_map):
                        break

                    next_letter = new_polymer_list_map[index+1][0]
                    next_letter_status = new_polymer_list_map[index+1][1]

                    # If letter has already been swapped in list, then do not consider this for additional
                    # swapping.  This is here to preserve simultaneous swapping in original list
                    if any("swapped" == status for status in (letter_status, next_letter_status)):
                        index += 1
                        continue
                    
                    if (f"{letter}{next_letter}") == pair_replacement[0]:
                        new_polymer_list_map = (
                            new_polymer_list_map[:index+1] + 
                            [(pair_replacement[1], "swapped")]+
                            new_polymer_list_map[index+1:]
                        )
                    
                    index += 1

            new_polymer_list = [letter_map[0] for letter_map in new_polymer_list_map]

            new_polymer = "".join(new_polymer_list)

            if new_polymer:
                current_polymer = copy.deepcopy(new_polymer)

        return current_polymer
    

polymer_formula = PolymerFormula(template, pair_insertions)


new_formula = polymer_formula.find_new_polymer(10)


print(most_common_minus_least_common(new_formula))
            
                
            


    
    
    


    