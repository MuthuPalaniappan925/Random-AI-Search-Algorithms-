##Creation of Graph -> unweighted graph
from collections import defaultdict
graph = defaultdict(list)

##To add edge to the graph
graph['A'].append('B')
graph['A'].append('C')
graph['B'].append('D')
graph['B'].append('E')

##To print the entire graph
#print(dict(graph))

##To print some edges for the nodes
#print(f"Edge A: {graph['A']}")

##Creation of Graph -> weighted graph
graph_weighted = defaultdict(dict) ##allows you to assign (weights) directly to each edge / list is not possible
graph_weighted['A']['B'] = 1
graph_weighted['A']['C'] = 2
graph_weighted['B']['D'] = 3
graph_weighted['B']['E'] = 4

print("Weighted Graph using defaultdict:", dict(graph_weighted))