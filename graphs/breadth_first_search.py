import unittest

# Runtime = O(V + E)



#    A
#  /   \
# C     B
# |   /   \
# |  D     E 
# |        |
#  \      /
#    F _/ 


def bfs(graph, start):
    '''Returns all nodes in graph'''
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# print(bfs(graph, 'A')) # {'B', 'C', 'A', 'F', 'D', 'E'}

def bfs_paths(graph, start, goal):
    '''Returns all possible paths between starting node and goal node'''
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# print(list(bfs_paths(graph, 'A', 'F'))) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

# print(shortest_path(graph, 'A', 'F')) # ['A', 'C', 'F']

class Test(unittest.TestCase):


    def test_bfs(self):
        actual = bfs({'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}, 'A')
        expected = ({'B', 'C', 'A', 'F', 'D', 'E'})
        self.assertEqual(actual, expected)

    def test_bfs_paths(self):
        input_graph = ({'A': set(['B', 'C']),
                            'B': set(['A', 'D', 'E']),
                            'C': set(['A', 'F']),
                            'D': set(['B']),
                            'E': set(['B', 'F']),
                            'F': set(['C', 'E'])})
        expected_result = ([['A', 'C', 'F'], ['A', 'B', 'E', 'F']])
        result = list(bfs_paths(input_graph, 'A', 'F'))
        self.assertEqual(expected_result, result)

    def test_shortest_path(self):
        actual = shortest_path({'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}, 'A', 'F')
        expected = (['A', 'C', 'F'])
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)

