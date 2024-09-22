
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


def add_node_to_graph(graph, node1, node2):

    if node1 not in graph:
        graph[node1] = [node2]
    elif node2 not in graph[node1]:
        graph[node1].append(node2)

    return graph

def formulate_graph(raw_input):
    graph = {}
    edges = []
    for line in raw_input.splitlines():
        start_node, end_node = line.split("-")

        graph = add_node_to_graph(graph, start_node, end_node)

        graph = add_node_to_graph(graph, end_node, start_node)      

    return graph

import copy

def small_cave_visited_twice(current_route):
    for cave in current_route:
        if cave.islower() and current_route.count(cave) == 2:
            return True
    return False

def find_cave_routes(raw_input):

    graph = formulate_graph(raw_input)

    all_routes = []

    current_node = "start"
    current_routes = [[current_node]]
    counter = 0

    while True:

        discovered_routes = []
        for current_route in current_routes:
            current_node = current_route[-1]
            adjacent_nodes = graph[current_node]

            for adjacent_node in adjacent_nodes:

                if small_cave_visited_twice(current_route) and adjacent_node.islower() and adjacent_node in current_route:
                    continue
            
                if adjacent_node == "start":
                    continue

                if adjacent_node == "end":
                    route = copy.deepcopy(current_route)
                    route.append(adjacent_node)
                    all_routes.append(route)
                    continue

                route = copy.deepcopy(current_route)
                route.append(adjacent_node)
                discovered_routes.append(route)

        # no more routes to discovere
        if not discovered_routes:
            break

        counter += 1

        if counter >100:
            break

        current_routes = copy.deepcopy(discovered_routes)

    return all_routes

cave_routes = find_cave_routes(raw_input)
print(len(cave_routes))
