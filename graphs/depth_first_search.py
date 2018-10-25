import unittest 

#    A
#  /   \
# C     B
# |   /   \
# |  D     E 
# |        |
#  \      /
#    F _/ 


def dfs_iterative_1(graph, start):
    visited= set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def dfs_iterative_2(graph, start):
    # keep track of paths
    stack = [start] 
    # keep track of explored nodes
    explored = set()
    # iterate through graph until reach deadend
    while stack:
        # add last item to explored if not in there
        vertex = stack.pop()
        if vertex in explored:
            continue
        explored.add(vertex)
        # add neighbor to stack 
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    return explored

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_recursive(graph, next, visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


class Test(unittest.TestCase):

    def test_dfs_iterative_1(self):
        actual = dfs_iterative_1({'A': set(['B', 'C']),
                                'B': set(['A', 'D', 'E']),
                                'C': set(['A', 'F']),
                                'D': set(['B']),
                                'E': set(['B', 'F']),
                                'F': set(['C', 'E'])}, 'A')
        expected = ({'E', 'D', 'F', 'A', 'C', 'B'})
        self.assertEqual(actual, expected)

    def test_dfs_iterative_2(self):
        actual = dfs_iterative_2({'A': set(['B', 'C']),
                                'B': set(['A', 'D', 'E']),
                                'C': set(['A', 'F']),
                                'D': set(['B']),
                                'E': set(['B', 'F']),
                                'F': set(['C', 'E'])}, 'A')
        expected = ({'E', 'D', 'F', 'A', 'C', 'B'})
        self.assertEqual(actual, expected)

    def test_dfs_recursive(self):
        actual = dfs_recursive({'A': set(['B', 'C']),
                                'B': set(['A', 'D', 'E']),
                                'C': set(['A', 'F']),
                                'D': set(['B']),
                                'E': set(['B', 'F']),
                                'F': set(['C', 'E'])}, 'A')
        expected = ({'E', 'D', 'F', 'A', 'C', 'B'})
        self.assertEqual(actual, expected)

    def test_dfs_paths(self):
        input_graph = ({'A': set(['B', 'C']),
                        'B': set(['A', 'D', 'E']),
                        'C': set(['A', 'F']),
                        'D': set(['B']),
                        'E': set(['B', 'F']),
                        'F': set(['C', 'E'])})
        expected_result = ([['A', 'C', 'F'], ['A', 'B', 'E', 'F']])
        result = list(dfs_paths(input_graph, 'A', 'F'))
        self.assertEqual(expected_result, result)


unittest.main(verbosity=2)

