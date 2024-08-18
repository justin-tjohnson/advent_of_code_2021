
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

def most_common_minus_least_common(polymer_count_map):

    max_qty = max(polymer_count_map.values())
    min_qty = min(polymer_count_map.values())
    return max_qty - min_qty


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

    @staticmethod
    def create_polymer_map_from_string(polymer_string):

        polymers_list = list(polymer_string)
        polymer_map = {}
        for idx, pol_char in enumerate(polymers_list):

            if idx+1 == len(polymers_list):
                break

            pol_pair = f"{pol_char}{polymers_list[idx+1]}"

            if pol_pair not in polymer_map:
                polymer_map[pol_pair] = 0

            polymer_map[pol_pair] += 1

        return polymer_map
    
    @staticmethod
    def create_official_count_dict(polymer_map, starting_pair, ending_pair):

        starting_included = False
        ending_included = False

        official_count = {}

        polymer_string = "".join(list(polymer_map.keys()))

        polymer_set = set(list(polymer_string))

        for polymer in polymer_set:
            official_count[polymer] = 0

        for polymer_pair, polymer_value in polymer_map.items():

            if polymer_pair == starting_pair and not starting_included:

                official_count[polymer_pair[0]] += 1 + (polymer_value-1)/2
                official_count[polymer_pair[1]] += polymer_value/2

                starting_included = True

                continue

            if polymer_pair == ending_pair and not ending_included:
                official_count[polymer_pair[0]] += polymer_value/2
                official_count[polymer_pair[1]] += 1 + (polymer_value-1)/2

                ending_included = True

                continue

            for polymer_char in polymer_pair:
                official_count[polymer_char] += polymer_value/2


        return official_count
    
    @staticmethod
    def add_two_maps_together(map1, map2):
        new_map = {}

        for map1_key, map1_value in map1.items():
            if map1_key in map2:
                new_value = map1_value + map2[map1_key]
                new_map[map1_key] = map1_value + map2[map1_key]
            
            else:
                new_value = map1_value
            
            if new_value == 0:
                continue
            
            new_map[map1_key] = new_value

        for map2_key, map2_value in map2.items():

            if map2_value == 0:
                continue

            if map2_key not in new_map:
                new_map[map2_key] = map2_value
        
        return new_map

    def find_new_polymer(self, loop_number):

        current_polymer = copy.deepcopy(self.template)
        current_polymer_map = self.create_polymer_map_from_string(self.template)
        print(current_polymer_map)

        starting_pair = current_polymer[:2]
        ending_pair = current_polymer[-2:]

        loops = list(range(1,loop_number+1))

        for _ in loops:

            new_polymer_map = {}

            starting_pair_replaced = False
            ending_pair_replaced = False

            # find replacements
            pair_replacements = []
            for pair_key, pair_value in self.pair_insertion_map.items():

                if pair_key in current_polymer_map:
                    pair_replacements.append((pair_key, pair_value))
            
            for pair_replacement in pair_replacements:
                
                current_count = current_polymer_map[pair_replacement[0]]
                current_polymer_map[pair_replacement[0]] = 0 

                new_pairs = [
                    (f"{pair_replacement[0][0]}{pair_replacement[1]}"), 
                    ((f"{pair_replacement[1]}{pair_replacement[0][1]}"))
                ]

                if pair_replacement[0] == starting_pair and not starting_pair_replaced:
                    starting_pair = f"{pair_replacement[0][0]}{pair_replacement[1]}"
                    starting_pair_replaced = True
                
                elif pair_replacement[0] == ending_pair and not ending_pair_replaced:
                    ending_pair = f"{pair_replacement[1]}{pair_replacement[0][1]}"
                    ending_pair_replaced = True

                for new_pair in new_pairs:

                    if new_pair not in new_polymer_map:
                        new_polymer_map[new_pair] = current_count

                    else:
                        new_polymer_map[new_pair] += current_count

            current_polymer_map = self.add_two_maps_together(current_polymer_map, new_polymer_map)

        return self.create_official_count_dict(current_polymer_map, starting_pair, ending_pair)


polymer_formula = PolymerFormula(template, pair_insertions)
new_formula = polymer_formula.find_new_polymer(40)
print(most_common_minus_least_common(new_formula))
            

        







    