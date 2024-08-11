raw_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


import copy

class Caves:
    def __init__(self, raw_input):
        self.formatted_input = self.format_input(raw_input)
        self.node_dict = self.create_node_dict()
    
    def format_input(self, raw_input):
        formatted_input = []
        for line in raw_input.splitlines():
            formatted_input.append(line.split("-"))

        return formatted_input

    def create_node_dict(self):
        
        all_nodes = []
        for combo in self.formatted_input:
            all_nodes.extend(combo)
        
        # remove duplicates
        all_nodes = list(set(all_nodes))

        node_dict = {}
        for node in all_nodes:
            connected_nodes = []
            for combo in self.formatted_input:
                if node in combo:
                    node_index = combo.index(node)
                    connected_nodes.append(combo[node_index-1])
            
            node_dict[node] = connected_nodes


        return node_dict
    
    
    def find_all_iterations(self):

        routes = []

        for starting_node in self.node_dict["start"]:
            routes.append(["start", starting_node])

        while True:
            
            discovered_routes = []
            for route in routes:
                
                current_node = route[-1]
                
                # route is complete if end is found - move onto next route
                if current_node == "end":
                    discovered_routes.append(route)
                    continue
                
                next_nodes = self.node_dict[current_node]

                # if start is a option from the node, then remove it.  
                # Start is only the origin and cannot be visited again
                if "start" in next_nodes:
                    next_nodes.remove("start")

                for next_node in next_nodes:
                    
                    local_route = copy.deepcopy(route)
                    
                    # Small caves, i.e. lowercase node, can only be visited once
                    # Do not consider these nodes if they have alrady been visited
                    small_cave = next_node.islower()
                    
                    if small_cave and next_node in route:
                        pass
                        # new_routes.append(local_route)
                    
                    else:
                        local_route.append(next_node)
                        discovered_routes.append(local_route)

            if discovered_routes:
                routes = copy.deepcopy(discovered_routes)
            
                    
            if all(route[-1] == "end" for route in routes):
                # all routes have been found and can exit
                break
            
            # Only putting this here to prevent my computer
            # from getting borked in case of code bug
            if len(routes) > 1000000:
                break
        
        return routes

            

caves = Caves(raw_input)

cave_routes = caves.find_all_iterations()

# debugging purposes
# formatted_solution = ""
# for cave_route in cave_routes:
#     formatted_solution += ",".join(cave_route) + "\n"

# print(formatted_solution)


len(cave_routes)
