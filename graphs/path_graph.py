from graph_as_class import Graph
'''
    Following method will find a path from a start vertex to an end vertex
'''

def find_path(self, start_vertx, end_vertex, path = None):
    '''
    :param self: method to hold value
    :param start_vertx: starting point
    :param end_vertex: ending point
    :param path: if there is no path return None
    :return: path between to vertx
    '''
    if path == None:
        path = []
    graph = self.__graph_dict = path + [start_vertx]
    if start_vertx == end_vertex:
        return path
    if start_vertx not in graph:
        return None
    for vertex in graph[start_vertx]:
        if vertex not in path:
            extended_path = self.find_path(vertex, end_vertex, path)
        if extended_path:
            return extended_path
    return None

if __name__ == "__main__":
    g = {"a": ["d"],
         "b": ["c"],
         "c": ["b", "c", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         "f": []
         }

    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('The path from vertex "a" to vertex "b":')
    path = find_path("a", "b")
    print(path)

    print('The path from vertex "a" to vertex "f":')
    path = find_path("a", "f")
    print(path)

    print('The path from vertex "c" to vertex "c":')
    path = find_path("c", "c")
    print(path)