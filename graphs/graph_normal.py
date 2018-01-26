'''
    The normal illustration of the graph without using Class and Methods
'''

# The below is the illustration of graph in dictionary form
# Keys are nodes and values are connected nodes

graph = {
    "a" : ["c"],
    "b" : ["c", "e"],
    "c" : ["a", "b", "d", "e"],
    "d" : ["c"],
    "e" : ["c", "b"],
    "f" : []
}

# function to generate list of all edges

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

# Function to find isolated nodes
def find_isolated_nodes(graph):
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated

if __name__ == "__main__":
    print(generate_edges(graph))
    print(find_isolated_nodes(graph))