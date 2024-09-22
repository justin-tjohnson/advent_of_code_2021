raw_input = """ex-NL
ex-um
ql-wv
VF-fo
VF-ql
start-VF
end-tg
wv-ZQ
wv-um
NL-start
lx-ex
ex-wv
ex-fo
sb-start
um-end
fo-ql
NL-sb
NL-fo
tg-NL
VF-sb
fo-wv
ex-VF
ql-sb
end-wv"""

import copy


def create_cave_dict(raw_input):
    cave_dict = {}
    for line in raw_input.splitlines():
        starting_cave, ending_cave = line.split("-")

        if starting_cave not in cave_dict:
            cave_dict[starting_cave] = []

        if ending_cave not in cave_dict:
            cave_dict[ending_cave] = []
        
        if ending_cave not in cave_dict[starting_cave]:   
            cave_dict[starting_cave].append(ending_cave)

        if starting_cave not in cave_dict[ending_cave]:   
            cave_dict[ending_cave].append(starting_cave)
    
    return cave_dict



def is_small_cave(cave):
    return cave.islower()

def small_cave_visited_twice(current_route):
    for cave in current_route:
        if is_small_cave(cave) and current_route.count(cave)==2:
            return True
    return False


def find_cave_routes(cave_dict):

    current_route = ["start"]
    discovered_routes = [current_route]
    current_node = current_route[-1]
    all_routes = []


    counter = 0
    while True:
    
        counter += 1
        current_routes = copy.deepcopy(discovered_routes)
        discovered_routes = []
        

        for current_route in current_routes:

            current_node = current_route[-1]

            adjacent_nodes = cave_dict[current_node]
            for adjacent_node in adjacent_nodes:

                # don't visit start cave again
                if adjacent_node == "start":
                    continue
                    
    
                if small_cave_visited_twice(current_route) and is_small_cave(adjacent_node) and adjacent_node in current_route:
                    continue
                
                new_route = copy.deepcopy(current_route)
                new_route.append(adjacent_node)

                
                if adjacent_node == "end":
                    all_routes.append(new_route)
                    continue

                discovered_routes.append(new_route)



        if all(route[-1] == "end" for route in discovered_routes):
            break
    
    return(all_routes)


cave_dict = create_cave_dict(raw_input)

cave_routes = find_cave_routes(cave_dict)
print(len(cave_routes))