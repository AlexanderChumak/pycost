
from RoadGraphBuilder import build_graph

build_graph()


graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5

graph['a'] = {}
graph['a']['end'] = 1

graph['end'] = {}
print(graph)

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = float('inf')

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
        parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print('costs', costs)
print('parents', parents)
print('processed', processed)